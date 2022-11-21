"""
Using if statements, this program uses the user's input to calculate speed fines
"""

def main():
    limit = int(input("Enter speed limit: "))
    speed = int(input("Enter clocked speed: "))
    total = 0

    if speed > limit:
        print("Motorist is over the limit by", speed-limit, "mph")
        if speed-limit > 5:
            base  = 35
            total = base + ((speed-limit)-5)*2
        if speed-limit > 5 and limit >= 65:
            base = 42.50
            total = base + ((speed-limit)-5)*2

        print("Total fine is: $"+str(total))
    else:
        print("Motorist is within limit")


main()
