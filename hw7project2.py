#! /usr/bin/python
# Exercise No.   2
# File Name:     hw7project2.py
# Programmer:    Mika Okamoto
# Date:          July 9 2020
#
# Problem Statement: Write a program that takes the gender of a child and the parents heights and calculates the height of the child as an adult.
#
# Overall Plan:
# 1. Take the gender and parents heights as inputs.
# 2. Calculate the height in inches with the formulas.
# 3. Print the height of the child. 

import math

gender = input('What is the gender of the child? >> ')
momHeight = eval(input("What is the mother's height in inches? >> "))
dadHeight = eval(input("What is the father's height in inches? >> "))

if gender == 'female':
    inches = round(((dadHeight*12/13)+momHeight)/2)
else:
    inches = round(((momHeight*13/12)+dadHeight)/2)

print('The child is {} feet {} inches.'.format(inches//12, inches%12))