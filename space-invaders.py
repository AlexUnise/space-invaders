#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Createurs: OUENADIO Alexandre, MICHALOPOULOS Zaphirios
Groupe: C
Description du fichier: Programme principale.

"""

import lib_space_invaders as SpaceInv
from tkinter import Tk, Label, Button, Canvas, PhotoImage
from PIL import Image,ImageTk

#Initialisation de la fenetre de jeu
wind = Tk()

wind.geometry('1280x655')
wind.title('Space Invaders')
Jeu=SpaceInv.Space_Invaders(wind)


#backgroundImage = PhotoImage(file="background.gif")

#Load an image in the script
img= Image.open("background.jpg")


#Resize the Image using resize method



# resized_image= img.resize((Jeu.__width,Jeu.__height), Image.ANTIALIAS)
# backgroundImage= ImageTk.PhotoImage(resized_image)
# Jeu.__canvas.create_image(0,0, image=backgroundImage, anchor = "nw")
# Jeu.__canvas.grid(column=0, row=1, sticky="w")

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

Jeu.place_aliens()
Jeu.move_alien()

wind.mainloop()

