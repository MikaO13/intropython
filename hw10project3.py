#! /usr/bin/python
# Exercise No.   3
# File Name:     hw10project3.py
# Programmer:    Mika Okamoto
# Date:          July 26 2020
#
# Problem Statement: Write a program that modifies hw10project1.py to use the Circular Button class (CButton)
#
# Overall Plan:
# 1. Import CButton and graphics.
# 2. Creates the graphwin, buttons, text, and so on.
# 3. Loops (checking if button is clicked) until the button is clicked.
# 4. Takes the inputs and calculates the height of female child from the parent's heights.
# 5. Prints out the height of the child and waits for a click to close the program.

from graphics import *
from cbutton import CButton

win = GraphWin('Project 3', 400, 200)
button = CButton(win, Point(200, 150), 35, 'Calculate')

Text(Point(150, 30), "Enter father's height in inches").draw(win)
Text(Point(150, 70), "Enter mother's height in inches").draw(win)

input1 = Entry(Point(300,30), 5)
input1.setText("0.0")
input1.draw(win)
input2 = Entry(Point(300,70), 5)
input2.setText("0.0")
input2.draw(win)

button.activate()

while not button.clicked(win.getMouse()):
    continue

button.deactivate()

n1 = eval(input1.getText())
n2 = eval(input2.getText())

inches = round(((n1*12/13)+n2)/2)

Text(Point(200, 105), 'The female child is ' + str(inches) + ' inches tall.').draw(win)

win.getMouse()
