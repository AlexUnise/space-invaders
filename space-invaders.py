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

wind.geometry('1280x720')
wind.title('Space Invaders')

scoreLabel = Label(wind, text="Score: 0")
livesLabel = Label(wind, text="Lives: 3")
quitButton = Button(wind, text="Quit game", command=wind.destroy)
newGameButton = Button(wind, text="New game")


#backgroundImage = PhotoImage(file="background.gif")

#Load an image in the script
img= Image.open("background.jpg")

#Resize the Image using resize method
resized_image= img.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

canvas = Canvas(wind,bg="white")
canvas.create_image(0,0, image=backgroundImage, anchor = "nw")
canvas.grid(column=0, row=1, sticky="NSWE")

wind.columnconfigure(0, weight=3)
wind.columnconfigure(1, weight=1)

scoreLabel.grid(column=0, row=0, sticky="W")
livesLabel.grid(column=0, row=0, sticky="E")
newGameButton.grid(column=1, row=0)
quitButton.grid(column=1, row=1)

wind.mainloop()

