class Player:
    #Classe Joueur
    #Un joueur peut se déplacer uniquement sur l'axe x. Le programmeur définit sa coordonnée y. 
    #dx réprésente la vitesse de déplacement sur l'axe, définie par le programmeur.
    #La fonction draw déssine pour la première fois le player sur le canvas
    #Les fonctions moveRight et moveLeft permettent de déplacer le joueur sur le canvas.
    
    def __init__(self,x,y,dx,width,height,canvas,wind):
        self.__name=""
        self.__lives=3
        self.__score=0
        self.__positionx = x
        self.__positiony = y
        self.dx = dx
        self.width = width
        self.height = height
        self.__canvas=canvas
        self.__wind=wind
        
        
    def place_player(self):
        self.rect=self.__canvas.create_rectangle (self.__positionx,self.__positiony,self.__positionx+self.width,self.__positiony+self.height,fill="green")
    
    def moveLeft(self,canvas):
        canvas.move(self.rect,-self.dx, 0)
    def moveRight(self,canvas):
        canvas.move(self.rect,self.dx, 0)
