#! /usr/bin/python
# Exercise No.   2
# File Name:     hw4project2.py
# Programmer:    Mika Okamoto
# Date:          June 28 2020
#
# Problem Statement: Create a simple GUI for MyFirstProgram.py using the techniques from the chapter. Your GUI should include both the input of number and the output of the answers.
#
# Overall Plan:
# 1. Open a GraphWin. 
# 2. Draw welcoming text and input boxes.
# 3. Accept inputs, then wait for click.
# 4. Multiply numbers, display output. 
# 5. Wait for click to close.

from graphics import *

def main():
    win = GraphWin("Multplying Numbers", 300, 200) 
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1,1), "Number 2:").draw(win) 
    Text(Point(1,3), "Number 1:").draw(win) 

    input1 = Entry(Point(2,1), 5)
    input1.setText("0.0")
    input1.draw(win)
    input2 = Entry(Point(2,3), 5)
    input2.setText("0.0")
    input2.draw(win)

    button = Text(Point(1.5,2.0),"Multiply Them!")
    button.draw(win) 

    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    win.getMouse()

    n1 = eval(input1.getText())
    n2 = eval(input2.getText())

    button.setText("Product: " + str(n1*n2))

    win.getMouse()
    win.close()

main()