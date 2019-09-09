# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from Source.Tree import *
from Source.read import vic,vic2,searchParent,convert

form_class = uic.loadUiType("Source/Window.ui")[0]
filename1 = "Memory/memory1.txt"
filename2 = "Memory/memory2.txt"
c = open(filename1,"r")
d = open(filename2,"r")
contentRead1 = c.read()
contentRead2 = d.read()
contentWrite1 = ""
contentWrite2 = ""
t1 = Tree()
vic(contentRead1,t1)
t2 = Tree()
vic(contentRead2,t2)
class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self,current,title,tree,file,ext = "",parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("Source/2window.ui",self)
        self.parent = parent
        self.file = file
        self.title = title
        self.extention = ext
        self.setWindowTitle(QtWidgets.QApplication.translate("Crear","Crear %s"%self.title))
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.label.setText(QtWidgets.QApplication.translate("Crear", "Nombre de %s"%self.title))
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.value = ""
        self.t = tree
        self.addButton.clicked.connect(self._add)
        self.cancelButton.clicked.connect(self.cancel)
        self.center()

    def cancel(self):
        self.lineEdit.clear()
        self.close()
        self.focusNextPrevChild(True)

    def _add(self):
        if(self.t == t1):
            listW = self.parent.listWidget1
            curr = self.parent.current1
        if(self.t == t2):
            listW = self.parent.listWidget2
            curr = self.parent.current2
        #current = listW.currentItem().text() 
        if(curr == None):    
            self.value = "%s%s"%(self.lineEdit.text(),self.extention)
            print(self.value)
            self.t.add(self.value)
            self.lineEdit.clear()
            self.close()
            self.focusNextPrevChild(True)
            print(self.t._print())
            array = self.t._print()
            content = ""
            f = open(self.file,"w")
            f.write(convert(self.t._print(),content))
            array1 = self.t._printInTree()
            listW.clear()        
            self.parent.listIcons(array1,listW,curr)
        else:
            #current = listW.currentItem().text()
            self.value = "%s%s"%(self.lineEdit.text(),self.extention)
            print(self.value)
            self.t.addChildren(self.value,curr)
            self.lineEdit.clear()
            self.close()
            self.focusNextPrevChild(True)
            print(self.t._print())
            parent1 = self.t.search(curr)
            array = self.t._print()
            array1 = parent1.children._printInTree() 
            content = ""
            f = open(self.file,"w")
            f.write(convert(self.t._print(),content))
            listW.clear()        
            self.parent.listIcons(array1,listW,curr)


    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)

    def closeEvent(self,event):
        event.accept()    


class MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.current1 = None
        self.current2 = None
        self.parents1 = []
        self.parents2 = []
        children = ChildWindow(self.current1,"Carpeta",t1,filename1,"/",parent=self)
        children1 = ChildWindow(self.current1,"Archivo",t1,filename1,"",parent=self)
        children2 = ChildWindow(self.current2,"Carpeta",t2,filename2,"/",parent=self)
        children3 = ChildWindow(self.current2,"Archivo",t2,filename2,"",parent=self)
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.listWidget1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)        
        array1 = t1._printInTree()
        array2 = t2._printInTree()
        self.listIcons(array1,self.listWidget1,self.current1)
        self.listIcons(array2,self.listWidget2,self.current2)           
        self.setWindowIcon(QIcon('Source/Icons/67170.svg'))
        self.addCarpet1.clicked.connect(lambda:children.show())
        children.lineEdit.setFocus()
        self.copyToSecondTree.clicked.connect(self.copyIn2)
        self.copyToFirstTree.clicked.connect(self.copyIn1)
        self.delete1.clicked.connect(self.del1)
        self.delete2.clicked.connect(self.del2)
        self.addFile1.clicked.connect(lambda:children1.show())
        children1.lineEdit.setFocus()
        self.addCarpet2.clicked.connect(lambda:children2.show())
        children2.lineEdit.setFocus()
        self.addFile2.clicked.connect(lambda:children3.show())
        children3.lineEdit.setFocus()
        self.listWidget1.itemDoubleClicked.connect(self._handleDoubleClick1)
        self.listWidget2.itemDoubleClicked.connect(self._handleDoubleClick2)
        self.center()
          
    def copyIn2(self,tree):
        tree = t2    
        if(self.current2 == None):
            parents = self.getItems(self.listWidget1)
            for i in range(len(parents)):
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:    
                    tree.add(parents[i])
            self.parents2.clear()    
            f = open(filename2,"w")
            f.write(convert(tree._print(),contentWrite2))
            self.listWidget2.clear()
            array = tree._printInTree()
            self.listIcons(array,self.listWidget2)
        else:
            parents = self.getItems(self.listWidget1)
            for i in range(len(parents)):
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:
                    tree.addChildren(parents[i],self.current2)    
            f = open(filename2,"w")
            f.write(convert(tree._print(),contentWrite2))
            self.listWidget2.clear()
            item = tree.search(self.current2)
            array = item.children._printInTree()
            self.listIcons(array,self.listWidget2,self.current2)    

    def copyIn1(self,tree):
        tree = t1    
        if(self.current1 == None):
            parents = self.getItems(self.listWidget2)
            for i in range(len(parents)):
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:    
                    tree.add(parents[i])
            self.parents1.clear()    
            f = open(filename1,"w")
            f.write(convert(tree._print(),contentWrite1))
            self.listWidget1.clear()
            array = tree._printInTree()
            self.listIcons(array,self.listWidget1)
        else:
            parents = self.getItems(self.listWidget1)
            for i in range(len(parents)):
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:
                    tree.addChildren(parents[i],self.current1)    
            f = open(filename1,"w")
            f.write(convert(tree._print(),contentWrite1))
            self.listWidget1.clear()
            item = tree.search(self.current1)
            array = item.children._printInTree()
            self.listIcons(array,self.listWidget1,self.current1)            

    def del1(self,parents,tree=t1):
        if(self.current1 == None):
            parents = self.getItems(self.listWidget1)
            for i in range(len(parents)):    
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:    
                    tree.delete(parents[i])
            self.parents1.clear()    
            f = open(filename1,"w")
            f.write(convert(tree._print(),contentWrite1))
            self.listWidget1.clear()
            array = t1._printInTree()
            self.listIcons(array,self.listWidget1)
        else:
            parents = self.getItems(self.listWidget1)
            for i in range(len(parents)):
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:
                    tree.delete(parents[i],self.current1)    
            f = open(filename1,"w")
            f.write(convert(tree._print(),contentWrite1))
            self.listWidget1.clear()
            item = t1.search(self.current1)
            array = item.children._printInTree()
            self.listIcons(array,self.listWidget1,self.current1)
            

    def del2(self,parent,tree=t2):
        if(self.current2 == None):
            parents = self.getItems(self.listWidget2)
            for i in range(len(parents)):    
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:    
                    tree.delete(parents[i])
            self.parents2.clear()    
            f = open(filename2,"w")
            f.write(convert(tree._print(),contentWrite2))
            self.listWidget2.clear()
            array = t2._printInTree()
            self.listIcons(array,self.listWidget2)
        else:
            parents = self.getItems(self.listWidget2)
            for i in range(len(parents)):
                if(parents[i] == "." or parents[i] == ".."):
                    pass
                else:
                    tree.delete(parents[i],self.current2)    
            f = open(filename2,"w")
            f.write(convert(tree._print(),contentWrite2))
            self.listWidget2.clear()
            item = t2.search(self.current2)
            array = item.children._printInTree()
            self.listIcons(array,self.listWidget2,self.current2)   

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)
        
    def listIcons(self,array,listW,curr=None):
        array2 = self.orderedItems(array)
        if(curr != None):
            listW.addItem(".")
            listW.addItem("..")
            for i in array2:
                item = QtWidgets.QListWidgetItem()
                if(i[-1] == "/"):
                    item.setText(i)
                    item.setIcon(QIcon("Source/Icons/folder.png"))
                    listW.addItem(item)
                else:
                    item.setText(i)
                    item.setIcon(QIcon("Source/Icons/file.png"))
                    listW.addItem(item)
        else:
            for i in array2:
                item = QtWidgets.QListWidgetItem()
                if(i[-1] == "/"):
                    item.setText(i)
                    item.setIcon(QIcon("Source/Icons/folder.png"))
                    listW.addItem(item)
                else:
                    item.setText(i)
                    item.setIcon(QIcon("Source/Icons/file.png"))
                    listW.addItem(item)

    def _handleDoubleClick1(self,item):
	    
        
        item = self.listWidget1.currentItem().text()
        if(item[-1] == "/"):
            self.current1 = item 
            self.parents1.append(self.current1)
            self.listWidget1.clear()
            print(self.parents1)
            parent = t1.search(self.current1)
            print(self.parents1)
            array = parent.children._printInTree()
            self.listIcons(array,self.listWidget1,self.current1)
        elif(item == ".."):
            parent = self.searchParent(self.parents1,self.current1,self.current1)
            if(parent == "root"):
                array = t1._printInTree()
                self.parents1.clear()
                self.listWidget1.clear()
                self.listIcons(array,self.listWidget1)
                self.current1 = None
            else:
                self.current1 = parent
                newParent = t1.search(self.current1)
                array = newParent.children._printInTree()
                self.listWidget1.clear()
                self.listIcons(array,self.listWidget1,self.current1)
                   
        #print(self.parents1)    
        
    def _handleDoubleClick2(self,item):
	    
        item = self.listWidget2.currentItem().text()
        if(item[-1] == "/"):
            self.current2 = item 
            self.parents2.append(self.current2)
            self.listWidget2.clear()
            print(self.parents2)
            parent = t2.search(self.current2)
            print(self.parents2)
            array = parent.children._printInTree()
            self.listIcons(array,self.listWidget2,self.current2)
        elif(item == ".."):
            parent = self.searchParent(self.parents2,self.current2,self.current2)
            if(parent == "root"):
                array = t2._printInTree()
                self.parents2.clear()
                self.current2 = None
                self.listWidget2.clear()
                self.listIcons(array,self.listWidget2)
            else:
                self.current2 = parent
                newParent = t2.search(self.current2)
                array = newParent.children._printInTree()
                self.listWidget2.clear()
                self.listIcons(array,self.listWidget2,self.current2)    
                

    def searchParent(self,array,parent,curr):
        if(len(array) == 1 ):
            x = "root"
            curr = None
        else:    
            for i in range(len(array)):
                if(array[i] == parent and len(array) > 1):
                    x = array[i-1]
                    array.pop()        
        return x
        
    def getItems(self,lst):
        items = lst.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(lst.selectedItems()[i].text()))
        return x       

    def orderedItems(self,array):
        array2 = []
        for i in array:
            if(i[-1] == "/"):
                array2.append(i)
        for i in array:
            if(i[-1] != "/"):
                array2.append(i)
        return array2    




