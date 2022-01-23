class File:
    def __init__(self):
        self.__file=[]

    def ajouter(self,element):
        liste=[element]
        self.__file=liste + self.__file

    def premier(self):
        if len(self.__file)==0:
            return None
        else:
            return self.__file[-1]

    def retirer(self):
        if len(self.__file)!=0:
            element=self.__file.pop(-1)
            return element,self.__file
        else:
            return None,None