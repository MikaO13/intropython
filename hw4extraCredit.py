#! /usr/bin/python
# Exercise No.   4
# File Name:     hw4extraCredit.py
# Programmer:    Mika Okamoto
# Date:          June 28 2020
#
# Problem Statement: You are to write a progam that allows the user to draw a simple house using five mouse clicks. 
#
# Overall Plan:
# 1. Open a GraphWin. 
# 2. Take two points as the inputs for the frame of the house and draw the rectangle.
# 3. Calculate the bottom, top, left, and right values for the house for use later.
# 4. Take the third point as input and calculate to draw the door.
# 5. Take the fourth point as input and calculate to draw the window. 
# 6. Take the fifth point as input and calculate to draw the roof. 
# 7. Wait for a click to close the window. 

from graphics import *

def main():
    win = GraphWin("Five Click House") 

    p1 = win.getMouse()
    p2 = win.getMouse()

    frame = Rectangle(p1, p2)
    frame.draw(win)

    bottomY, topY = max(p1.getY(), p2.getY()), min(p1.getY(), p2.getY())
    leftX, rightX = min(p1.getX(), p2.getX()), max(p1.getX(), p2.getX())
    length = rightX-leftX

    p3 = win.getMouse()

    door = Rectangle(Point(p3.getX()+length/10, p3.getY()), Point(p3.getX()-length/10, bottomY))
    door.draw(win)

    p4 = win.getMouse()

    window = Rectangle(Point(p4.getX()+length/20, p4.getY()+length/20), Point(p4.getX()-length/20, p4.getY()-length/20))
    window.draw(win)

    p5 = win.getMouse()
    Line(p5, Point(leftX, topY)).draw(win)
    Line(p5, Point(rightX, topY)).draw(win)


    win.getMouse()

main()