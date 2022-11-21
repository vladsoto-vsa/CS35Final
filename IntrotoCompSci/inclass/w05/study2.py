def main():
    word = input("Enter a word: ")
    letter = ""

    for i in range(len(word)):
        if word[i] == "e":
            letter = letter + "E"
        else:
            letter = letter + word[i]

    print(letter)
main()
