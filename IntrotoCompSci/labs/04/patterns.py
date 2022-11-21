"""
This program prints out a shape with letters. The type of shape
is chosen by the user from a set of options
"""

from random import *

def main():
    """
    Purpose: have user choose from options
    Parameters: none
    Returns: none
    """
    done = False
    options = ["block","triangle","reverse","diamond", "quit"]
    while not done:
        selection = menu(options)
        letter = list("ABDCEFG")
        randomnumber = randrange(5,16)
        if selection == "1":
            block(randomnumber,choice(letter))
        elif selection == "2":
            triangle(randomnumber,choice(letter))
        elif selection == "3":
            reverse(randomnumber,choice(letter))
        elif selection == "4":
            diamond(randomnumber,choice(letter))
        else:
            done = True


def menu(options):
    for i in range(len(options)):
        print(str(i+1)+".", options[i])

    done = False
    while not done:
        selection = input("your choice --> ")
        if alldigits(selection) == False:
            print("please enter a positive integer")

        elif int(selection) > len(options) or int(selection) < 1:
            print("please enter a valid choice!!!")

        else:
            done = True
    return selection


def alldigits(string):
    """
    This function returns true if all of the characters in the string
    are digits. If they're not, then it returns false
    """
    numbers = ["0","1","2","3","4","5","6","7","8","9"]


    for i in range(len(string)):
        if string[i] not in numbers:
            return False


    return True

def block(rows, letter):
    """
    Purpose: This makes a block out of letters and determined rows
    Parameters: rows -- how many lines the block prints letters
                letter -- type of letter
    Returns: none

    """
    for i in range(rows):
        print(letter * rows)

def triangle(rows, letter):
    """
    Purpose: This makes a triangle out of letters and determined rows
    Parameters: rows -- how many lines the block prints letters
                letter -- type of letter
    Returns: none

    """
    for i in range(rows):
        print(letter * (i + 1))

def reverse(rows, letter):
    """
    Purpose: This makes a triangle, like the last one but flipped, out of letters and determined rows
    Parameters: rows -- how many lines the block prints letters
                letter -- type of letter
    Returns: none

    """
    for i in range(rows):
        rows = rows - 1
        print((" " * rows) + letter * (i + 1))

def diamond(rows, letter):
    """
    Purpose: This makes a diamond out of letters and determined rows
    Parameters: rows -- how many lines the block prints letters
                letter -- type of letter
    Returns: none

    """
    rows2 = rows
    for i in range(rows):
        rows = rows - 1
        print((" " * rows) + letter * (i + 1) + letter * (i + 1))

    for j in range(rows2):
        rows2 = rows2 - 1
        print((" " * j) + letter * (rows2 + 1) + letter * (rows2 + 1))


main()
