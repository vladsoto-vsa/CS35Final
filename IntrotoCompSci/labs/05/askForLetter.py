"""
Name: Vladimir Soto-Avina
Date: 2/25/2020
This program asks the user to input a character from a given subset. If it's
of the invalid format/character, it will ask until the user gives an acceptable
character
"""

from wheeloffortune_utils import *

# TODO: Define askForLetter
def main():
    letter = askForLetter("Enter a consonant: ", "bcdfghjklmnpqrstvwxyz")
    print("You chose:", letter)

    letter = askForLetter("Enter a vowel: ", "aeoiu")
    print("You chose:", letter)

def askForLetter(message, validChars):
    """
    Parameters:
        message -- message shown to user when asked to enter a letter
        validChars -- characters included in the given subset that
        would be accepted by function
    Returns:
        character chosen by user
    Side Effects:
        none
    """
    done = False
    while not done:
        character = input(message)
        if character in validChars:
            done = True
            return character
        elif character not in validChars:
            print(character, "is not valid. Try again.")


main()
