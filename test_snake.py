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

    assert x2Snake==x1Snake-1 and y1Snake==y2Snake

    mySnake.Down()
    x3Snake=mySnake.getX()
    y3Snake=mySnake.getY()

    assert x3Snake==x2Snake+1 and y2Snake==y3Snake 

    mySnake.Left()
    x4Snake=mySnake.getX()
    y4Snake=mySnake.getY()

    assert x3Snake==x4Snake and y4Snake==y3Snake -1

    mySnake.Right()
    x5Snake=mySnake.getX()
    y5Snake=mySnake.getY()

    assert x4Snake==x5Snake and y5Snake==y4Snake +1 
