import random

class Berry:
    def __init__(self):
        self.x=0
        self.y=0

    #random position berry
    def randomCoordinates(self):
        self.x= random.randint(0, 20)
        self.y= random.randint(0, 20)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def sayCoordinates(self):
        print("X: "+str(self.getX())+ ", Y: "+str(self.getY()))

#create berry object
myBerry= Berry()

#call methods on the berry object
myBerry.randomCoordinates()
myBerry.sayCoordinates()

