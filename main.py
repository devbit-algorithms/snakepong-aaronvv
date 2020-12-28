import random
import msvcrt
import time

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

#berry object
myBerry= Berry()

#random berry coordinates
myBerry.randomCoordinates()
myBerry.sayCoordinates()

#snake object
mySnake= Snake()

#snake algorithm to go to berry
mySnake.sayCoordinates()
#mySnake.AI(myBerry.getX(), myBerry.getY())

#mySnake.sayCoordinates()
AI=True
gameOver=False
key="d"
points=0
print("z=up, s= down, q=left, d= right, x= quit")
while gameOver==False:
    if AI==True:
        mySnake.AI(myBerry.getX(), myBerry.getY())
    if msvcrt.kbhit():
           key = msvcrt.getch()
    
    if key=="z" and AI==False:
        mySnake.Up()
    if key=="s" and AI==False:
        mySnake.Down()
    if key=="q" and AI==False:
        mySnake.Left()
    if key=="d" and AI==False:
        mySnake.Right()
    if key=="x":
        gameOver=True

    if myBerry.getX()==mySnake.getX() and mySnake.getY()==myBerry.getY():
        points=points+1
        myBerry.randomCoordinates()
    myBerry.sayCoordinates()
    mySnake.sayCoordinates()
    
    print("Points: "+str(points))
    time.sleep(1)

