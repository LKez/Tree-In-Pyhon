
class Compare():
    def __init__(self):
        self.alphabet = ".,-;:_^`~!@#$%&/()=?¡¿¡[]{*}012345678890ABCDEFGHIJKLMNÑOPQRSTUVwXYZÁÉÍÓÚÜabcdefghijklmnñopqrstuvwxyzáéíóúü"
        
    def compare(self,obj1,obj2):
        
        if(type(obj1) == "int"):
            obj1 = "%s" % obj1
        if(type(obj1) == "Node.Node"):
            obj1 = obj1.name
        if(type(obj2) == "int"):
            obj2 = "%s" % obj2
        if(type(obj2) == "Node.Node"):
            obj2 = obj2.name   

        obj1 = obj1.strip()
        obj2 = obj2.strip()

        if(obj1 == obj2):
            return 0;    
        else:
            lesser = self.compareLesserLength(obj1,obj2)
            for i in range(lesser):
                if(type(obj1[i]) != "undefined" and type(obj2[i]) != "undefined" and self.alphabet.index(obj1[i]) < self.alphabet.index(obj2[i])):
                    return -1
                elif(type(obj1[i]) != "undefined" and type(obj2[i]) != "undefined" and self.alphabet.index(obj1[i]) > self.alphabet.index(obj2[i])):      
                    return 1 
                if( len(obj1) < len(obj2)):
                    return -1
                return 1    

    def compareLesserLength(self,str1,str2):
        l = 0
        if(l < len(str1)):
            l = len(str1)
        if(l < len(str2)):
            l = len(str2)
        return l                