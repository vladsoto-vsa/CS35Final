"""
An example of an if statement with both a then and an else.
"""

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    
    if x < y:
        print(x, "is smaller than", y)
    else:
        print(x, "is greater than or equal to", y)

    print("so long")

main()
