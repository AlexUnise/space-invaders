        
#classe Alien pour attribuer le nombre de vie, la cadence de tir et le comportment de l'alien       
class Alien:
    #Classe Alien
    #Chaque Alien à une coordonnée x et une coordonnée y.
    #On definit sa taille ainsi que sa hitbox
    #dx et dy réprésentent sa vitesse sur chaque axe
    def __init__(self,x,y,left_offset,right_offset,canvas,wind):
        self.__lives=1
        self.__hitbox=50
        self.width = 50
        self.height = 50
        self.__positionx=x
        self.__positiony=y
        self.__dx = 5
        self.__dy = 0
        self.__queue=[]
        self.__canvas=canvas
        self.__wind=wind
        self.__left_offset = left_offset
        self.__right_offset = right_offset
        self.rect = self.__canvas.create_rectangle(self.__positionx,self.__positiony,self.__positionx+self.width,self.__positiony+self.height,fill="red")
    

    def move_alien(self):
        (x0,y0,x1,y1)=self.__canvas.coords(self.__queue[0])
        if x1+self.__right_offset+self.__dx>int(self.__canvas.cget('width')):
            self.__dx=-self.__dx
        if x0-self.__left_offset+self.__dx<0:
            self.__dx=-self.__dx
            self.__dy=50
        self.__canvas.move(self.__queue[0],self.__dx,self.__dy)
        self.__dy=0
        self.__wind.after(20,self.move_alien)

    def place_aliens(self):
        self.__queue.append(self.rect)

    

    
    
    

    