"""
Example of a while loop
"""
def main():
    grade = int(input("enter a grade between 0 and 100: "))
    counteErrors = 0
    while grade < 0 or grade > 100:
        print("Invalid! Try again.")
        grade = int(input("Enter a grade between 0 and 100: "))
        counteErrors = counteErrors + 1
        if counteErrors > 5:
            print("Come on, bruh! Don't be dummy!")
    print("you entered: ", grade)

main()
