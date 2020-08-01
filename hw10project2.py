#! /usr/bin/python
# Exercise No.   2
# File Name:     hw10project2.py
# Programmer:    Mika Okamoto
# Date:          July 26 2020
#
# Problem Statement: Create a modified circular button class and use it in implenting the roller.py program.
#
# Overall Plan:
# 1. Create and define CButton class (in another file), and import necessary things.
# 2. Create the GraphWin and other things on it.
# 3. Loops until the quit button is clicked.
# 4. Inside of that loop check if the roll button is clicked, and if it is roll two dice and display them

from graphics import GraphWin, Point
from cbutton import CButton
from random import randrange
from dieview import DieView

win = GraphWin('Dice Roller')
win.setCoords(0, 0, 10, 10)
win.setBackground('green2')

die1 = DieView(win, Point(3, 7), 2)
die2 = DieView(win, Point(7, 7), 2)
rollButton = CButton(win, Point(5, 4.5), 1.2, 'Roll')
rollButton.activate()
quitButton = CButton(win, Point(5, 1), 1, 'Quit')

pt = win.getMouse()
while not quitButton.clicked(pt):
    if rollButton.clicked(pt):
        value1 = randrange(1, 7)
        die1.setValue(value1)
        value2 = randrange(1, 7)
        die2.setValue(value2)
        quitButton.activate()
    pt = win.getMouse()

win.close()