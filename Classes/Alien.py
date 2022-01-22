#classe Alien pour attribuer le nombre de vie, la cadence de tir et le comportment de l'alien       
class Alien:
    #Classe Alien
    #Chaque Alien à une coordonnée x et une coordonnée y.
    #On definit sa taille ainsi que sa hitbox
    #dx et dy réprésentent sa vitesse sur chaque axe
    def __init__(self,canvas,wind,positionx,positiony):
        self.__lives=1
        self.__hitbox=50
        self.width = 50
        self.height = 50
        self.__positionx=positionx
        self.__positiony=positiony
        self.__dx = 5
        self.__dy = 30
        self.__canvas=canvas
        self.__wind=wind
        self.__alien=self.__canvas.create_rectangle(self.__positionx,self.__positiony,self.__positionx+self.width,self.__positiony+self.height,fill="red")
    

    def move_alien(self,signe,DownMovement):
        (x0,y0,x1,y1)=self.__canvas.coords(self.__alien)
        self.__canvas.move(self.__alien,signe*self.__dx,DownMovement*self.__dy)

            

    def border_overlapping(self,signe,DownMovement):
        (x0,y0,x1,y1)=self.__canvas.coords(self.__alien)

        if x1+(signe*self.__dx)>int(self.__canvas.cget('width')):
            signe=-1
            DownMovement=1
        elif x0+(signe*self.__dx)<0:
            signe=1
            DownMovement=1
        return signe,DownMovement
    
    def alien_hit(self):
        self.__alien
