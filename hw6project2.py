#! /usr/bin/python
# Exercise No.   2
# File Name:     hw6project2.py
# Programmer:    Mika Okamoto
# Date:          July 5 2020
#
# Problem Statement: Write and test sumList(nums), where nums is a list of numbers. Returns the sum of the numbers. 
#
# Overall Plan:
# 1. Define the functions.
# 2. Create a total variable and set to 0
# 3. Iteratre through the list and add all the numbers to total.
# 4. Return total. 
# 5. Test the function.

def sumList(nums):
    total = 0
    for i in nums: total += i
    return total

print(sumList([1, 2, 3, 4, 5, 6, 7, 8, 8]))