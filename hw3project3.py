#! /usr/bin/python
# Exercise No.   3
# File Name:     hw3project3.py
# Programmer:    Mika Okamoto
# Date:          June 22 2020
#
# Problem Statement: Determine the length of a ladder required to reach a given height when leaned against a house. The height and angle of the ladder are given as inputs. length = height/(sin angle)
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for the height and the angle of the ladder. 
# 3. Calculate the length of the ladder. 
# 4. Print the result. 

import math

def main():
  print("Hello! I can determine the length of a ladder required to reach a given height when leaned against a house.")

  height = eval(input("What is the height? >> "))
  angle = eval(input("What is the angle? >> "))

  length = height / (math.sin(angle))

  print('The length of the ladder is', length)

main()