#! /usr/bin/python
# Exercise No.   3
# File Name:     hw6project3.py
# Programmer:    Mika Okamoto
# Date:          July 5 2020
#
# Problem Statement: Write a program that prints the lyrics to the ten verses of "The Ants go Marching"
#
# Overall Plan:
# 1. Define lists to use when looping.
# 2. Loop 10 times and print out the lyrics, formatting with the lists.

count = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ants = ['suck his thumb', 'tie his shoe', 'get stung by a bee', 'eat more', 'smell the bee hive', 'eat cake mix', 'go into heaven', 'check and mate', 'be sublime', 'play with stick men']
for i in range(10):
    print('The ants go marching {} by {}, hurrah! hurrah!'.format(count[i], count[i]))
    print('The ants go marching {} by {}, hurrah! hurrah!'.format(count[i], count[i]))
    print("The ants go marching {} by {},".format(count[i], count[i]))
    print("The little one stops to " + ants[i])
    print('And they all go marching down...')
    print('In the ground...')
    print("To get out...")
    print("Of the rain.")
    print('Boom! Boom! Boom!')