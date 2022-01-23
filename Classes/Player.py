from PIL import Image,ImageTk
import os
#Classe qui gere les differentes informations, etats et mouvements du joueur,
class Player:
    #Classe Joueur
    #Un joueur peut se deplacer uniquement sur l'axe x. Le programmeur definit sa coordonnee y. 
    #dx represente la vitesse de deplacement sur l'axe, definie par le programmeur.

    
    
    def __init__(self,x,y,dx,width,height,life_counter,canvas,wind):
        self.__name=""
        self.lives = 3
        self.score = 0
        self.__positionx = x
        self.__positiony = y
        self.dx = dx
        self.width = width
        self.height = height
        self.__canvas=canvas
        self.__wind=wind
        self.__file=[]
        self.__life_counter = life_counter
        
    #Methode qui place le joueur sur le canvas    
    def place_player(self):
        scriptDir = os.path.dirname(__file__)
        imgpath = os.path.join(scriptDir, '../Assets/space_invaders_player.png')
        img= Image.open(imgpath)
        self.__canvas_img = ImageTk.PhotoImage(img)
        self.rect=self.__canvas.create_image(self.__positionx,self.__positiony, image=self.__canvas_img)  

    #Methode qui permet de déplacer le joueur a gauche sur le canvas.
    def moveLeft(self,canvas):
        canvas.move(self.rect,-self.dx, 0)

    #Methode qui permet de déplacer le joueur a droite sur le canvas.
    def moveRight(self,canvas):
        canvas.move(self.rect,self.dx, 0)

    #Methode qui gere les vies du joueur et l'ecran de defaite
    def player_hit(self):
        self.lives-=1
        self.__life_counter.set('Lives: ' + str(self.lives) )

        if self.lives==0:
            self.game_over(1)
    
    def set_keyboard_id(self,id):
        self.__keyboard_event_id = id


    def game_over(self,resultat):

        if resultat==1:
            texte="Vous avez perdu ! Score: "+str(self.score)
        else:
            texte="L'humanité survit! Score: "+str(self.score)
        #On efface tout dans le canvas
        self.__canvas.delete('all')
        #Affichage du titre gameover 
        self.__canvas.create_text(int(int(self.__canvas.cget('width'))/2),int(int(self.__canvas.cget('height'))/2), text=texte, fill="#fff", font=('Helvetica','30','bold'))
        #On désactive l'écoute des évenements clavier 
        self.__canvas.unbind('<Key>', self.__keyboard_event_id)
        # #On désactive l'exécution de la fonction alien_fire 
        # self.__canvas.after_cancel(self.__alienFireAfter)


    # def set_alienFireAfter(self, id):
    #     self.__alienFireAfter = id