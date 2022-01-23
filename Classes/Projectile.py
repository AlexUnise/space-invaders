
class Projectile:
    def __init__(self,canvas,wind,entity,backImg,blockAlien,shooter,player):
        self.__height=10
        self.__width=4
        self.__dy=20
        self.__canvas=canvas
        self.__wind=wind
        self.__entity=entity
        self.__backImg=backImg
        self.__blockAlien=blockAlien
        self.__player=player
        self.__origin=shooter

    def place_projectile(self):
        (x0,y0)=self.__canvas.coords(self.__entity.rect)
        if self.__origin=="player":
            color="yellow"
        elif self.__origin=="alien":
            color="red"
        self.projectile=self.__canvas.create_rectangle(x0+int(self.__entity.width/2),y0-5,x0+int(self.__entity.width/2)+self.__width,y0-5-self.__height,fill=color)
        
    
    def fire_projectile(self):
        (x_proj0,y_proj0,x_proj1,y_proj1)=self.__canvas.coords(self.projectile)
        liste_objet=self.__canvas.find_overlapping(x_proj0,y_proj0,x_proj1,y_proj1)
        
        if len(liste_objet)>2:
            
            for objet in liste_objet:
                if objet!=self.__backImg and objet!=self.projectile and self.__origin=="player":
                    self.__blockAlien.add_aliens_hit(objet)
                    self.__canvas.delete(self.projectile)

                elif objet!=self.__backImg and objet!=self.projectile and self.__origin=="alien":
                     
                    if objet==self.__player.rect:
                        self.__player.player_hit()
                        self.__canvas.delete(self.projectile)   
                    else:
                        if y_proj1>int(self.__canvas.cget('height'))-250:
                            self.__canvas.delete(self.projectile)  
                            self.__canvas.delete(objet)
     


        if y_proj0<0 or y_proj1>int(self.__canvas.cget('height')):
            self.__canvas.delete(self.projectile)



        if self.projectile in self.__canvas.find_all():
            if self.__origin=="player":
                self.__canvas.move(self.projectile,0,-self.__dy)
            elif self.__origin=="alien":
                self.__canvas.move(self.projectile,0,self.__dy) 
            self.__wind.after(20,self.fire_projectile)