import random

class Berry:
    def __init__(self):
        self.x=12
        self.y=17

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
        self.x=15
        self.y=15
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def sayCoordinates(self):
        print("Snake   X: "+str(self.getX())+ ", Y: "+str(self.getY()))
    
    def Left(self):
        self.x= self.x-1

    def Right(self):
        self.x= self.x+1
    def Up(self):
        self.y= self.y-1

    def Down(self):
        self.y= self.y+1
        
    
    
    def AI(self,Xberry,Yberry):
        
        while not(self.getX()== Xberry and self.getY()==Yberry):
            if self.getX()>Xberry:
                self.Left()

            if self.getX()<Xberry:
                self.Right()

            if self.getY()>Yberry:
                self.Up()

            if self.getY()<Yberry:
                self.Down()
            

    



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
mySnake.AI(myBerry.getX(), myBerry.getY())

mySnake.sayCoordinates()


