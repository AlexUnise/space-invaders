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

scoreLabel = Label(wind, text="Score: 0")
livesLabel = Label(wind, text="Lives: 3")
quitButton = Button(wind, text="Quit game", command=wind.destroy)
newGameButton = Button(wind, text="New game")


#backgroundImage = PhotoImage(file="background.gif")

#Load an image in the script
img= Image.open("background.jpg")

#Resize the Image using resize method


canvas = Canvas(wind,bg="white", width=int(2500/2.25), height=int(1406/2.25))
resized_image= img.resize((int(2500/2.25),int(1406/2.25)), Image.ANTIALIAS)
backgroundImage= ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, image=backgroundImage, anchor = "nw")
canvas.grid(column=0, row=1, sticky="w")

wind.columnconfigure(0, weight=1)
wind.columnconfigure(1, weight=1)

wind.rowconfigure(1, minsize=500)

scoreLabel.grid(column=0, row=0, sticky="W")
livesLabel.grid(column=0, row=0, sticky="E")
newGameButton.grid(column=1, row=0, sticky="s")
quitButton.grid(column=1, row=1, sticky='n')

wind.mainloop()

