from PIL import Image,ImageTk
import os

from Classes.Projectile import Projectile

from random import randint

class AlienSpecial:
    def __init__(self,canvas,wind,positionx,positiony):
        self.width = 50
        self.height = 50
        self.__positionx=positionx
        self.__positiony=positiony
        self.__dx = 5
        self.__dy = 0
        self.__canvas=canvas
        self.__wind=wind
        self.rect=0

    

    def place_special(self):
        scriptDir = os.path.dirname(__file__)
        imgpath = os.path.join(scriptDir, '../Assets/space_invaders_alien.png')
        img= Image.open(imgpath)
        self.__canvas_img = ImageTk.PhotoImage(img)
        self.rect=self.__canvas.create_image(self.__positionx,self.__positiony, image=self.__canvas_img) 

    def Special_fire(self):
        time=randint(800,1250)
        projectileAlienSpecial=Projectile(self.__canvas,self.__wind,self.__Special,self.canvas_img_rect,self.__blockAlien,"alien",self.__player)
        projectileAlienSpecial.place_projectile()
        projectileAlienSpecial.fire_projectile()
        self.__wind.after(time,self.Special_fire)