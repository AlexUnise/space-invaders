class Protection:
    def __init__(self,canvas,wind):
        self.__canvas=canvas
        self.__wind=wind
        self.__width=10
        self.__height=5
        self.__numberOfProtections=3
        self.__protectionDistancex=150
        self.__protectionDistancey=250
        self.__cubeSize=20
        self.__listProtections=[]
        self.__positionx=int(int(self.__canvas.cget('width'))-((self.__numberOfProtections*self.__width*self.__cubeSize)+((self.__numberOfProtections-1)*self.__protectionDistancex)))/2
        self.__positiony=int(self.__canvas.cget('height'))-self.__protectionDistancey
    

    def place_protection(self):
        placementProtection=0
        for columns in range(0,self.__numberOfProtections):

            blocProtection=[]
            placementy=0

            for rows in range(0,self.__height):
                ligneProtection=[]
                placementx=0
                
                for columns in range(0,self.__width):
                    
                    protectionSquare=self.__canvas.create_rectangle(self.__positionx + placementx + placementProtection,self.__positiony + placementy,self.__positionx + placementx + self.__cubeSize + placementProtection,self.__positiony + placementy + self.__cubeSize,fill="grey")
                    placementx+=self.__cubeSize+1
                    ligneProtection.append(protectionSquare)

                blocProtection.append(ligneProtection)
                placementy+=self.__cubeSize+1

            self.__listProtections.append(blocProtection)
            placementProtection+=self.__protectionDistancex+(self.__width*self.__cubeSize)
        