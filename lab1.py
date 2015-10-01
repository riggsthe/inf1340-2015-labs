#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowels_and_consonants():
    """
    Exercise: Vowel or Consonant
    Reads a letter of the alphabet from the user. (You can assume that it's
    lowercase.) If the user enters a, e, i, o or u then your program should
    display "vowel". If the user enters y then your program should display
    "sometimes a vowel, sometimes a consonant". Otherwise your program should
    display a message indicating that the letter is a "consonant".
    """
# Issue instruction to user to input a letter
    letter = raw_input("input a letter")
# Establish vowels with if statements
    if letter == "a":
        print("vowel")
    elif letter == "e":
        print("vowel")
    elif letter == "i":
        print("vowel")
    elif letter == "o":
        print("vowel")
    elif letter == "u":
        print("vowel")

# Establish y is a vowel sometimes, sometimes a consonant with another if statement
    elif letter == "y":
        print("Sometimes a vowel, sometimes a consonant")
# Establish rules for consonants with else statement

    else:
        print("consonant")
# For some reason when a vowel is entered (besides y) it prints both "vowel" and "consonant". how to fix??

vowels_and_consonants()

