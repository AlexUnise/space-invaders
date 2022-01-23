from PIL import Image,ImageTk
import os

#classe Alien pour attribuer le nombre de vie, la cadence de tir et le comportment de l'alien       
class Alien:
    #Classe Alien
    #Chaque Alien à une coordonnée x et une coordonnée y.
    #On definit sa taille ainsi que sa hitbox
    #dx et dy réprésentent sa vitesse sur chaque axe
    def __init__(self,canvas,wind,positionx,positiony):
        self.width = 50
        self.height = 50
        self.__positionx=positionx
        self.__positiony=positiony
        self.__dx = 5
        self.__dy = 30
        self.__canvas=canvas
        self.__wind=wind


        scriptDir = os.path.dirname(__file__)
        imgpath = os.path.join(scriptDir, '../Assets/space_invaders_alien.png')
        img= Image.open(imgpath)
        self.__canvas_img = ImageTk.PhotoImage(img)
        self.rect=self.__canvas.create_image(self.__positionx+self.width,self.__positiony+self.height, image=self.__canvas_img)  

    
    #Methode qui permet au alien de se deplacer verticalement ou horizontalement sur le canvas, en fonction de la des entrees
    #ou le signe est la direction horizontale de l'alien, et le DownMovement est le deplacement ou pas vers le bas.
    def move_alien(self,signe,DownMovement):
        self.__canvas.move(self.rect,signe*self.__dx,DownMovement*self.__dy )
            
    #Methode qui verifie si l'alien touche les bord du canvas.
    def border_overlapping(self,signe,DownMovement):

        (x0,y0)=self.__canvas.coords(self.rect)
        if x0+self.width+(signe*self.__dx)>int(self.__canvas.cget('width')):
            signe=-1
            DownMovement=1
        elif x0-self.width+(signe*self.__dx)<0:
            signe=1
            DownMovement=1
        return signe,DownMovement
    

    
