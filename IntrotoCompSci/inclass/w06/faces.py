from facesLibrary import *
from graphics import *
from random import randrange


def main():
    win = GraphWin("drawing faces", 500, 500)
    win.setCoords(0, 0, 500, 500)

    msg = Text(Point(250,450), "Click anywhere to make a face")
    msg.draw(win)

    while True:
        point = win.getMouse()
        drawFace(win, point, randrange(5,50))
        msg.setText("click again, foo!")


    drawFace(win, Point(250,250), 100)



main()
