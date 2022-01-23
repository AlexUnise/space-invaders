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


#Classe principale contenant le jeu 
class Space_Invaders:
    def __init__(self):
        self.__width=int(2500/2.25)
        self.__height=int(1406/2.25)
        
        #Fenêtre
        
        self.__wind=Tk()
        self.__wind.geometry('1280x655')
        self.__wind.title('Space Invaders')
       
        #Check for new game
        self.__afterFunctions=[]
        

        #Lancer le jeu
        self.start_window()


    #Fonction permettant de lancer, ainsi que de relancer la partie
    def  start_game(self):
        #Nouvelle partie
        if self.__afterFunctions!=[]:
            for afterFunction in self.__afterFunctions:
                self.__wind.after_cancel(afterFunction)

        self.__canvas=Canvas(self.__wind,bg="black", width=self.__width, height=self.__height)

        scriptDir = os.path.dirname(__file__)
        imgpath = os.path.join(scriptDir, '../Assets/background.jpg')

        img= Image.open(imgpath)
        resized_image= img.resize((self.__width,self.__height), Image.ANTIALIAS)
        self.__canvas_img = ImageTk.PhotoImage(resized_image)
        self.canvas_img_rect=self.__canvas.create_image(0,0, image=self.__canvas_img, anchor = "nw")

        self.__canvas.grid(column=0, row=1, sticky="w")

        
        
        #Joueur
        self.__player = Player(int(self.__width/2),self.__height-50,20,50,50,self.lives,self.__canvas,self.__wind)
        #On met le score a 0
        self.__player.score=0
        self.score.set('Score: ' + str(self.__player.score))
        #On met les vies du joueur a 3
        self.__player.lives=3
        self.lives.set('Lives: ' + str(self.__player.lives) )
        #Protection
        self.__protection=Protection(self.__canvas,self.__wind)

        #Aliens
        self.__blockAlien=Aliens_block(self.__canvas,self.__wind,self.__player,self.score)

        #Special Alien
        self.__specialAlien=AlienSpecial(self.__canvas,self.__wind,0,0)
        self.__specialSpawnTime=20000
        self.__spawn=False

        #Vitesse de tir du projectile du joueuer
        self.__fireRate=600
        self.__wait=0
        #On place les protections
        self.__protection.place_protection()
        #On place les ennemis
        self.__blockAlien.create_bloc()
        #on fait bouger les ennemis
        self.__blockAlien.move_bloc()
        #On fait apparaitre un ennemi special
        self.special_spawn()
        #On place le joueur
        self.__player.place_player()

        
        #On detecte les touches appuyees
        self.__canvas.focus_set()
        self.__keyboard_event_id = self.__canvas.bind('<Key>',self.keyboard)
        self.__player.set_keyboard_id(self.__keyboard_event_id)
        #On lance un compteur pour limiter le nombre de tir du joueur
        self.projectile_wait()

        #Les aliens commencent a tirer aleatoirement
        self.alien_fire()




        



        
       


    #Methode qui cree et organise la fenetre 
    def start_window(self):
        wind=self.__wind
    
        #Chaine de caratère qui évolue en fonction du nombre d'aliens tués
        self.score = StringVar()
        self.score.set('Score: 0')
        #Chaine de caratère qui évolue en fonction du nombre de fois que le joueur est touché
        self.lives = StringVar()
        self.lives.set('Lives: 3')

        scoreLabel = Label(wind, textvariable=self.score)
        livesLabel = Label(wind, textvariable=self.lives)
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
       
    
        
     #Methode qui impose une pause entre chaque tir du joueur   
    def projectile_wait(self):
        if self.__wait!=0:
            self.__wait=0
        projectileWaitAfter=self.__wind.after(self.__fireRate,self.projectile_wait)
        self.__afterFunctions.append(projectileWaitAfter)

        
    
    #Methode qui recoit en entree les touches appuyees par l'utilisateur et qui effectue l'action correspondante a cette touche
    def keyboard(self,event):
        (x0,y0)=self.__canvas.coords(self.__player.rect)
        key=event.keysym
        if key=='d' and x0+int(self.__player.width/2)+self.__player.dx<self.__width:
            self.__player.moveRight(self.__canvas)

        if key=='q' and x0-int(self.__player.width/2)-self.__player.dx>0:
            self.__player.moveLeft(self.__canvas)   
        if key=='space' and self.__wait==0:
            self.__wait=1
            projectilePlayer=Projectile(self.__canvas,self.__wind,self.__player,self.canvas_img_rect,self.__blockAlien,"player",self.__player,self.__specialAlien)
            projectilePlayer.place_projectile()
            projectilePlayer.fire_projectile()

    #Methode qui determine aleatoirement quand et quel alien va tirer          
    def alien_fire(self):
        
        time=randint(600,1000)
        row=randint(0,len(self.__blockAlien.aliens)-1)
        column=randint(0,len(self.__blockAlien.aliens[row])-1)
        projectileAlien=Projectile(self.__canvas,self.__wind,self.__blockAlien.aliens[row][column],self.canvas_img_rect,self.__blockAlien,"alien",self.__player,self.__specialAlien)
        projectileAlien.place_projectile()
        projectileAlien.fire_projectile()
        alienFireAfter=self.__wind.after(time,self.alien_fire)
        self.__afterFunctions.append(alienFireAfter)

    #Methode qui fait apparaitre l'ennemi special
    def special_spawn(self):
        
        if self.__spawn==True:
            self.__specialAlien.place_special()
            self.__spawn=False
        elif self.__specialAlien.rect not in self.__canvas.find_all():
            self.__spawn=True
        specialSpawnAfter=self.__wind.after(self.__specialSpawnTime,self.special_spawn)
        self.__afterFunctions.append(specialSpawnAfter)