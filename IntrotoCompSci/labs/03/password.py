"""
Use string accumulation to make good passwords
"""

def main():
    phrase = input("Enter phrase: ")
    password = ""


    for i in range(len(phrase)):
        if phrase[i] == "a" or phrase[i] == "A":
            password = password + "@"
        elif phrase[i] == "e" or phrase[i] == "E":
            password = password + "3"
        elif phrase[i] == "i" or phrase[i] == "I":
            password = password + "1"
        elif phrase[i] == "o" or phrase[i] == "O":
            password = password + "0"
        elif phrase[i] == "u" or phrase[i] == "U":
            password = password + "^"
        elif phrase[i] == " ":
            password = password
        else:
            password = password + phrase[i]
    print("Possible password: ", password)

main()
