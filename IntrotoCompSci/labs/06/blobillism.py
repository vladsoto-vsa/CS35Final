"""
Program: blobillism.py

A library of functions for use in a blob drawing application.
"""
from graphics import *


def makeCircle(window, centerPt, radius, color):
    """
    Parameters:
        window -- the window where the circle is drawn
        centerPt -- center coordinates of the circle
        radius -- radius of the circle
        color -- color of the circle
    Returns:
        Returns the the drawing of the circle
    Side Effects:
        None
    """

    circulo = Circle(centerPt, radius)
    circulo.setFill(color)
    circulo.draw(window)
    centerX = centerPt.getX()
    centerY = centerPt.getY()
    return circulo


def makeTextButton(window, XCoordLL, YCoordLL, XCoordUR, YCoordUR, Word):
    """
    Parameters:
        window -- the window where the circle is drawn
        XCoordLL -- lower left x coordinate of button
        YCoordLL -- lower left y coordinate of button
        XCoordUR -- upper right x coordinate of button
        YCoordUR -- upper right y coordinate of button
        Word -- text displayed in center of button
    Returns:
        Returns a button, or rectangle, with text in its center
    Side Effects:

    """
    LL = Point(XCoordLL, YCoordLL)
    UR = Point(XCoordUR, YCoordUR)
    button = Rectangle(LL,UR)
    button.setFill("black")
    button.draw(window)
    center = button.getCenter()
    word = Text(center, Word)
    word.setTextColor("white")
    word.draw(window)
    return button

def makeColorButton(window,XCoordLL,YCoordLL,XCoordUR,YCoordUR, color):
    """
    Parameters:
        window -- the window where the circle is drawn
        XCoordLL -- lower left x coordinate of button
        YCoordLL -- lower left y coordinate of button
        XCoordUR -- upper right x coordinate of button
        YCoordUR -- upper right y coordinate of button
        color -- color that fills the button
    Returns:
        Returns a button, or rectangle, filled with a color
    """
    LL = Point(XCoordLL, YCoordLL)
    UR = Point(XCoordUR, YCoordUR)
    button = Rectangle(LL,UR)
    button.setFill(color)
    button.draw(window)
    return button

def clickInButton(point,rectangle):
    """
    Parameters:
        point -- point where the user clicks
        rectangle -- used to sense if point is within coordinates of rectangle
    Returns:
        Returns whether or not the user clicked within the
        control section

    """

    XPoint = point.getX()
    YPoint = point.getY()
    LLRect = rectangle.getP1()
    URRect = rectangle.getP2()
    LLX = LLRect.getX()
    LLY = LLRect.getY()
    URX = URRect.getX()
    URY = URRect.getY()

    if XPoint > LLX and XPoint < URX and YPoint > LLY and YPoint < URY:
        return True
    else:
        return False
