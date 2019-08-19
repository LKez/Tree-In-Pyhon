from LinkedList import *

class Tree():
    def __init__(self):
        self.root = LinkedList()
        self.size = 0
        
    def add(self,value):
        parent = self.root
        self.addIn(value,parent)
        self.size = self.size +1

    def addIn(self,value,parent):
        parent.add(value)    

    def _print(self):
        current = self.root
        return current._print()
        

    def _printIn(self,value,parent):
        parent._printIn(parent.first)        