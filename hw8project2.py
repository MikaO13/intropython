#! /usr/bin/python
# Exercise No.   2
# File Name:     hw8project2.py
# Programmer:    Mika Okamoto
# Date:          July 16 2020
#
# Problem Statement: Write a program that takes an Image and converts it to grayscale.
#
# Overall Plan:
# 1. Import graphics, open a GraphWin, and ask the user for the image file name.
# 2. Wait for a click, then loop through each row and column of the image.
# 3. When looping, get the rbg values, then create a brightness value for converting to grayscale.
# 4. Then set the pixel colors to the grayscale equivalent.
# 5. Redraw the image on the graphwin.
# 6. Wait for a click, then prompt the user for a file name to save the new image at.


from graphics import *

win = GraphWin()
img = Image(Point(100,100), input('What is the name of the image file? >> '))
img.draw(win)
win.getMouse()
for i in range(img.getWidth()):
    for j in range(img.getHeight()):
        r, g, b = img.getPixel(i, j)
        brightness = int(round(0.299*r + 0.587 *g + 0.114*b))
        img.setPixel(i, j, color_rgb(brightness, brightness, brightness))
    img.undraw()
    img.draw(win)
win.getMouse()
img.save(input('What file name would you like to save this image at? >> '))