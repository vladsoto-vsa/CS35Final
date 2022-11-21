"""
using if statements to provide answer for questions
"""

def main():
    age = int(input("What is your age? "))
    if age < 0:
        print("invalid!")
    elif age > 100:
        print("seriously?")
    elif age >= 21:
        print("you can legally drink")
    elif age >= 18:
        print("you can legally vote")
    elif age >= 13:
        print("you are a teenager")
    elif age <= 2:
        print("you must be a prodigy")

    else:
        print("bruh, you are baby")
    print("thanks for playing!")

main()
