from Node import *
from Compare import *

class LinkedList():
    def __init__(self):
        self.first = None
        self.size = 0
         

    def add(self,value):
        if(not self.first):
            self.first = Node(value)
        else:
            compare = Compare()
            if(compare.compare(self.first.name,value) > 0):
                stack = self.first
                self.first = Node(value)
                self.first.next = stack
                return True
            elif(compare.compare(self.first.name,value) == 0):
                stack = self.first.next
                self.first = Node(value)
                self.first.next = stack
                return True
            elif(compare.compare(self.first.name,value) < 0):
                if(not self.first.next):
                    self.first.next = Node(value)
                else:    
                    previous = self.first
                    current = self.first.next
                    while(current):                       
                        if(compare.compare(current.name,value) < 0):
                            previous = current
                            current = current.next
                        elif(compare.compare(current.name,value) > 0):
                            previous.next = Node(value)
                            previous.next.next = current
                            return True
                        else:
                            stack = current.next
                            previous.next = Node(value)
                            previous.next.next = stack
                            return True
                    current = Node(value)
                    return True         
        self.size = self.size + 1               

    def _print(self):
        current = self.first        
        return self._printIn(current)

    def _printIn(self,current):
        array = [] 
        while(current):
            array.append(current.name)
            current = current.next
        return array
        