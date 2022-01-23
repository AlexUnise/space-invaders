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
        self.rect=self.__canvas.create_image(self.__positionx+self.width,self.__positiony+self.height, image=self.__canvas_img) 
        
        self.special_move()
        #self.special_fire()

    def special_move(self):
        (x0,y0)=self.__canvas.coords(self.rect)
        if x0+self.width+(self.__dx)>int(self.__canvas.cget('width')):
            self.__dx=-self.__dx
        elif x0-self.width+(self.__dx)<0:
            self.__dx=-self.__dx
        if self.rect in self.__canvas.find_all():
            self.__canvas.move(self.rect,self.__dx,self.__dy )
            self.__wind.after(10,self.special_move)


    def special_fire(self):
        time=randint(800,1250)
        projectileAlienSpecial=Projectile(self.__canvas,self.__wind,self.rect,self.canvas_img_rect,self.__blockAlien,"alien",self.__player)
        projectileAlienSpecial.place_projectile()
        projectileAlienSpecial.fire_projectile()
        if self.__specialAlien.rect in self.__canvas.find_all():
            self.__wind.after(time,self.special_fire)