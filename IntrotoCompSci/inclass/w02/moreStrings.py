"""
Este programa will take a text input de el usuario y va a producir un output
string of the following form:

'abc' => 'abbccc'
'swat'
"""


def main():
    text = input("Enter some text: ")
    result = ""
    for i in range(len(text)):
        result = result + text[i] *(i+1)
    print("Result is", result)

main()
