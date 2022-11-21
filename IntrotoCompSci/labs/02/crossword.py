"""
This program will print out a word and its reverse, while having two columns of
the two variation sbeing spelled out
"""

def main():
    phrase = input("Enter a phrase: ")
    length = (len(phrase))
    reverse = ""

    print(phrase)

    for i in range(length - 1 , -1 , -1):
        reverse = reverse + phrase[i]

    for i in range(1 ,length - 1, 1):
        print(phrase[i+1] + " " * (length-2) + reverse[i])


    print(reverse)


main()
