"""
This program suggests a tip amount based on total cost of dinner by using percentages of total cost
"""

def main():
    bill = float(input("Total bill? $"))
    print("with 10% tip: $", bill * 1.1, "(tip = $", bill * .1,")")
    print("with 15% tip: $", bill * 1.15, "(tip = $", bill * .15,")")
    print("with 20% tip: $", bill * 1.2, "(tip = $", bill * .2,")")

main()
