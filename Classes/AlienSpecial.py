from PIL import Image,ImageTk
import os

from Classes.Projectile import Projectile

from random import randint

#Classe contenant les informations et les methodes pour l'ennemi special
class AlienSpecial:
    def __init__(self,canvas,wind,positionx,positiony):
        self.bonusScore=150
        self.width = 50
        self.height = 50
        self.__positionx=positionx
        self.__positiony=positiony
        self.__dx = 5
        self.__dy = 0
        self.__canvas=canvas
        self.__wind=wind
        self.rect=0

    
    #Methode qui place l'ennemi special sur le canvas
    def place_special(self):
        scriptDir = os.path.dirname(__file__)
        imgpath = os.path.join(scriptDir, '../Assets/space_invaders_special.png')
        img= Image.open(imgpath)
        self.__canvas_img = ImageTk.PhotoImage(img)
        self.rect=self.__canvas.create_image(self.__positionx+self.width,self.__positiony+self.height, image=self.__canvas_img) 
        
        self.special_move()


    #Methode qui permet au ennemi special de bouger
    def special_move(self):
         if self.rect in self.__canvas.find_all():
            (x0,y0)=self.__canvas.coords(self.rect)
            if x0+self.width+(self.__dx)>int(self.__canvas.cget('width')):
                self.__dx=-self.__dx
            elif x0-self.width+(self.__dx)<0:
                self.__dx=-self.__dx
        
            self.__canvas.move(self.rect,self.__dx,self.__dy )
            self.__wind.after(10,self.special_move)

