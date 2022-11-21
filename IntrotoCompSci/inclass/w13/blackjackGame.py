from cards import *
from blackjackHand import *

def main():
    instructions()
    deck = Deck()
    deck.shuffle()
    userScore = userTurn(deck)
    if userScore > 21:
        print("Sorry you lose.")
        return
    dealerScore = dealerTurn(deck)
    if dealerScore > 21:
        print("Dealer is busted!")
        print("You win!")
    elif userScore > dealerScore:
        print("You win!")
    elif userScore == dealerScore:
        print("It's a tie.")
    else:
        print("Sorry you lose.")

def instructions():
    print("\nLet's play blackjack!")
    print("The computer will play the role of the dealer.")
    print("The dealer always holds at 17 or higher.")
    print("\nYou'll go first...")

def userTurn(deck):
    """
    Inputs: An instance of the Deck class
    Returns: The user's final score
    Purpose: Allows the user to draw cards and play blackjack
    """
    name = input("What's your name? ")
    hand = BlackjackHand(name)
    hand.addCard(deck.dealOne())
    hand.addCard(deck.dealOne())
    while True:
        print(hand.toString())
        score = hand.getValue()
        if score > 21:
            print("Busted!")
            return score
        action = input("Draw (d) or Hold (h)? ")
        if action == 'd':
            hand.addCard(deck.dealOne())
        elif action == 'h':
            print("Holding...")
            return score
        else:
            print("Invalid choice, try again.")

def dealerTurn(deck):
    """
    Inputs: An instance of the Deck class
    Returns: The dealer's final score
    Purpose: Allows the dealer to draw cards until the value of the hand
    is at least 17
    """
    hand = BlackjackHand("Dealer")
    hand.addCard(deck.dealOne())
    hand.addCard(deck.dealOne())
    while True:
        print(hand.toString())
        score = hand.getValue()
        if score >= 17:
            print("Dealer done...\n")
            return score
        else:
            hand.addCard(deck.dealOne())


main()
