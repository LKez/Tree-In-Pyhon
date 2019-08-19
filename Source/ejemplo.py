
from Tree import *

v = Tree()
c = Compare()
v.add("867")
v.add("afd")
v.add("zas")
v.add("@4345")
v.add("!345")
v.addIn("23",v.root.first)
print(v.root.first.first.name)
#print(v.root.first.next.name)
#print(v.root.first.next.next.name)
"""print(c.compare("afd","867"))
print(c.compare("867","zas"))
print(c.compare("afd","zas"))"""
print(v._print())
array = ["/","Documentos/","BMTH.zip",["archivos/",["source.py","archivo.jpg"],"ejemplo.txt","eda/",["weqr.csv","sdgfs.tsv","hola.cpp",],"wer/"],"we.mp3"] #v._print()
print(type(array[2][3]))
filename = "ejemplo.txt"
content = ""
f = open(filename,"w")
def con(array,cont,q=0,tab=""):
    i = 0
    while(i < len(array)):
        if(isinstance(array[i],list)):
            cont = con(array[i],cont,q+1,"\t")
        else:
            cont = cont + "%s%s\n"%(tab*q,array[i])
        i = i+1        
            
    return cont
print(con(array,content))
print("Es una linkedlist : %s" % isinstance((v.root),LinkedList))
f.write(con(array,content))