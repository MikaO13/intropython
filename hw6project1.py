#! /usr/bin/python
# Exercise No.   1
# File Name:     hw6project1.py
# Programmer:    Mika Okamoto
# Date:          July 5 2020
#
# Problem Statement: Write definitions for these functions: sphereArea(radius) and sphereVolume(radius)
#
# Overall Plan:
# 1. Import math modules.
# 2. Define the functions.
# 3. Return the formulas. 
# 4. Test the functions.

import math

def sphereArea(radius):
    return 4 * math.pi * (radius ** 2)

def sphereVolume(radius):
    return 4/3 * math.pi * (radius ** 3)

print(sphereArea(4))
print(sphereVolume(4))