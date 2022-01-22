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
        


