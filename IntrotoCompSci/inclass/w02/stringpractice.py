"""
Practicing with strings
"""

def main():
    text = input("Enter some text: ")
    repeats = int(input("How many repetitions per letter: "))
    # Accumulating a string result, start with empty
    result = ""
    for i in range(len(text)):
        result = result + text[i]*repeats
    print("Result is", result)

main()
