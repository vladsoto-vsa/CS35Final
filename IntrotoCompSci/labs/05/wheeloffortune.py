"""
Name: Vladimir Soto-Avina
Date: 2/26/2020
Purpose:
    The purpose of this program is a game that gives the user the opportunity
    guess a hidden phrase. They have three options: spinthewheel, guess the phrase,
    or quit. With spinthewheel, it. If the user guesses a letter correctly, with
    multiple functions, the puzzle is further revealed and turns and cash won accumulate
    With guess the phrase, the user has the opportunity to enter a matching guess to the
    answer. if it matches, the program ends. With quit, the program ends.
"""
from wheeloffortune_utils import *

def main():
    answer = choosePhrase()
    puzzle = initPuzzle(answer)
    turns = 0
    money = 0
    done = False
    options = ["spin wheel","guess the phrase", "quit"]

    while done == False:
        print("Puzzle: ", makePhraseString(puzzle))
        print("$" + str(money))
        selection = menu(options)
        if selection == "1":
            money = doSpinWheel(money,puzzle,answer)
            turns = turns + 1
        elif selection == "2":
            turns = turns + 1
            guess = doGuessPuzzle(answer)

            if guess == True:
                print("Cash: $" + str(money) +  " Turns:", turns)
                done = True


        else:
            done = True
    print("The hidden phrase was: ", makePhraseString(answer))
#------------------------------------------------------------------------------
def menu(options):
    """
    Purpose: Using the alldigits function, this prevents a user from choosing
    an option outside of the range or a string
    Parameters: options -- uses the opts list
    Returns: selection -- returns the option the user enters
    Side effects:
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

#------------------------------------------------------------------------------
def alldigits(string):
    """
    Parameters: string -- serves as the list based on tests
    Return: false and true. if it's false, means the item on the list has non
        positive-integers
    Side effects: none

    """
    numbers = ["0","1","2","3","4","5","6","7","8","9"]


    for i in range(len(string)):
        if string[i] not in numbers:
            return False


    return True
#------------------------------------------------------------------------------

def initPuzzle(answer):
    """
    Purpose: Convert answer given by makePhraseString into unkwowns
    Parameters: answer -- the original phrase
    Return: Returns the changed phrase to main
    Side effects: None
    """

    letters = "abcdefghijklmnopqrstuvwxyz"
    puzzle = []
    for i in range(len(answer)):
        if answer[i] in letters:
            puzzle.append("*")
        elif answer[i] == " ":
            puzzle.append("_")
        else:
            puzzle.append(answer[i])
    return puzzle
#------------------------------------------------------------------------------
def updatePuzzle(puzzle,letter,answer):
    """
    Purpose: Reveals characters in puzzle based on user input
    Parameters:
        Puzzle -- uses the puzzle list to reveal certain letter
        letter -- if letter is found in answer, it will replace corresponding
                    character in puzzle
        answer -- is referenced to change/reveal puzzle list
    Returns: none
    Side effects:
    """
    for i in range(len(answer)):
        if letter == answer[i]:
            puzzle[i] = letter
#-------------------------------------------------------------------------------
def askForLetter(message, validChars):
    """Parameters:
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
#-------------------------------------------------------------------------------
def doSpinWheel(money, puzzle, answer):
    """
    Parameters:
        money -- total cash won by player
        puzzle -- current puzzle state
        answer -- hidden phrase

    Return: the new total amount of money. if the user goes bankrupt, money = $0
            Else, the new amount gets added on to previous
    Side effects:
            May modify phrase if user guesses a letter correctly
            prints spin results
    """
    cash = spinWheel()
    times = 0
    if cash != -1:
        print("The wheel spins and lands on $" + str(cash))
        letter = input("Enter a letter: ")

        if letter in puzzle:
            print("You already chose", letter)
        elif letter not in answer:
            print(letter, "is not in the phrase!")
        else:
            times = answer.count(letter)
            newmoney = times * cash
            print("There are " + str(times) + " of " + str(letter) + " in the phrase. You win $" + str(newmoney))
            money = money + newmoney
            updatePuzzle(puzzle,letter,answer)

    else:
        print("The wheel spins and lands on BANKRUPT! YOU SUCKER")
        money = 0

    return money
#------------------------------------------------------------------------------

def doGuessPuzzle(answer):
    """
    Parameters:
        answer -- the hidden phrase
    Return:
        returns true or False if input matches the Answer
    side effects: none
    """
    guess = input("Guess the phrase: ")

    if guess == makePhraseString(answer):
        return True
    else:
        return False

main()
