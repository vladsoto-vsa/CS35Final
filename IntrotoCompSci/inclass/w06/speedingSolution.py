"""From PA drivinglaws.org:

For most speeding violations, the fine is $35 plus $2 for every mile
in excess of 5 mph over the limit. However, if the maximum limit is 65
mph or higher, the fine is $42.50 plus $2 for every mile in excess of
5 mph over the limit.

"""

def main():
    print()
    limit = int(input("Enter speed limit: "))
    speed = int(input("Enter clocked speed: "))
    print()
    if speed < limit:
        print("Motorist is within the limit")
    else:
        over = speed - limit
        print("Motorist is over the limit by", over, "mph")
        print()
        if limit < 65:
            fine = 35
        else:
            fine = 42.50
        if over > 5:
            print("Base fine is: $%.2f" % fine)
            extra = over - 5
            print("Additional $2 per %d miles in excess of 5 mph over limit" % extra)
            fine +=  2 * extra
        print("Total fine is: $%.2f" % fine)
    print()
        
main()
