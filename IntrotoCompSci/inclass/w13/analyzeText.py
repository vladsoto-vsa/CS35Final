"""
Analyze the text of 'Alice in Wonderland' by Lewis Carroll which is
stored on the CS system in this file:

/usr/local/stow/cs21/doc/alice.txt

Use a dictionary data structure to calculate the word frequencies for
unique words used in this book.  Sort the words based on frequency.
Show the top 100 most used words.

wordFrequency[<word>] = <count>
keys are the unique words in the book
values are the number of occurences of each word in the book
"""

def main():
    wordFrequency = processFile("/usr/local/stow/cs21/doc/alice.txt")
    print("Found", len(wordFrequency), "unique words in text")
    ls = list(wordFrequency.items())
    ls.sort(reverse=True,key=getCount)
    print(ls[:100])

def getCount(pair):
    return pair[1]

def processFile(filename):
    """
    Inputs: The filename of the text of a book
    Returns: a dictionary keyed on unique words with values being the
                number of occurrences of each word
    """
    file = open(filename, "r")
    wordFrequency = {} # keys are unique words, values are word counts
    line_count = 0

    for line in file:
        if line[0] != "#":
            line_count = 0
            words = line.strip().split()
            for i in range(len(words)):
                cleaned_word = words[i].strip(",.!?;:()[]\"_'-*")
                cleaned_word = cleaned_word.lower()
                if cleaned_word in wordFrequency:
                    wordFrequency[cleaned_word] += 1
                else:
                    wordFrequency[cleaned_word] = 1



    file.close()
    print("Processed", line_count)
    return wordFrequency
main()
