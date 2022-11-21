from cards import *

class BlackjackHand(object):
    """
    This class is used to represent a hand in the Blackjack card game.
    """
    def __init__(self, name):
        """Saves the player's name and creates an empty list for the hand"""
        self.name = name
        self.hand = []
    def getName(self):
        """Returns the player's name"""
        return self.name
    def getLength(self):
        """Returns the length of the hand"""
        return len(self.hand)
    def addCard(self, card):
        """Adds a card into the hand"""
        self.hand.append(card)
    def __str__(self):
        """Returns a string representing the hand including the player's
        name, the individual cards in the hand, and the blackjack value"""
        result = "\n%s's hand contains %d cards\n" % (self.name,
                                                      self.getLength())
        for i in range(self.getLength()):
            result += "  " + str(self.hand[i]) + "\n"
        result += "Blackjack value: %d\n" % (self.getValue())
        return result
    def getValue(self):
        """
        The score in Blackjack is the sum of the values of the cards
        in the hand.  Face cards (Jack, Queen, and King) are worth
        10 each. An Ace can either be worth 1 or 11.  All other cards
        are worth their rank.  This method calculates the largest
        possible viable score (<= 21) given the number of Aces held.
        """
        numAces = 0
        totalScore = 0
        for i in range(len(self.hand)):
            card = self.hand[i]
            if card.getRank() == 'A':
                numAces += 1
                totalScore += 11
            elif card.getRank() in ['K', 'Q', 'J']:
                totalScore += 10
            else:
                totalScore += int(card.getRank())
        while numAces > 0:
            if totalScore > 21:
                totalScore -= 10
                numAces -= 1
            else:
                break
        if totalScore == 21:
            print("**BLACKJACK!**")
        return totalScore

def main():
    hand1 = BlackjackHand("test1")
    hand1.addCard(Card('A', 'C'))
    hand1.addCard(Card('A', 'D'))
    print(hand1)
    hand2 = BlackjackHand("test2")
    hand2.addCard(Card('10', 'H'))
    hand2.addCard(Card('9', 'D'))
    hand2.addCard(Card('A', 'D'))
    print(hand2)

if __name__ == '__main__':
    main()
