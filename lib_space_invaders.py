#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Createurs: OUENADIO Alexandre, MICHALOPOULOS Zaphirios
Groupe: C
Description du fichier: Bibilothèque contenant toutes les fonctions et classes utiles au bon fonctionnement du programme.
"""

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
