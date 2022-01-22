from tkinter import Tk, Label, Button, Canvas, PhotoImage
from PIL import Image,ImageTk
import os

from Classes.Alien import Alien
from Classes.Player import Player
from Classes.Projectile import Projectile


class Space_Invaders:
    def __init__(self):
        self.__width=int(2500/2.25)
        self.__height=int(1406/2.25)
        
        #Fenêtre
        
        self.__wind=Tk()
        self.__wind.geometry('1280x655')
        self.__wind.title('Space Invaders')
       
        #Canvas

        scriptDir = os.path.dirname(__file__)
        impath = os.path.join(scriptDir, '../Assets/background.jpg')
        self.__canvas=Canvas(self.__wind,bg="white", width=self.__width, height=self.__height)
        img= Image.open(impath)
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
            