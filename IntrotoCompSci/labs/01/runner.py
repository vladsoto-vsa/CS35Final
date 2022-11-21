"""
This program calculates running times by convertind distance units
"""

def main():

    Seconds = float(input("How many seconds does it take you to run a lap? "))

    print("1 mile time:", Seconds * 4, "(minutes =", Seconds *4 /60,")")
    print("10K time:", Seconds * 24.8, "(minutes =", Seconds *24.8 /60,")")
main()
