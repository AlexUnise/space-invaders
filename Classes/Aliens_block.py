from Classes.Alien import Alien

class Aliens_block:
    def __init__(self,canvas,wind):
        self.__height=3
        self.__canvas = canvas
        self.__wind = wind
    
    def create_block(self,number_rows):
        list_aliens = []
        canvas_width = int(self.__canvas.cget('width'))
        canvas_height= int(self.__canvas.cget('height'))
        y = self.__height
        for i in range(number_rows):
            for j in range(11):
                if j == 11:
                    list_aliens.append(Alien(j*60,y,60*j,0,self.__canvas, self.__wind))
                elif j == 0:
                    list_aliens.append(Alien(j*60,y,0,60*(11-j),self.__canvas, self.__wind))
                else:
                    list_aliens.append(Alien(j*60,y,60*j,60*(11-j),self.__canvas, self.__wind))
            y += 60
        return list_aliens

        
    
    