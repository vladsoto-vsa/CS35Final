"""
example of using while loop with random events

How many coin flips needed to get 5 heads in a row?
"""

from random import choice

def main():
    flips = 0
    consecutiveHeads = 0
    while consecutiveHeads < 5:
        outcome = choice(["heads", "tails"])
        if outcome == "heads":
            consecutiveHeads = consecutiveHeads + 1
        else:
            consecutiveHeads = 0
        flips = flips + 1
    print("It took", flips, "flips to get 5 consecutive Heads")

main()
