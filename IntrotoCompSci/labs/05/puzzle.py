"""
This program has two functions that display chracters. One of them contains
the answer but hides the characters, while the other reveals the characters based on input
Name: Vladimir Soto-Avina
Date: 2/26/2020
"""

from wheeloffortune_utils import *



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



def main():
    answer = choosePhrase()
    print("Answer: ", makePhraseString(answer))
    puzzle = initPuzzle(answer)
    print("Puzzle: ", makePhraseString(puzzle))
    # call initPuzzle
    done = False
    while not done:
        letter = input("Enter a letter (type ENTER to quit): ")
        updatePuzzle(puzzle,letter,answer)
        print("Puzzle: ", makePhraseString(puzzle))
        if letter == "" or answer == puzzle:
            done = True
    # call updatePuzzle in a while loop (user types ENTER to exit)


main()
