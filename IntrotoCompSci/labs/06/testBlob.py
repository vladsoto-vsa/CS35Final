"""
Program: testBlob.py

This program is used to debug the functions within blobillism.py
"""

from blobillism import *
def main():
    win = GraphWin("masterpiece", 500, 500)
    win.setCoords(0,0,500,500)
    PointX = 25
    PointY = 250
    for i in range(10):
        makeCircle(win,Point(PointX,PointY), 25, "green")
        PointX= PointX + 50


    plusButton = makeTextButton(win,252,59,375,83,"size +")
    minButton = makeTextButton(win,252,29,375,57,"size -")
    quitButton = makeTextButton(win,252,0,375,27,"quit")


    #testingButton = makeTextButton(win,0,0,500,50,"testing")
    blueButton = makeColorButton(win,85,0,168,83,"blue")
    redButton = makeColorButton(win,0,0,83,83,"red")
    greenButton = makeColorButton(win,170,0,250,83,"green")
    showButton = makeColorButton(win,377,0,500,83,"white")
    color = "blue"
    showCircle = makeCircle(win,)


    done = False
    while not done:
        point = win.getMouse()
        if clickInButton(point,blueButton) == True:
            print("blue pressed")
        elif clickInButton(point,redButton) == True:
            print("testing pressed")
        elif clickInButton(point,greenButton) == True:
            print("testing pressed")
        elif clickInButton(point,quitButton) == True:
            print("quit pressed")
            done = True
        else:
            print("clicked somwhere else...")


    point = win.getMouse()



main()
