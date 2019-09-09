
from Source.Tree import *


def searchParent(array,parent):
    for i in range(len(array)):
        if(array[i] == parent):
            x = array[i-1]
    return x

def vic(cont,tree,current="",parent="",brother="",root=""):
    t = tree.root    
    parents = []
    rows = cont.split("\n")
    if(rows[-1] == ""):
        rows.pop()
    for row in rows:
        if(row.count("\t") == 0):
            t.add(row)
            parents.clear()
            current = row
            brother=""
            parent=""
            root = ""
            comp = ""
        else:
            if(brother.count("\t") > row.count("\t")):
                current = searchParent(parents,root)
            if(brother.count("\t") > row.count("\t")):
                root = searchParent(parents,root)
            if(brother.count("\t") < row.count("\t")):
                root = brother.replace("\t","")                       
            vic2(row,t,current,1,root,brother)
            if(parent == current and root != parent):
                parent = root
            else:
                parent = current    
            if(brother.count("\t") == row.count("\t")):
                current = row.replace("\t","")
            if(brother.count("\t") < row.count("\t")):    
                parents.append(parent)
                root = parent   
                current = row.replace("\t","")
            brother = row
            
def vic2(row,tree,current,q,parent,brother):#root):
    if(row.count("\t") == q):
        if(brother.count("\t") == row.count("\t")):
            row = row.replace("\t","")
            t = tree.search(parent)
            t.children.add(row)
        else:
            row = row.replace("\t","")    
            t = tree.search(current)
            t.children.add(row)
    elif(row.count("\t") > q):
        if(brother.count("\t") == row.count("\t")):
            vic2(row,tree,parent,q+1,parent,brother)
        else:
            vic2(row,tree,parent,q+1,parent,brother)    

def convert(array,cont,q=0,tab=""):
    i = 0
    while(i < len(array)):
        if(isinstance(array[i],list)):
            cont = convert(array[i],cont,q+1,"\t")
        else:
            cont = cont + "%s%s\n"%(tab*q,array[i])
        i = i+1        
            
    return cont