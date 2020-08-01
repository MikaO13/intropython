#! /usr/bin/python
# Exercise No.   2
# File Name:     hw3project2.py
# Programmer:    Mika Okamoto
# Date:          June 22 2020
#
# Problem Statement: Write a program that divides two number and outputs the results using whole numbers and the remainder.
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two numbers. 
# 3. Calculate the result and the remainder. 
# 4. Print the results. 

def main():
  print("Hello! I divide two numbers and tell you the result and the remainder.")
  x = eval(input("Enter a number >> "))
  y = eval(input("Enter a second number >> "))
  result = x // y
  remain = x % y
  print(str(result) + "R" + str(remain))

main()

