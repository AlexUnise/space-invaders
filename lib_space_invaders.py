#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Createurs: OUENADIO Alexandre, MICHALOPOULOS Zaphirios
Groupe: C
Description du fichier: Bibilothèque contenant toutes les fonctions et classes utiles au bon fonctionnement du programme.
"""


class Player:
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
        