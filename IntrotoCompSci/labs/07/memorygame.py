from random import *

"""
Purpose: This is top-down design for a card game that allows the player
to match a deck of cards
Name: Vladimir Soto-Avina
Date: 3/25/2020
"""

def main():
    introduction()
    cardMatches = 0
    turns = 1
    done = False
    revealedCards = ["finch","robin","crane","macaw","stork"]
    shuffledCards = mixCards(revealedCards)
    hiddenCards = hideCardNames(shuffledCards)
    print(shuffledCards)

    while not done:
        displayCards(hiddenCards)
        cardOne = userChoices(hiddenCards, turns)
        cardTwo = userChoices(hiddenCards, turns)

        if compareCards(shuffledCards,cardOne,cardTwo, hiddenCards) == True:
            updateCards(shuffledCards,cardOne,cardTwo,hiddenCards)
            cardMatches = cardMatches + 1
        if cardMatches == len(revealedCards):
            done = True
            reportResults(cardMatches, turns)
            feedback(cardMatches, turns)
        if cardOne != cardTwo:
            turns = turns + 1

#------------------------------------------------------------------------------
def introduction():
    """
    Purpose: Prints a welcome message to user
    Parameters: nothing
    Returns: nothing
    """
    msg = """
         ----Let's play a game----
      Are you smarter than....a MONKEY?
    ----Match the cards from the deck----

    """
    print(msg)

#------------------------------------------------------------------------------

def mixCards(revealedCards):
    """
    Purpose: Creates a new list based off of the original and shuffles
    Parameters:
        revealedCards - Uses these cards to shuffle
    Returns: a shuffled list based on original

    """
    shuffledCards = sample(revealedCards,len(revealedCards))
    shuffledCards = shuffledCards * 2
    shuffle(shuffledCards)
    return shuffledCards
#-------------------------------------------------------------------------------

def displayCards(cards):
    """
    Purpose: Displays hidden/uncovered cards using updateCards
    Parameters:
        cards -- uses the bird list to reveal words
    Returns: nothing
    """
    print("=" * 100)

    display = ""
    for i in range(len(cards)):
        display = display + ("===%s=== " % (cards[i]))
    print(display)

#------------------------------------------------------------------------------

def alldigits(number):
    """
    Purpose: Checks whether the user's input is valid
    Parameters:
        Number -- the integer the user inputs
    Returns: True or False
    """
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    if number not in numbers:
        return False

    return True

#-------------------------------------------------------------------------------

def hideCardNames(shuffledCards):
    """
    Purpose: Converts the shuffled deck of cards into numbered cards.
    Parameters:
        shuffledCards - the card types/card names
    Returns: Returns the converted list
    """

    hiddenList = []

    for i in range(len(shuffledCards)):
        hiddenList.append(i)
    return hiddenList


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

    cardNumbers[SelectionOne] = cardWords[SelectionOne]
    cardNumbers[SelectionTwo] = cardWords[SelectionOne]

    print("Yeet")

#------------------------------------------------------------------------------
def userChoices(cardNumbers, turns):
    """
    Purpose: Using the alldigits function, this prevents a user from choosing
    an option outside of the range or a string
    Parameters:
        cardNumbers - the list of numbered cards
        turns - numbers of turns user has tried to match cards
    Return: selection -- returns the integer the user enters
    """

    print("Turn #"+str(turns)+":")
    done = False
    while not done:
        selection = (input("card to flip> "))
        if alldigits(selection) == False:
            print("Select a card 0-9")

        else:
            done = True
    selection = int(selection)

    return selection



#------------------------------------------------------------------------------

def compareCards(cardWords, cardOne, cardTwo, cardNumbers):
    """
    Purpose: Compares whether or not cards match
    Parameters:
        cardWords -- list with answers/words
        cardOne -- first integer chosen by user
        cardTwo -- second integer chosen by user
        cardNumbers -- numbered list that hides words
    Returns: True or False
    """


    if cardOne == cardTwo:
        print("You can't choose the same card")
        return False
    elif cardWords[cardOne] == cardNumbers[cardOne]:
        print("You already matched this pair")
        return False
    elif cardWords[cardOne] == cardWords[cardTwo]:
        return True

    else:
        print("nah nah")
        return False

#-----------------------------------------------------------------------------

def reportResults(cardMatches, turns):
    """
    Purpose: Report how many turns it took for player to match all cards
    Parameters:
        cardMatches - pairs of cards matched
        turns - amount of turns taken to match cards
    Returns: nothing
    """
    print(cardMatches, "cards matched in", turns, "turns.")

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
    if cardMatches/turns >= .8:
        print("Woah, smarty! I proclaim you King of the Chimps!")
    elif cardMatches/turns < .8 and cardMatches/turns >= .7:
        print("Heeeeey, that was pretty good.")
    elif cardMatches/turns < .7 and cardMatches/turns >= .5:
        print("That was alright. I give you a C for Chimp.")
    else:
        print("Eeesh, the office monkey can do better.")



main()
