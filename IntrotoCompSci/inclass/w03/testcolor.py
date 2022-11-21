"""
This program asks the user for a primary color (red, yellow, blue)
and verifies that the color is indeed a primary one
"""

def main():
    color = input("Enter a primary color ")
    if color != "blue" and color != "red" and color != "yellow":
        print("That's not a primary color!")
    else:
        print("bruh, you smart")

main()
