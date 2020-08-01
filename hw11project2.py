#! /usr/bin/python
# Exercise No.   2
# File Name:     hw11project2.py
# Programmer:    Mika Okamoto
# Date:          July 26 2020
#
# Problem Statement: Write a program that displays a given card suit with input.
#
# Overall Plan:
# 1. Import Button class and set up GraphWin and such.
# 2. Loop until the button is clicked.
# 3. Take the input given and find the correct file name or display wrong input (if wrong input loop this step and last step again.)
# 4. Display the suit given.
# 5. Wait for a click to close.

from graphics import *
from button import Button

win = GraphWin('Cards', 600, 800)

button = Button(win, Point(300, 700), 150, 100, 'Display')

Text(Point(300, 50), 'Displaying Cards').draw(win)
inp = Entry(Point(300,120), 20)
inp.setText("Suit")
inp.draw(win)

rect = Rectangle(Point(100, 160), Point(500, 600))
rect.draw(win)

button.activate()

while not button.clicked(win.getMouse()):
    continue

s = inp.getText().lower()
if s == 'spade' or s == 'club' or s == 'diamond' or s == 'heart':
    img = Image(Point(300,400), s + ".gif")
    img.draw(win)
    print(img.getHeight(), img.getWidth())
else:
    inp.setText('Retry, Wrong Input')
    while not button.clicked(win.getMouse()):
        continue
    s = inp.getText().lower()
    if s == 'spade' or s == 'club' or s == 'diamond' or s == 'heart':
        img = Image(Point(300,400), s + ".gif")
        img.draw(win)
    else:
        inp.setText('Retry, Wrong Input')

win.getMouse()