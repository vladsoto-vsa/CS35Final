"""
This file contains the definition of two classes:
1. Card to represent a playing card
2. Deck to represent a deck of 52 playing cards

These classes can be used to build various card games, such as blackjack.
"""

import random

class Card(object):
    """
    The Card class represents individual cards within a standard deck
    of playing cards. Each card has a suit (spades, diamonds, hearts,
    or clubs) and a rank (ace, king, queen, jack, 10, 9, ..., 2).
    """
    suits = ['S','D','H','C']
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    def __init__(self, rank, suit):
        """Ensure that a valid rank and suit are provided"""
        assert((rank in Card.ranks) == True)
        assert((suit in Card.suits) == True)
        self.rank = rank
        self.suit = suit
    def __str__(self):
        """Full name of each suit and rank"""
        if self.suit == 'S':
            suit = "Spades"
        elif self.suit == 'D':
            suit = "Diamonds"
        elif self.suit == 'H':
            suit = "Hearts"
        else:
            suit = "Clubs"
        if self.rank == 'A':
            rank = "Ace"
        elif self.rank == 'K':
            rank = "King"
        elif self.rank == 'Q':
            rank = "Queen"
        elif self.rank == 'J':
            rank = "Jack"
        else:
            rank = self.rank
        return rank + "_of_" + suit
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def getValue(self):
        """
        Aces are considered the highest valued card in most
        games, followed by King, Queen, Jack, 10, 9, ..., 2.
        """
        if self.rank == 'A':
            return 14
        elif self.rank == 'K':
            return 13
        elif self.rank == 'Q':
            return 12
        elif self.rank == 'J':
            return 11
        else:
            return int(self.rank)

class Deck(object):
    """
    The Deck class uses the Card class to create a deck of 52 standard
    playing cards.
    """
    def __init__(self):
        self.deck = self.refresh()
    def getLength(self):
        return len(self.deck)
    def shuffle(self):
        """Randomly re-order the cards in the deck"""
        random.shuffle(self.deck)
    def refresh(self):
        """
        Refreshes the deck back to its original condition, with all
        52 cards.
        """
        deck = []
        for i in range(len(Card.suits)):
            for j in range(len(Card.ranks)):
                deck.append(Card(Card.ranks[j],Card.suits[i]))
        return deck
    def __str__(self):
        result = ""
        for i in range(len(self.deck)):
            result += str(self.deck[i]) + " "
        result += "\n"
        return result
    def dealOne(self):
        """Remove and return the top card on the deck"""
        return self.deck.pop(0)

def main():
    """Add unit testing"""
    print("Unit testing the Card Class")
    card1 = Card('A', 'C')
    card2 = Card('2', 'D')
    print(card1)
    print(card2)
    asser(card1.getRank() == 'A')
    assert(card2.getRank() == '2')
    assert(card1.getValue() == 14)
    assert(card2.getValue() == 2)
    assert(card1.getSuit() == 'C')
    assert(card2.getSuit() == 'D')
    print("Passed all unit tests for Card!")
    deck = Deck()
    assert(deck.getLength() == 52)
    print(deck)
    deck.shuffle()
    print("Shuffled deck: ")
    print(deck)
    cardA = deck.dealOne()
    print("dealt: ", cardA)
    cardB = deck.dealOne()
    print("dealt: ", cardB)

    print("Passed all unit tests for Deck!")


if __name__ == '__main__':
    main()
