"""
Name: Vladimir Soto-Avina
Date: March 7, 2020

Program: mainBlob.py

This program uses the functions in blobillism.py to create a drawing
application.
"""

from blobillism import *

def main():
    win = GraphWin("masterpiece", 500, 500)
    win.setCoords(0,0,500,500)



    plusButton = makeTextButton(win,252,59,375,83,"size +")
    minButton = makeTextButton(win,252,29,375,57,"size -")
    quitButton = makeTextButton(win,252,0,375,27,"quit")



    blueButton = makeColorButton(win,85,0,168,83,"blue")
    redButton = makeColorButton(win,0,0,83,83,"red")
    greenButton = makeColorButton(win,170,0,250,83,"green")
    showButton = makeColorButton(win,377,0,500,83,"white")
    color = "red"
    radius = 25
    exampleBlob = makeCircle(win,showButton.getCenter(), radius, color)



    done = False
    while not done:
        point = win.getMouse()

        if clickInButton(point,blueButton) == True:
            exampleBlob.undraw()
            color = "blue"
            exampleBlob = makeCircle(win,showButton.getCenter(), radius, color)
        elif clickInButton(point,redButton) == True:

            exampleBlob.undraw()
            color = "red"
            exampleBlob = makeCircle(win,showButton.getCenter(), radius, color)
        elif clickInButton(point,greenButton) == True:
            exampleBlob.undraw()

            color = "green"
            exampleBlob = makeCircle(win,showButton.getCenter(), radius, color)
        elif clickInButton(point,plusButton) == True:
            if radius < 38:
                exampleBlob.undraw()
                radius = radius + 5
                exampleBlob = makeCircle(win,showButton.getCenter(), radius, color)

        elif clickInButton(point, minButton) == True:
            if radius > 5:
                exampleBlob.undraw()
                radius = radius - 5
                exampleBlob = makeCircle(win,showButton.getCenter(), radius, color)

        elif clickInButton(point,quitButton) == True:
            done = True
        else:
            if point.getY() - radius > 83:
                drawBlob = makeCircle(win,point,radius,color)


main()
