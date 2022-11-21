from random import shuffle

def main():
    filename = input("Flashcard file? ")
    cards = readCardData(filename)
    done = False
    while not done:
        shuffle(cards)
        correct = testUser(cards)
        reportResults(correct, len(cards))
        if not goAgain():
            done = True
    print("Bye!")

def readCardData(filename):
    """
    Parameters:
    filename a string representing name of a file containing the flashcard
    data
    Returns:
    list of lists storing a series of prompts and answers to test on
    """
    print("Calling readCardData...")
    return [[]]

def testUser(listOfCards):
    """
    Parameters:
    listOfCards List of lists storing the prompts and answers
    Returns:
    int representing the number of correct answers
    """
    print("Calling testUser...")
    return 0

def reportResults(correct, totalPossible):
    """
    Parameters:
    correct int representing the number of correct answers
    totalPossible int representing the number of questions
    Returns:
    None, just prints a message about the results
    """
    print("Calling reportResults...")
    print("results", correct, totalPossible)
    
def goAgain():
    """
    Prompts the user to find out if they want to try again.
    Returns: 
    Either True or False
    """
    print("Calling goAgain...")
    return False

main()

    
