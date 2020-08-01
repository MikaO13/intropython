#! /usr/bin/python
# Exercise No.   3
# File Name:     hw4project3.py
# Programmer:    Mika Okamoto
# Date:          June 27 2020
#
# Problem Statement: Allow a user to draw a line segment then display some graphical and texual information about the line segment. 
#
# Overall Plan:
# 1. Open a GraphWin. 
# 2. Take two points as inputs.
# 3. Calculate the midpoint and save as a variable. 
# 4. Calculate the length and slope of the line and save as variables. 
# 5. Draw the line. 
# 6. Draw the midpoint in cyan. 
# 5. Print the length and the slope of the line. 

from graphics import *
import time
import math

win = GraphWin("Project 3")

text = Text(Point(5, 1), "Click on two points!")
p1 = win.getMouse()
p2 = win.getMouse()

line = Line(p1, p2)
mid = Point((p1.getX()+p2.getX())/2, (p1.getY()+p2.getY())/2)

dx = p2.getX()-p1.getX()
dy = p2.getY()-p1.getY()
slope = dy/dx
length = math.sqrt(dx**2 + dy**2)

line.draw(win)
mid.draw(win)
mid.setFill('cyan')

print("The length is", length)
print("The slope is", slope)

time.sleep(10)