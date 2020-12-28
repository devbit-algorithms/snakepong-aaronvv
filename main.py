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
        print("Berry   X: "+str(self.getX())+ ", Y: "+str(self.getY()))

class Snake:
    def __init__(self):
        self.x=0
        self.y=0
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def sayCoordinates(self):
        print("Snake   X: "+str(self.getX())+ ", Y: "+str(self.getY()))
    
    def Up(self):
        self.x= self.x-1

    def Down(self):
        self.x= self.x+1
        
    def Left(self):
        self.y= self.y-1

    def Right(self):
        self.y= self.y+1
    



# OUTPUT

#create berry object
myBerry= Berry()

#call methods on the berry object
myBerry.randomCoordinates()
myBerry.sayCoordinates()

#create snake object
mySnake= Snake()

#call methods on the snake object
mySnake.sayCoordinates()
mySnake.Up()
mySnake.sayCoordinates()


