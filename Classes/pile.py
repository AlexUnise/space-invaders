#Classe pile
class Pile:
    def __init__(self):
        self.__pile=[]

    def empiler(self,element):
        self.__pile.append(element)
        return self.__pile

    def sommet(self):
        if len(self.__pile)==0:
            return None
        else:
            return self.__pile[-1]

    def depiler(self):
        if len(self.__pile)!=0:
            element=self.__pile.pop(-1)
            return element,self.__pile
        else:
            return None,None