"""
Example of a multiway if
"""

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    
    if x == y:
        print("the numbers are equal")
    elif x < y:
        print(x, "is smaller")
    else:
        print(x, "is larger")

    print("so long")

main()
