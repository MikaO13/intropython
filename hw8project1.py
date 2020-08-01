#! /usr/bin/python
# Exercise No.   1
# File Name:     hw8project1.py
# Programmer:    Mika Okamoto
# Date:          July 16 2020
#
# Problem Statement: Write a program that takes a number and calculates that number of the fibonacci sequence.
#
# Overall Plan:
# 1. Define a recursive function called fibonacci, and program it to find increment itself until it reaches the given number or the fibonacci sequence.
# 2. Run this function with the number being one that the user is prompted to give.

counter = 0
def fibonacci(x, y, n):
    global counter
    if counter == n:
        print(y)
    else:
        counter += 1
        fibonacci(y, x+y, n)

fibonacci(1, 1, eval(input('Choose a number >> ')))