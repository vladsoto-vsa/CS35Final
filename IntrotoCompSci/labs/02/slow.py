"""
This program will have the user input a pause length to seperate the
word they input
"""

def main():
     length = int(input("Pause Length: "))
     text = input("Text: ")
     result = ""
     for i in range(len(text)):
         result = result + text[i]+"." * length
     print(result)
main()
