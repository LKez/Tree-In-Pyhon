from Source.LinkedList import *

class Tree():
    def __init__(self):
        self.root = LinkedList()
        self.size = 0
        
    def add(self,value):
        parent = self.root
        self.addIn(value,parent)

    def addIn(self,value,parent):
        parent.add(value)

    def addChildren(self,value,parent):
        self.root.addIn(value,parent)        

    def _print(self):
        current = self.root
        return current._print()

    def _printInTree(self):
        return self.root._printInTree()

    def delete(self,parent,father=""):
        self.root.delete(parent,father)

    def search(self,value):
       return self.root.search(value)

    def _printIn(self,value,parent):
        parent._printIn(parent.first)        