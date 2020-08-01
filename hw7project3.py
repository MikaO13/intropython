#! /usr/bin/python
# Exercise No.   3
# File Name:     hw7project3.py
# Programmer:    Mika Okamoto
# Date:          July 9 2020
#
# Problem Statement: Write a program that calculates if a speed is illegal and the fine for speeding if it is. 
#
# Overall Plan:
# 1. Take the limit and the clocked time as inputs.
# 2. Calculate if it is legal or not.
# 3. If it is not, calculate the fine.
# 4. Print if it is legal or not, and the fine if it is not.

limit = eval(input('What is the speed limit? >> '))
clocked = eval(input('What is the speed of the car? >> '))

if clocked <= limit:
    print('The speed is legal.')
else:
    fine = 50 + (clocked - limit)*5
    if clocked > 90: fine += 200
    print('The speed is illegal, and the fine is ' + str(fine))