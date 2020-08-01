#! /usr/bin/python
# Exercise No.   1
# File Name:     hw7project1.py
# Programmer:    Mika Okamoto
# Date:          July 9 2020
#
# Problem Statement: Write a program which takes the input of a percentage grade and outputs the letter grade.
#
# Overall Plan:
# 1. Take percentage as input.
# 2. Use if/elif statements to figure out the grade.
# 3. Print grade.

percentage = eval(input('What is your percentage grade in the class? >> '))
if percentage < 60:
    print('You receive a F.')
elif percentage < 70:
    print('You receive a D.')
elif percentage < 80:
    print('You receive a C.')
elif percentage < 90:
    print('You receive a B.')
elif percentage < 100:
    print('You receive a A.')