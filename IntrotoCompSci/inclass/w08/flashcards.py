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
    fp = open(filename, "r")
    ls = []
    for line in fp:
        data = line.strip().split(",")
        ls.append(data)
    return ls

def testUser(listOfCards):
    """
    Parameters:
    listOfCards List of lists storing the prompts and answers
    Returns:
    int representing the number of correct answers
    """
    print("="*30)
    correct = 0
    for i in range(len(listOfCards)):
        answer = input(listOfCards[i][0]+": ")
        if answer == listOfCards[i][1]:
            correct += 1
            print("Correct!")
        else:
            print("Nope...", listOfCards[i][0], "means", listOfCards[i][1])
        print("-"*30)
    return correct

def reportResults(correct, totalPossible):
    """
    Parameters:
    correct int representing the number of correct answers
    totalPossible int representing the number of questions
    Returns:
    None, just prints a message about the results
    """
    pct = correct/totalPossible
    if pct == 1.0:
        msg = "That's amazing!"
    elif pct >= 0.8:
        msg = "Well done."
    elif pct >= 0.7:
        msg = "Keep practicing."
    else:
        msg = "You need a lot more practice!"
    print("You got", correct, "out of", totalPossible)
    print(msg)
    
def goAgain():
    """
    Prompts the user to find out if they want to try again.
    Returns: 
    Either True or False
    """
    while True:
        answer = input("Go again (y/n)? ")
        if answer == "n":
            return False
        elif answer == "y":
            return True
        else:
            print("Invalid answer!")
        

main()

    
