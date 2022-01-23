#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:34:13 2022

@author: z.michalopoulos
"""
from tkinter import Tk, Label, Button, Canvas, PhotoImage
from PIL import Image,ImageTk


size=50
x=0
y=0
dx=10

sizep=50
xp=0
yp=int(1406/2.25)
dxp=20

sizexl=10
sizeyl=20
xl=xp+int(sizep/2)-int(sizexl/2)
yl=int(1406/2.25)-sizep
dyl=10
listeProjectile=[]

wind = Tk()

wind.geometry('1280x655')
wind.title('Space Invaders')




#backgroundImage = PhotoImage(file="background.gif")

#Load an image in the script
img= Image.open("background.jpg")

#Resize the Image using resize method


canvas = Canvas(wind,bg="white", width=int(2500/2.25), height=int(1406/2.25))
resized_image= img.resize((int(2500/2.25),int(1406/2.25)), Image.ANTIALIAS)
backgroundImage= ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, image=backgroundImage, anchor = "nw")
canvas.grid(column=0, row=1, sticky="w")
Alien=canvas.create_rectangle(x,y,x+size,y+size,fill="red")
Joueur=canvas.create_rectangle(xp,yp-sizep,xp+sizep,yp,fill="blue")



def move_alien():
    global size,x,y,dx
    if x+size+dx>int(2500/2.25):
        dx=-dx
    if x+dx<0:
        dx=-dx
    
    x+=dx
    canvas.coords(Alien,x,y,x+size,y+size)
    wind.after(20,move_alien)

def keyboard(event):
    global xp,yp,sizep,dxp,listeProjectile
    key=event.keysym
    if key=='d' and xp+sizep+dxp<int(2500/2.25):
        xp+=dxp

    if key=='q' and xp-dxp>0:
        xp-=dxp
    canvas.coords(Joueur,xp,yp-sizep,xp+sizep,yp)     
    if key=='f':
        yl=int(1406/2.25)-sizep
        listeProjectile.append(canvas.create_rectangle(xp,yl,xp+sizexl,yl-sizeyl,fill="green"))
        projectile()
        
def projectile():
    global xl,yl,sizexl,sizeyl,dyl,listeProjectile
    print(listeProjectile)
    if yl-sizeyl-dyl>0:
        yl-=dyl
        canvas.coords(listeProjectile[0],xl,yl,xl+sizexl,yl-sizeyl)
        wind.after(20,projectile)
    else:
        canvas.delete(listeProjectile[0])
        listeProjectile.pop(0)
    
    
canvas.focus_set()
canvas.bind('<Key>',keyboard)



scoreLabel = Label(wind, text="Score: 0")
livesLabel = Label(wind, text="Lives: 3")
quitButton = Button(wind, text="Quit game", command=wind.destroy)
newGameButton = Button(wind, text="New game",command=move_alien)

wind.columnconfigure(0, weight=1)
wind.columnconfigure(1, weight=1)

wind.rowconfigure(1, minsize=500)

scoreLabel.grid(column=0, row=0, sticky="W")
livesLabel.grid(column=0, row=0, sticky="E")
newGameButton.grid(column=1, row=0, sticky="s")
quitButton.grid(column=1, row=1, sticky='n')
print(canvas.cget('height'))


wind.mainloop()


