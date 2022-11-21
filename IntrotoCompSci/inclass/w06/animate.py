from facesLibrary import*
from graphics import *

def main():
    win = GraphWin("animate a face!", 500, 500)
    win.setCoords(0, 0, 500, 500)

    msg = Text(Point(250,480), "click to make a face")
    msg.draw(win)

    point = win.getMouse()
    face = drawFace(win, point, 50)
    steps = 50
    while True:
        msg.setText("click to move face to new location")
        newPoint = win.getMouse()
        dx = newPoint.getX() - point.getX()
        dy = newPoint.getY() - point.getY()
        animateObjects(face,dx,dy, steps)
        point = newPoint

    win.getMouse()
main()
