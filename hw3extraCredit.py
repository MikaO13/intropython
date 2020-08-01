#! /usr/bin/python
# Exercise No.   4
# File Name:     hw3extraCredit.py
# Programmer:    Mika Okamoto
# Date:          June 22 2020
#
# Problem Statement: Calculates the Gregorian epact given a year as input. 
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for a year as input.
# 3. Calculate the Gregorian epact.
# 4. Print the result. 

def main():
  print("Hello! I calculate the Gregorian epact for you.")
  year = eval(input("Input a year >> "))
  c = year //100
  epact = (8 + (c//4) - c + ((8*c+13)//25) + 11*(year%19))%30
  
  print(epact)

main()