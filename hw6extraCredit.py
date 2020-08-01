#! /usr/bin/python
# Exercise No.   1
# File Name:     hw6project1.py
# Programmer:    Mika Okamoto
# Date:          July 5 2020
#
# Problem Statement: Write definitions for these functions: sphereArea(radius) and sphereVolume(radius)
#
# Overall Plan:
# 1. Import math modules.
# 2. Define the functions.
# 3. Return the formulas. 
# 4. Test the functions.

from graphics import *

win = GraphWin()
circ = Circle(win.getMouse(), 5)
circ.draw(win)

def moveTo(shape, newCenter):
    shape.setOutline('white')
    newcirc = Circle(newCenter, shape.getRadius())
    return newcirc

for i in range(9):
    circ = moveTo(circ, win.getMouse())
    circ.draw(win)