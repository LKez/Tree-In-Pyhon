from Source.Node import *
from Source.Compare import *

class LinkedList():
    def __init__(self):
        self.first = None
        self.size = 0
      

    def add(self,value):
        if(not self.first):
            if(isinstance(value,Node)):
                self.first = value
            else:        
                self.first = Node(value)
        else:
            compare = Compare()
            if(compare.compare(self.first.name,value) > 0):
                stack = self.first
                if(isinstance(value,Node)):
                    self.first = value
                else:    
                    self.first = Node(value)
                self.first.next = stack
                return True
            elif(compare.compare(self.first.name,value) == 0):
                stack = self.first.next
                if(isinstance(value,Node)):
                    self.first = value
                else:    
                    self.first = Node(value)
                self.first.next = stack
                return True
            elif(compare.compare(self.first.name,value) < 0):
                if(not self.first.next):
                    if(isinstance(value,Node)):
                        self.first.next = value
                    else:    
                        self.first.next = Node(value)
                else:    
                    previous = self.first
                    current = self.first.next
                    while(current.next):                       
                        if(compare.compare(current.name,value) < 0):
                            previous = current
                            current = current.next
                        elif(compare.compare(current.name,value) > 0):
                            if(isinstance(value,Node)):
                                previous.next = value
                            else:    
                                previous.next = Node(value)
                            previous.next.next = current
                            return True
                        else:
                            stack = current.next
                            if(isinstance(value,Node)):
                                previous.next = value
                            else:    
                                previous.next = Node(value)
                            previous.next.next = stack
                            return True
                    if(compare.compare(current.name,value) > 0):
                        if(isinstance(value,Node)):
                                previous.next = value
                        else:    
                            previous.next = Node(value)
                        previous.next.next = current
                        return True
                    if(isinstance(value,Node)):        
                        current.next = value
                    else:
                        current.next = Node(value)    
                    return True

    def length(self):
        current = self.first
        while(current):
            self.size = self.size + 1           
        return self.size
    def _print(self):
        current = self.first        
        return self._printIn(current)

    def _printIn(self,current):
        array = [] 
        while(current):
            array.append(current.name)
            if(current.children.first):
                array.append(self._printIn(current.children.first))
            current = current.next
        return array
                       

    def addIn(self,value,parent):
        parnt = self.search(parent)
        parnt.children.add(value)

        
    def search(self,parent,current=""):
        current = self.first
        while(current):
            if current.name == parent:
                return current
            elif(current.children.first != None):
                answer = current.children.search(parent)
                if answer != None:
                    return answer
            current = current.next    

    def delete(self,parent,father=""):
        if(father == ""):
            return self.deleteIn(parent)
        else:    
            fath = self.search(father)
            return fath.children.deleteIn(parent)

    def deleteIn(self,parent):
        if(parent == self.first.name):
            stack = self.first.next
            self.first = stack
            return True
        else:
            previous = self.first
            current = self.first.next
            while(current):
                if(parent == current.name):
                    stack = current.next
                    previous.next = stack
                    return True
                else:
                    previous = current
                    current = current.next
        return False            

    def _printInTree(self):
        array = []
        current = self.first
        while(current):
            array.append(current.name)
            current = current.next
        return array    