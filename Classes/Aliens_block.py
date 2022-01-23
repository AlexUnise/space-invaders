from Classes.Alien import Alien

def objectToID(object):
    return object.alien

#Classe qui gere la creation de multiples alien en bloc
class Aliens_block:
    def __init__(self,canvas,wind,player,score_counter):
        self.__canvas=canvas
        self.__wind=wind
        self.__height=3
        self.__width=12
        self.aliens=[]
        self.__positionx=0
        self.__positiony=0
        self.__signeDx=1
        self.__DownMovement=0
        self.__aliensHit=[]
        self.__player = player
        self.score_counter = score_counter


    #Methode qui permet de creer et de placer multiples alien en formation rectangulaire sur le canvas
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



    #Methode qui va deplacer la formation d'alien dans le sens oppose de leur mouvement, 
    #le moment ou les aliens aux extremites touchent les bord du canvas, tout en verifiant
    # si un alien a ete touche par le joueur. 
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


    #Methode qui recoit l'alien touche par un projectile du joueur et qui le sauvegarde dans une liste    
    def add_aliens_hit(self,id):
        self.__aliensHit.append(id)


    #Methode qui detruit les aliens qui ont ete touches par le joueur
    def destroy_alien(self):
        for ligne in self.aliens:
            for alien in ligne:
                for id in self.__aliensHit:
                    if id==alien.rect:
                        ligne.pop(ligne.index(alien))
                        self.__aliensHit.pop(self.__aliensHit.index(id))
                        self.__canvas.delete(alien.rect)
                        self.__player.score += 1
                        self.score_counter.set('Score: ' + str(self.__player.score))
                        if ligne==[]:
                            self.aliens.pop(self.aliens.index(ligne))
        if self.aliens==[]:
            self.__player.score+=20
            self.score_counter.set('Score: ' + str(self.__player.score))
            self.__player.game_over(0)
    


        
