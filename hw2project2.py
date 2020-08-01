#! /usr/bin/python
# Exercise No.   2
# File Name:     hw2project2.py
# Programmer:    Mika Okamoto
# Date:          June 21 2020
#
# Problem Statement: Write a program that converts degrees Fahrenheit to Celsius using the following formula. 
# degreesC = 5(degreesF – 32)/9
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for the temperature in Fahrenheit
# 3. Convert it to Celsius with the function.
# 4. Print results. 

def main():
  print("Hello, welcome! I can convert Fahrenheit to Celsius for you.")
  fahrenheit = eval(input("Enter a temperature in degrees Fahrenheit >> ")) 
  celsius = 5*(fahrenheit-32)/9
  print(fahrenheit, "degrees Fahrenheit is", celsius, "degrees Celsius.")

main()
