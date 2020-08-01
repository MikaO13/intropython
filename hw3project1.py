#! /usr/bin/python
# Exercise No.   1
# File Name:     hw3project1.py
# Programmer:    Mika Okamoto
# Date:          June 22 2020
#
# Problem Statement: Write a program that calculates the cost per square inch of a circular pizza given its diameter and price.
# pi r^2
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the

import math

def main():
  print("Hello, welcome! I calculate the cost per square inch of a circular pizza for you!")
  diameter = eval(input("What is the diameter of the pizza in inches? >> "))
  price = eval(input("What is the price of the pizza? >> "))
  area = math.pi * (diameter/2)**2
  cpsi = price / area
  print("The cost per square inch of the pizza was", cpsi)

main()