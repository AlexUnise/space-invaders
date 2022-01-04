#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Createurs: OUENADIO Alexandre, MICHALOPOULOS Zaphirios
Groupe: C
Description du fichier: Bibilothèque contenant toutes les fonctions et classes utiles au bon fonctionnement du programme.
"""

from tkinter import Tk, Label, Button, Canvas, PhotoImage
from PIL import Image,ImageTk



class Space_Invaders:
    def __init__(self,wind):
        self.__width=int(2500/2.25)
        self.__height=int(1406/2.25)
        self.__alien=Alien()
        self.__queue=[]
        self.__aliens=2
        self.__wind=wind
        self.__canvas=Canvas(wind,bg="white", width=self.__width, height=self.__height)
        img= Image.open("background.jpg")
        resized_image= img.resize((self.__width,self.__height), Image.ANTIALIAS)
        backgroundImage= ImageTk.PhotoImage(resized_image)
        self.__canvas.create_image(0,0, image=backgroundImage, anchor = "nw")
        self.__canvas.grid(column=0, row=1, sticky="w")
        
    def place_aliens(self):
        self.__queue.append(self.__canvas.create_rectangle (self.__alien.get_posx(),self.__alien.get_posy(),self.__alien.get_posx()+self.__alien.get_size(),self.__alien.get_posy()+self.__alien.get_size(),fill="red"))
    
    def move_alien(self):
        (x0,y0,x1,y1)=self.__canvas.coords(self.__queue[0])
        if x1+(x1-x0)+(self.__alien.get_dx())>self.__width:
            dx=-self.__alien.get_dx()
        if x0-self.__alien.get_dx()<0:
            dx=self.__alien.get_dx()
        self.__canvas.move(self.__queue[0],self.__alien.get_dx(),self.__alien.get_dy())
        self.__wind.after(20,self.move_alien)
        
#classe Alien pour attribuer le nombre de vie, la cadence de tir et le comportment de l'alien       
class Alien:
    #Classe Alien
    #Chaque Alien à une coordonnée x et une coordonnée y.
    #On definit sa taille ainsi que sa hitbox
    #dx et dy réprésentent sa vitesse sur chaque axe
    def __init__(self):
        self.__lives=1
        self.__hitbox=50
        self.__size=50
        self.__positionx=0
        self.__positiony=0
        self.__dx = 10
        self.__dy = 0

    def get_posx(self):
        return self.__positionx
    
    def get_posy(self):
        return self.__positionx
    
    
    def get_dx(self):
        return self.__dx
    
    def get_dy(self):
        return self.__dy
    
    def get_size(self):
        return self.__size

class Player:
    def __init__(self):
        self.__name=""
        self.__lives=3
        self.__score=0

class Player:
    #Classe Joueur
    #Un joueur peut se déplacer uniquement sur l'axe x. Le programmeur définit sa coordonnée y. 
    #dx réprésente la vitesse de déplacement sur l'axe, définie par le programmeur.
    #La fonction draw déssine pour la première fois le player sur le canvas
    #Les fonctions moveRight et moveLeft permettent de déplacer le joueur sur le canvas.
    
    def __init__(self,x,y,dx,width,height,canvas):
        self.x = x
        self.y = canvas.cget('height') - y
        self.dx = dx
        self.width = width
        self.height = height
        
        
    def draw(self,canvas):
        self.rect = canvas.create_rectangle(self.x, self.y, 50, 50, outline="#fb0", fill="#fb0")
    def moveLeft(self,canvas):
        canvas.move(self.rect,self.x - self.dx, self.y)
    def moveRight(self,canvas):
        canvas.move(self.rect,self.x + self.dx, self.y)
