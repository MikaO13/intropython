#! /usr/bin/python
# Exercise No.   1
# File Name:     hw4project1.py
# Programmer:    Mika Okamoto
# Date:          June 27 2020
#
# Problem Statement: Draw a simple picture with at least 3 graphical objects.
#
# Overall Plan:
# 1. Open a GraphWin. 
# 2. Define variables. 
# 3. Draw a circle.
# 4. Draw a rectangle. 
# 5. Draw a oval. 

from graphics import *
import time

def main():
    win = GraphWin("Project 1")

    center = Point(100, 100)
    p1 = Point(50, 25)
    p2 = Point(150, 175)

    circ = Circle(center, 50)
    rect = Rectangle(p1, p2)
    oval = Oval(p1, p2)

    circ.draw(win)
    rect.draw(win)
    oval.draw(win)

    time.sleep(10)

    win.close()

main()