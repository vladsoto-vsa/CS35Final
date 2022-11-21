"""
Ensure user givers integer input in a valid range
"""

def main():
    age = getIntegerInRange("Enter your age: ", 10, 100)
    gradYear = getIntegerInRange("Enter graduation year: ",2020,2023)
    print("Your age is %d and your grad year is %d" % (age, gradYear))


def getIntegerInRange(prompt, low, high):
    """
    While it's greater than stop and less than start, print message to indicate
    another integer
    Parameters: prompt is a string, low and high are ints
    Returns: the valid number is inputed by the user
    """
    valid = False
    while not valid:
        value = int(input(prompt))
        if value >= low and value <= high:
            valid = True
        else:
            print("Invalid. enter a value between %d and %d." % (low, high))
    return value

main()
