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
    def __init__(self):
        self.__width=int(2500/2.25)
        self.__height=int(1406/2.25)
        
        #Fenêtre
        
        self.__wind=Tk()
        self.__wind.geometry('1280x655')
        self.__wind.title('Space Invaders')
       
        #Canvas
        self.__canvas=Canvas(self.__wind,bg="white", width=self.__width, height=self.__height)
        img= Image.open("background.jpg")
        resized_image= img.resize((self.__width,self.__height), Image.ANTIALIAS)
        backgroundImage= ImageTk.PhotoImage(resized_image)
        self.__backImg=self.__canvas.create_image(0,0, image=backgroundImage, anchor = "nw")
        self.__canvas.grid(column=0, row=1, sticky="w")
        

        #Aliens
        self.__alien=Alien(self.__canvas,self.__wind)
        self.__queue=[]
        self.__aliens=2
        
        
        #Joueuer
        self.__player=Player(int(self.__width/2),self.__height-50,20,50,50,self.__canvas,self.__wind)
        
        #Lancer le jeu
        self.start()
    
        
        
    def start(self):
        wind=self.__wind
        scoreLabel = Label(wind, text="Score: 0")
        livesLabel = Label(wind, text="Lives: 3")
        quitButton = Button(wind, text="Quit game", command=wind.destroy)
        newGameButton = Button(wind, text="New game")


        wind.columnconfigure(0, weight=1)
        wind.columnconfigure(1, weight=1)

        wind.rowconfigure(1, minsize=500)

        scoreLabel.grid(column=0, row=0, sticky="W")
        livesLabel.grid(column=0, row=0, sticky="E")
        newGameButton.grid(column=1, row=0, sticky="s")
        quitButton.grid(column=1, row=1, sticky='n')
        
        self.__alien.place_aliens()
        self.__player.place_player()
        self.__alien.move_alien()
        self.__canvas.focus_set()
        self.__canvas.bind('<Key>',self.keyboard)
        
        
        wind.mainloop()
       
    
        
        
   
        

    def keyboard(self,event):
        (x0,y0,x1,y1)=self.__canvas.coords(self.__player.rect)
        key=event.keysym
        if key=='d' and x1+self.__player.dx<self.__width:
            self.__player.moveRight(self.__canvas)

        if key=='q' and x0-self.__player.dx>0:
            self.__player.moveLeft(self.__canvas)   
        if key=='f':
            projectile_joueur=Projectile(self.__canvas,self.__wind,self.__player,self.__backImg)
            projectile_joueur.placer_projectile()
            projectile_joueur.tirer_projectile()
            
        
#classe Alien pour attribuer le nombre de vie, la cadence de tir et le comportment de l'alien       
class Alien:
    #Classe Alien
    #Chaque Alien à une coordonnée x et une coordonnée y.
    #On definit sa taille ainsi que sa hitbox
    #dx et dy réprésentent sa vitesse sur chaque axe
    def __init__(self,canvas,wind):
        self.__lives=1
        self.__hitbox=50
        self.width = 50
        self.height = 50
        self.__positionx=0
        self.__positiony=0
        self.__dx = 10
        self.__dy = 0
        self.__queue=[]
        self.__canvas=canvas
        self.__wind=wind
    

    def move_alien(self):
        (x0,y0,x1,y1)=self.__canvas.coords(self.__queue[0])
        if x1+(self.__dx)>int(self.__canvas.cget('width')):
            self.__dx=-self.__dx
        if x0+self.__dx<0:
            self.__dx=-self.__dx
            self.__dy=50
        self.__canvas.move(self.__queue[0],self.__dx,self.__dy )
        self.__dy=0
        self.__wind.after(20,self.move_alien)

    def place_aliens(self):
        self.__queue.append(self.__canvas.create_rectangle (self.__positionx,self.__positiony,self.__positionx+self.width,self.__positiony+self.height,fill="red"))

    

    
    
    

    
    
class Player:
    #Classe Joueur
    #Un joueur peut se déplacer uniquement sur l'axe x. Le programmeur définit sa coordonnée y. 
    #dx réprésente la vitesse de déplacement sur l'axe, définie par le programmeur.
    #La fonction draw déssine pour la première fois le player sur le canvas
    #Les fonctions moveRight et moveLeft permettent de déplacer le joueur sur le canvas.
    
    def __init__(self,x,y,dx,width,height,canvas,wind):
        self.__name=""
        self.__lives=3
        self.__score=0
        self.__positionx = x
        self.__positiony = y
        self.dx = dx
        self.width = width
        self.height = height
        self.__canvas=canvas
        self.__wind=wind
        
        
    def place_player(self):
        self.rect=self.__canvas.create_rectangle (self.__positionx,self.__positiony,self.__positionx+self.width,self.__positiony+self.height,fill="green")
    
    def moveLeft(self,canvas):
        canvas.move(self.rect,-self.dx, 0)
    def moveRight(self,canvas):
        canvas.move(self.rect,self.dx, 0)




class Projectile:
    def __init__(self,canvas,wind,entity,backImg):
        self.__height=10
        self.__width=4
        self.__dy=20
        self.__canvas=canvas
        self.__wind=wind
        self.__entity=entity
        self.__backImg=backImg
        
    def placer_projectile(self):
        (x0,y0,x1,y1)=self.__canvas.coords(self.__entity.rect)
        self.projectile=self.__canvas.create_rectangle(x0+int(self.__entity.width/2),y0-5,x0+int(self.__entity.width/2)+self.__width,y0-5-self.__height,fill="yellow")
        
    
    def tirer_projectile(self):
        
        (x_proj0,y_proj0,x_proj1,y_proj1)=self.__canvas.coords(self.projectile)
        liste_objet=self.__canvas.find_overlapping(x_proj0,y_proj0,x_proj1,y_proj1)
        print(liste_objet)
        if y_proj0-self.__dy>0:
            self.__canvas.move(self.projectile,0,-self.__dy)
            self.__wind.after(20,self.tirer_projectile)
        elif len(liste_objet)!=0:
            self.__canvas.delete(self.projectile)
            for objet in liste_objet:
                if objet!=self.__backImg:
                    self.__canvas.delete(objet)
        else:
            self.__canvas.delete(self.projectile)
        



class Bloc:
    def __init__(self):
        self.__height=3
        self.__width
    
    