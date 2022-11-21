"""
This program displays a list with and allows the user to select an item on the list
"""

def main():
    opts = ["yes","no"]
    choice = menu(opts)
    print("You chose:", choice)

# add your menu function here
def menu(options):
    """
    Purpose: Using the alldigits function, this prevents a user from choosing
    an option outside of the range or a string
    Parameters: options -- uses the opts list
    Returns: selection -- returns the option the user enters
    """
    for i in range(len(options)):
        print(str(i+1)+".", options[i])
    done = False
    while not done:
        selection = input("your choice: ")
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




main()
