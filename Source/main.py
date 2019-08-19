# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from Tree import *

form_class = uic.loadUiType("Window.ui")[0]


t1 = Tree()
t1.add("...")
t2 = Tree()
t2.add("...")
class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self,title,tree,ext = ""):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("2window.ui",self)
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
        
        self.value = "%s%s"%(self.lineEdit.text(),self.extention)
        print(self.value)
        self.t.add(self.value)
        self.lineEdit.clear()
        self.close()
        self.focusNextPrevChild(True)
        print(self.t._print())
        array = self.t._print()
        filename = "../Memory/memory.txt"
        content = ""
        f = open(filename,"w")
        for i in range(len(array)):
            content = content + "%s\n\t"%array[i]

        f.write(content)


    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)

    def closeEvent(self,event):
        event.accept()    


class MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        children = ChildWindow("Carpeta",t1,"/")
        children1 = ChildWindow("Archivo",t1)
        children2 = ChildWindow("Carpeta",t2,"/")
        children3 = ChildWindow("Archivo",t2)
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.listWidget1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget1.itemDoubleClicked.connect(self._handleDoubleClick)
        self.listWidget2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget2.itemDoubleClicked.connect(self._handleDoubleClick)
        self.listWidget1.addItems(t1._print())    
        self.listWidget2.addItems(t2._print())    
        self.setWindowIcon(QIcon('../Icons/67170.svg'))
        self.addCarpet1.clicked.connect(lambda:children.show())
        children.lineEdit.setFocus()
        self.addFile1.clicked.connect(lambda:children1.show())
        children1.lineEdit.setFocus()
        self.addCarpet2.clicked.connect(lambda:children2.show())
        children2.lineEdit.setFocus()
        self.addFile2.clicked.connect(lambda:children3.show())
        children3.lineEdit.setFocus()
        self.center()
          
    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)

    def _handleDoubleClick(self,item):
	    
        item = self.listWidget1.currentItem().text()
        self.listWidget2.insertItem(2,"%s"%item)
        
        

        
        

app = QtWidgets.QApplication(sys.argv)
MyWindow = MainWindow()
MyWindow.show()
app.exec_()       
