#! /usr/bin/python
# Exercise No.   3
# File Name:     hw2project3.py
# Programmer:    Mika Okamoto
# Date:          June 21 2020
#
# Problem Statement: Modify the avg2.py program (Section 2.5.3) to find the average of N (where N is any number) exam scores.
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for a number of test scores to be averaged (n)
# 3. Prompt the user n times for the test score.
# 4. Calculate the average of the test scores
# 5. Print results. 

def main():
  print("Hello, welcome! I can calculate average test scores for you.")
  n = eval(input("Enter the number of exam scores to be averaged >> ")) 
  total = 0
  for i in range(n):
    total += eval(input("Enter Exam Score", i+1, " >> "))
  average = total / n
  print("Average exam score: ", average)
main()
