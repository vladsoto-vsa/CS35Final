"""
This program helps the user compute the tip and total amount owed.
"""

def main():
    amount = float(input("Enter the amount of the bill: $"))
    percent = int(input("Enter tip percentage (e.g. 15): %"))
    # call the computeTip function
    # print the tip and the total bill with tip
    # add a for loop to show tip percents 5,10,15,20
    for pct in range(5,21,5):
        tip = computeTip(amount, pct)
        print("For tip pct", pct, "Total is", amount + tipAmount)

def computeTip(bill, tipPercent):
    return bill * (tipPercent/100)
# Write a function called computeTip that takes the bill amount and
# the tip percentage as an integer.  It returns the tip amount.
# For example, computeTip(50.00, 10) would return 5.0.


main()
