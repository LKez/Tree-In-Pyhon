

def children():
    from Source.LinkedList import LinkedList
    return LinkedList()        

class Node():
    def __init__(self,name):
        self.children = children()
        self.name = name
        self.next = None

