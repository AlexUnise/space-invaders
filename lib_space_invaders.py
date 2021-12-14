#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Createurs: OUENADIO Alexandre, MICHALOPOULOS Zaphirios
Groupe: C
Description du fichier: Bibilothèque contenant toutes les fonctions et classes utiles au bon fonctionnement du programme.
"""

<<<<<<< HEAD
#classe Alien pour attribuer le nombre de vie, la cadence de tir et le comportment de l'alien

class Space_Invaders:
    def __init__(self):
        self.__width=int(2500/2.25)
        self.__height=int(1406/2.25)
        self.__pixelSize=50
        self.__queue=[]
        self.__aliens

    def create_matrix(self):
        for h in range(0:self.__height/self.__pixelSize):
            for w in range(0:self.__width/self.__pixelSize):
            
                self.__queue.appennd
    def move_aliens(self):

class Alien:
    def __init__(self):
        self.__lives=1
        self.__hitbox=50
        self.__positionx=0

    def get_pos(self):
        return self.__positionx
    
    def get_pos(self):
        return self.__positionx


class Player:
    def __init__(self):
        self.__name=""
        self.__lives=3
        self.__score=0
=======

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
        
>>>>>>> 23d985e67f66465bf297550d9abe4bead479b4e4
