#! /usr/bin/python
# Exercise No.   1
# File Name:     hw4project1.py
# Programmer:    Mika Okamoto
# Date:          June 27 2020
#
# Problem Statement: Write a program that open the file you just created and reads each line into a list. Name this file hw5project2.py.
#                    Process each item of the list by converting the two number strings in list to numbers and summing them together. Write this sum out to a file, output.txt. 
#
# Overall Plan:
# 1. Open input.txt and read lines into a list.
# 2. Sum the two space separated numbers in each line into a number and write the sum to a list. 

def main():
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')

    lines = fin.readlines()
    for line in lines:
        x, y = map(int, line.split())
        fout.write(str(x+y) + '\n')

    fin.close()
    fout.close()
main()