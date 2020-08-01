#! /usr/bin/python
# Exercise No.   1
# File Name:     hw11project1.py
# Programmer:    Mika Okamoto
# Date:          July 26 2020
#
# Problem Statement: Write a program that counts the reserved words in a python file.
#
# Overall Plan:
# 1. Read in the text file and the reserved word list. 
# 2. Loop through each line in the text file.
# 3. Loop through each word in the line.
# 4. Check if the word is in the reserved word list, and if so, increment a counter.
# 5. Print out the counter.

fin = open('file.txt', 'r')
reswords = ['False', 'class', 'finally', 'is', 'return', 'None', 'continue', 'for', 'lambda', 'try', 'True', 'def', 'from', 'nonlocal', 'while', 'and', 'del', 'global', 'not', 'with', 'as', 'elif', 'else', 'if', 'or', 'yield', 'assert', 'import', 'pass', 'break', 'except', 'in', 'raise']
c = 0

for line in fin.readlines():
    for word in line.split():
        if word in reswords:
            c += 1

print('There were {} words in the file that were in reserved words list.'.format(c))

fin.close()