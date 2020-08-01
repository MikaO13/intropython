#! /usr/bin/python
# Exercise No.   1
# File Name:     hw4project1.py
# Programmer:    Mika Okamoto
# Date:          June 27 2020
#
# Problem Statement: Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase.
#
# Overall Plan:
# 1. Prompt the user for input of a phrase.
# 2. Split the phrase into a list of the words in it, determined by space separation.
# 3. Create a variable for an empty string, called acronym. 
# 4. Loop through the list of words in the phrase and add the starting letter of each word to acronym. 
# 5. Print out an uppercase acronym.. 

def main():
    phrase = input("Enter a phrase >> ")
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0]
    print(acronym.upper())    
main()