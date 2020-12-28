from main import Berry

def test_random():
    myBerry= Berry()
    myBerry.randomCoordinates()
    x1Berry= myBerry.getX()
    y1Berry= myBerry.getY()
    myBerry.randomCoordinates()
    x2Berry= myBerry.getX()
    y2Berry= myBerry.getY()

    assert x1Berry!= x2Berry and y1Berry!=y2Berry
