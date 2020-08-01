#! /usr/bin/python
# Exercise No.   1
# File Name:     hw1project3.py
# Programmer:    Mika Okamoto
# Date:          June 21 2020
#
# Problem Statement: Modifies the convert function to print an introduction
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Insert the convert function

def main():
  print("Hello, welcome! I can convert Celsius to Fahrenheit for you.")
  celsius = eval(input("What is the Celsius temperature? ")) 
  fahrenheit = (9/5) * celsius + 32
  print("The temperature is ",fahrenheit," degrees Fahrenheit.")

main()
