#! /usr/bin/python
# Exercise No.   1
# File Name:     hw10project1.py
# Programmer:    Mika Okamoto
# Date:          July 26 2020
#
# Problem Statement: Write a program that uses the Button class to create a GUI.
#
# Overall Plan:
# 1. Define Button class. 
# 2. Creates the graphwin, buttons, text, and so on.
# 3. Loops (checking if button is clicked) until the button is clicked.
# 4. Takes the inputs and calculates the height of female child from the parent's heights.
# 5. Prints out the height of the child and waits for a click to close the program.

from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        w, h = width/2.0, height/2.0
    
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def clicked(self, p):
        return (self.active and self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax)
    
    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
    
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

win = GraphWin('Project 1', 400, 200)
button = Button(win, Point(200, 150), 75, 25, 'Calculate')

Text(Point(150, 30), "Enter father's height in inches").draw(win)
Text(Point(150, 70), "Enter mother's height in inches").draw(win)

input1 = Entry(Point(300,30), 5)
input1.setText("0.0")
input1.draw(win)
input2 = Entry(Point(300,70), 5)
input2.setText("0.0")
input2.draw(win)

while not button.clicked(win.getMouse()):
    continue

button.deactivate()

n1 = eval(input1.getText())
n2 = eval(input2.getText())

inches = round(((n1*12/13)+n2)/2)

Text(Point(200, 120), 'The female child is ' + str(inches) + ' inches tall.').draw(win)

win.getMouse()
