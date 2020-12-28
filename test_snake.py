from main import Berry
from main import Snake



def test_BerryRandom():
    myBerry= Berry()
    myBerry.randomCoordinates()
    x1Berry= myBerry.getX()
    y1Berry= myBerry.getY()
    myBerry.randomCoordinates()
    x2Berry= myBerry.getX()
    y2Berry= myBerry.getY()
    myBerry.randomCoordinates()
    x3Berry= myBerry.getX()
    y3Berry= myBerry.getY()

    assert not(x1Berry== x2Berry==x3Berry and y1Berry==y2Berry==y3Berry) 

def test_SnakeMove():
    mySnake= Snake()
    x1Snake=mySnake.getX()
    y1Snake=mySnake.getY()
    mySnake.Up()
    x2Snake=mySnake.getX()
    y2Snake=mySnake.getY()

    assert x2Snake==x1Snake and y1Snake-1==y2Snake

    mySnake.Down()
    x3Snake=mySnake.getX()
    y3Snake=mySnake.getY()

    assert x3Snake==x2Snake and y2Snake+1==y3Snake 

    mySnake.Left()
    x4Snake=mySnake.getX()
    y4Snake=mySnake.getY()

    assert x3Snake-1==x4Snake and y4Snake==y3Snake

    mySnake.Right()
    x5Snake=mySnake.getX()
    y5Snake=mySnake.getY()

    assert x4Snake+1 ==x5Snake and y5Snake==y4Snake

def test_AI():
    myBerry= Berry()
    myBerry.randomCoordinates()
    
    mySnake= Snake()
    xSnake=mySnake.getX()
    ySnake=mySnake.getY()
    xBerry= myBerry.getX()
    yBerry= myBerry.getY()

    mySnake.AI(myBerry.getX(), myBerry.getY())
    
    xAISnake=mySnake.getX()
    yAISnake=mySnake.getY()
    

    assert abs(xBerry-xSnake)>abs(xBerry-xAISnake) or abs(yBerry-ySnake)>abs(yBerry-yAISnake)