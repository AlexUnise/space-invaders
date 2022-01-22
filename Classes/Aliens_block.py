from Classes.Alien import Alien

class Aliens_block:
    def __init__(self,canvas,wind):
        self.__canvas=canvas
        self.__wind=wind
        self.__height=3
        self.__width=8
        self.__aliens=[]
        self.__positionx=0
        self.__positiony=0
        self.__signeDx=1
        self.__DownMovement=0
    
    def create_bloc(self):
        placementy=self.__positiony
        for columns in range(0,self.__height):
            ligne_alien=[]
            placementx=self.__positionx
            
            for rows in range(0,self.__width):
                alien=Alien(self.__canvas,self.__wind,placementx,placementy)
                ligne_alien.append(alien)
                placementx+=60
            self.__aliens.append(ligne_alien)
            placementy+=60
        
    def move_bloc(self):
        self.__DownMovement=0
        for ligne in self.__aliens:
            if self.__signeDx==1:
                [self.__signeDx,self.__DownMovement]=ligne[-1].border_overlapping(self.__signeDx,self.__DownMovement)
                
            elif self.__signeDx==-1:
                [self.__signeDx,self.__DownMovement]=ligne[0].border_overlapping(self.__signeDx,self.__DownMovement)

        for ligne in self.__aliens:
            for alien in ligne:
                alien.move_alien(self.__signeDx,self.__DownMovement)
        self.__wind.after(20,self.move_bloc)
    