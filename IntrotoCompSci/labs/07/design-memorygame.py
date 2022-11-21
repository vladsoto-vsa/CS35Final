"""
Purpose: This is top-down design for a card game that allows the player
to match a deck of cards
Name: Vladimir Soto-Avina
Date: 3/25/2020
"""

def main():
    introduction()
    cardMatches = 0
    turns = 0
    done = False
    revealedCards = ["finch","finch","robin","robin","crane","crane","macaw",
    "macaw","stork", "stork"]
    shuffledCards = shuffle(revealedCards)
    hiddenCards = hideCardNames(shuffledCards)

    while not done:
        displayCards(hiddenCards)
        cardOne = userChoices(hiddenCards)
        cardTwo = userChoices(hiddenCards)
        if compareCards(shuffledCards,cardOne,cardTwo) == True:
            updateCards(shuffledCards,cardOne,cardTwo,hiddenCards)
            turns = turns + 1
            cardMatches = cardMatches + 1
            print("Yeet")
        else:
            turns = turns + 1
            print("nah nah")
        if cardMatches == 5:
            done = True
            reportResults(cardMatches, turns)
            feedback(cardMatches, turns)

#------------------------------------------------------------------------------
def introduction():
    """
    Purpose: Prints a welcome message to user
    Parameters: nothing
    Returns: nothing
    """
    print("calling introduction")

#-------------------------------------------------------------------------------

def displayCards(cards):
    """
    Purpose: Displays hidden/uncovered cards using updateCards
    Parameters:
        cards -- uses the bird list to reveal words
    Returns: nothing
    """
    display = 0
    print("Calling displayCards")


#------------------------------------------------------------------------------

def alldigits(number):
    """
    Purpose: Checks whether the user's input is valid
    Parameters:
        Number -- the integer the user inputs
    Returns: True or False
    """
    #numbers = ["0","1","2","3","4","5","6","7","8","9"]

    #if number not in numbers:
    #    return False
    print("calling alldigits")
    return True

#-------------------------------------------------------------------------------

def hideCardNames(answers):
    """
    Purpose: Converts the shuffled deck of cards into numbered cards.
    Parameters: answers - the card types/card names
    Returns: Returns the changed list to main
    """
    print("Calling hideCardNames")
    return 0

#-------------------------------------------------------------------------------

def updateCards(cardWords, SelectionOne, SelectionTwo, cardNumbers):
    """
    Purpose: Updates the display of the cards by changing list that displays
    numbers into the answers
    Returns: returns new list for displayCards
    Parameters:
        cardWords - the answer list that is used to update cardNumbers
        SelectionOne - the first integer the user inputs
        SelectionTwo - the second integer the user inputs
        cardNumbers - this list is updated to be used by displayCards
    """
    if cardWords[SelectionOne] not in cardNumbers:
        print("You already chose that dummy!")
    else:
        cardWords[SelectionOne] == cardNumbers[SelectionOne]
        cardWords[SelectionTwo] == cardNumbers[SelectionTwo]
        print("Yeet")

    print("Calling updateCards")
    return cardNumbers
#------------------------------------------------------------------------------
def userChoices(answers):
    """
    Purpose: Using the alldigits function, this prevents a user from choosing
    an option outside of the range or a string
    Parameters: answers - the list of card answers
    Return: selection -- returns the integer the user enters
    """

    selection = int(input("card to flip> "))

    return selection



#------------------------------------------------------------------------------

def compareCards(shuffledCards, cardOne, cardTwo):
    """
    Purpose: Compares whether or not cards match
    Parameters:
        cardOne -- first integer chosen by user
        cardTwo -- second integer chosen by user
    Returns: True or False
    """
    if shuffledCards[cardOne] == shuffledCards[cardTwo]:
        return True
    else:
        return False

#-----------------------------------------------------------------------------

def reportResults(cardMatches, turns):
    """
    Purpose: Report how many turns it took for player to match all cards
    Parameters: integeres representing number of cards matched and turns
    Returns: nothing
    """
    print("Calling reportResults")

#-----------------------------------------------------------------------------
def feedback(cardMatches, turns):
    """
    Purpose: Gives user certain praise dependent on turns they took to
    match all cards
    Parameters:
        cardMatches - since there are different sizes for card decks, the
        feedback will also be dependent on size
        turns - the amount of turns taken determines score
    Returns: nothing
    """
    print("calling feedback")



main()
