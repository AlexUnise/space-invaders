class File:
    def __init__(self):
        self.__file=[]
    def ajouter(self,element):
        liste=[]
        self.__file=liste.append(element)+self.__file
    def premier(self):
        if len(self.__pile)==[]:
            return None
        else:
            return self.__file[-1]
    def retirer(self):
        if len(self.__pile)!=[]:
            element=self.__file.pop(-1)
            return element,self.__file
        else:
            return None,None