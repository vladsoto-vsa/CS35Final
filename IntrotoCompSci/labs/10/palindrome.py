"""
Name: Vladimir Soto-Avina
Date: April 22nd, 2020
Program to check whether user-entered strings are palindromes.
"""
def main():

    done = False
    while done == False:
        text = input("Enter some text (or 'quit'): ")
        if text != "quit":
            checkedtext = isPalindrome(text)
            if checkedtext == True:
                print("Yes, it's a palindrome!")
            else:
                done
                print("No, it's not a palindrome!")
        else:
            done = True
            print("Goodbye")


def isPalindrome(text):
    """
    Purpose: This function examines a text string entered by the user using
            recursion to see if the text is a palindrome
    Parameters:
        text -- the text that is checked to see if it's a parameter
    Returns:
        Returns true or false
    """
    if len(text) <= 1:
        return True
    else:
        if text[0].isalpha() == False:
            return isPalindrome(text[1:])
        elif text[len(text)-1].isalpha() == False:
            return isPalindrome(text[:len(text) - 1])
        else:
            if text[0].lower() == text[len(text) - 1].lower():
                return isPalindrome(text[1:len(text) - 1])
            else:
                return False


main()
