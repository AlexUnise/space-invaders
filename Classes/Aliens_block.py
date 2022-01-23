from Classes.Alien import Alien

def objectToID(object):
    return object.alien


class Aliens_block:
    def __init__(self,canvas,wind,player,score_counter):
        self.__canvas=canvas
        self.__wind=wind
        self.__height=3
        self.__width=8
        self.aliens=[]
        self.__positionx=0
        self.__positiony=0
        self.__signeDx=1
        self.__DownMovement=0
        self.__aliensHit=[]
        self.__player = player
        self.__score_counter = score_counter

    def create_bloc(self):
        placementy=self.__positiony
        for rows in range(0,self.__height):
            ligne_alien=[]
            placementx=self.__positionx
            
            for columns in range(0,self.__width):
                alien=Alien(self.__canvas,self.__wind,placementx,placementy)
                ligne_alien.append(alien)
                placementx+=alien.width+10
            self.aliens.append(ligne_alien)
            placementy+=alien.height+10

    def move_bloc(self):
        
        self.__DownMovement=0

        if len(self.__aliensHit)>0:
            self.destroy_alien()


        for ligne in self.aliens:
            if self.__signeDx==1:
                [self.__signeDx,self.__DownMovement]=ligne[-1].border_overlapping(self.__signeDx,self.__DownMovement)
                
            elif self.__signeDx==-1:
                [self.__signeDx,self.__DownMovement]=ligne[0].border_overlapping(self.__signeDx,self.__DownMovement)

        for ligne in self.aliens:
            for alien in ligne:
                alien.move_alien(self.__signeDx,self.__DownMovement)
        
        
        self.__wind.after(60,self.move_bloc)
    
    def destroy_alien(self):
        for ligne in self.aliens:
            for alien in ligne:
                for id in self.__aliensHit:
                    if id==alien.rect:
                        ligne.pop(ligne.index(alien))
                        self.__aliensHit.pop(self.__aliensHit.index(id))
                        self.__canvas.delete(alien.rect)
                        self.__player.score += 1
                        self.__score_counter.set('Score: ' + str(self.__player.score))
                        if ligne==[]:
                            self.aliens.pop(self.aliens.index(ligne))
        

        
    
    def add_aliens_hit(self,id):
        self.__aliensHit.append(id)
