from graphics import *
from random import randrange
from time import sleep


def drawFace(window,centerPt,radius):
    """
    Parameters:
    window is a GraphWin object where we will draw the face
    centerPt is a Point Object where face should be centered
    radius is an integer specifies radius of the case
    Returns:
    The list of objects that make up the face
    """
    head = Circle(centerPt, radius)
    color = color_rgb(randrange(256),randrange(256),randrange(256))
    head.setFill(color)
    head.draw(window)
    centerX = centerPt.getX()
    centerY = centerPt.getY()
    LeyeCenter = Point(centerX-radius/3, centerY+radius/3)
    Leye = Circle(LeyeCenter, radius/5)
    Leye.setFill("black")
    Leye.draw(window)
    Reye = Leye.clone()
    Reye.move(radius*2/3,0)
    Reye.draw(window)

    mouth = Line(Point(centerX-radius/2, centerY-radius/2), Point(centerX+radius/2, centerY-radius/2))
    mouth.setOutline("red")
    mouth.setWidth(6)
    mouth.draw(window)
    return[head,Leye,Reye,mouth]



def animateObjects(listOfObjects, max_dx, max_dy, steps):
    """
    Parameters:
    window is a GraphWin objects
    listOfObjects is a list of graphics objects to move
    max_dx Integer for amount to move in x direction
    max_dy integer for amount to move in Y direction
    steps integer for how many moves to make
    Returns:
    None, called to move objects
    """
    dx = max_dx/steps
    dy = max_dy/steps

    for j in range(steps):
        for i in range(len(listOfObjects)):
            listOfObjects[i].move(dx, dy)
        sleep(0.01)
