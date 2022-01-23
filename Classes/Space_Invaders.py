from tkinter import Tk, Label, Button, Canvas, StringVar
from PIL import Image,ImageTk
import os

from Classes.Alien import Alien
from Classes.AlienSpecial import AlienSpecial
from Classes.Aliens_block import Aliens_block
from Classes.Player import Player
from Classes.Projectile import Projectile
from Classes.Protection import Protection

from random import randint



class Space_Invaders:
    def __init__(self):
        self.__width=int(2500/2.25)
        self.__height=int(1406/2.25)
        
        #Fenêtre
        
        self.__wind=Tk()
        self.__wind.geometry('1280x655')
        self.__wind.title('Space Invaders')
       
        #Check for new game
        self.__restart=False
        

        #Lancer le jeu
        self.start_window()
        

    def  start_game(self):
        #Nouvelle partie
        self.__restart=True

        self.__canvas=Canvas(self.__wind,bg="black", width=self.__width, height=self.__height)

        scriptDir = os.path.dirname(__file__)
        imgpath = os.path.join(scriptDir, '../Assets/background.jpg')

        img= Image.open(imgpath)
        resized_image= img.resize((self.__width,self.__height), Image.ANTIALIAS)
        self.__canvas_img = ImageTk.PhotoImage(resized_image)
        self.canvas_img_rect=self.__canvas.create_image(0,0, image=self.__canvas_img, anchor = "nw")

        self.__canvas.grid(column=0, row=1, sticky="w")

        
        
        #Joueur
        self.__player = Player(int(self.__width/2),self.__height-50,20,50,50,self.__canvas,self.__wind)

        #Protection
        self.__protection=Protection(self.__canvas,self.__wind)

        #Aliens
        self.__blockAlien=Aliens_block(self.__canvas,self.__wind,self.__player,self.score)

        #Special Alien
        self.__specialAlien=AlienSpecial(self.__canvas,self.__wind,0,0)
        self.__specialSpawnTime=20000
        self.__spawn=False

        #Projectile
        self.__fireRate=600
        self.__wait=0

        self.__protection.place_protection()

        self.__blockAlien.create_bloc()
        self.__blockAlien.move_bloc()
        

        self.special_spawn()
 

        self.__player.place_player()

        

        self.__canvas.focus_set()
        self.__canvas.bind('<Key>',self.keyboard)

        self.projectile_wait()

        self.alien_fire()


        self.__restart=False


        



        
       



    def start_window(self):
        wind=self.__wind
    
        self.score = StringVar()
        self.score.set('Score: 0')


        scoreLabel = Label(wind, textvariable=self.score)
        livesLabel = Label(wind, text="Lives: 3")
        quitButton = Button(wind, text="Quit game", command=wind.destroy)
        newGameButton = Button(wind, text="New game", command=self.start_game)
        

        wind.columnconfigure(0, weight=1)
        wind.columnconfigure(1, weight=1)

        wind.rowconfigure(1, minsize=500)

        scoreLabel.grid(column=0, row=0, sticky="W")
        livesLabel.grid(column=0, row=0, sticky="E")
        newGameButton.grid(column=1, row=0, sticky="s")
        quitButton.grid(column=1, row=1, sticky='n')
        
        
        wind.mainloop()
       
    
        
     #Fonction qui impose une pause entre chaque tir du joueur   
    def projectile_wait(self):
        if self.__wait!=0:
            self.__wait=0
        projectileWaitAfter=self.__wind.after(self.__fireRate,self.projectile_wait)
        #if self.__restart==True:
            #self.__wind.after_cancel(projectileWaitAfter)

        
    

    def keyboard(self,event):
        (x0,y0)=self.__canvas.coords(self.__player.rect)
        key=event.keysym
        if key=='d' and x0+self.__player.width+self.__player.dx<self.__width:
            self.__player.moveRight(self.__canvas)

        if key=='q' and x0-self.__player.dx>0:
            self.__player.moveLeft(self.__canvas)   
        if key=='f' and self.__wait==0:
            self.__wait=1
            projectilePlayer=Projectile(self.__canvas,self.__wind,self.__player,self.canvas_img_rect,self.__blockAlien,"player",self.__player)
            projectilePlayer.place_projectile()
            projectilePlayer.fire_projectile()
            
    def alien_fire(self):
        
        time=randint(800,1250)
        row=randint(0,len(self.__blockAlien.aliens)-1)
        column=randint(0,len(self.__blockAlien.aliens[row])-1)
        projectileAlien=Projectile(self.__canvas,self.__wind,self.__blockAlien.aliens[row][column],self.canvas_img_rect,self.__blockAlien,"alien",self.__player)
        projectileAlien.place_projectile()
        projectileAlien.fire_projectile()
        alienFireAfter=self.__wind.after(time,self.alien_fire)
        #if self.__restart==True:
            #self.__wind.after_cancel(alienFireAfter)

    def special_spawn(self):
        
        if self.__spawn==True:
            self.__specialAlien.place_special()
            self.__spawn=False
        elif self.__specialAlien.rect not in self.__canvas.find_all():
            self.__spawn=True
        specialSpawnAfter=self.__wind.after(self.__specialSpawnTime,self.special_spawn)
        #if self.__restart==True:
            #self.__wind.after_cancel(specialSpawnAfter)