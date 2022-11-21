"""
This program helps a user learn a foregiun language by making flashcards
"""
from random import shuffle
def main():
    filename = input("Flashcard file? ")
    listOfData = readWordsFile(filename)
    done = False
    while not done:
        shuffle(listOfData)
        numCorrect = testUser(listOfData)
        scoreResults(numCorrect,len(listOfData))
        if not goAgain():
            done = True
    print("bye!")

def goAgain():
    """
    Purpose: To determine if the user wants to do the quiz again
    """
    print("in goAgain")
    return False

def scoreResults(correct, numQuestions):
    """
    Purpose: This function summmarizes the results and prints
    a message based on the percentage the user got correct
    """
    print("in scoreResults")



def readWordsFile(filename):
    """
    Purpose: this function opens the given filename, reads in the test
    words and translations and builds a list of lists.
    """
    print("in readWordsFile...")
    return [["aller", "to go"]]

def testUser(listOfData):
    """
    Purpose: this function runs through all of the flashcards data,
    testing the user on each word and accumulates
    the number of correct answers
    """
    print("in testUser...")
    return 0

main()
