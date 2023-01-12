import string
import sys


def text_analyzer(text={}):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    if text is text_analyzer.__defaults__[0]:
        text = input("What is the text to analyze?\n")
    upperChar = 0
    lowerChar = 0
    punctuationMarks = 0
    spaces = 0
    for c in text:
        if c.isupper():
            upperChar += 1
        if c.islower():
            lowerChar += 1
        if c.isspace():
            spaces += 1
        if c in string.punctuation:
            punctuationMarks += 1
    print(f"The text contains {len(text)} character(s):")
    print(f"- {upperChar} upper letter(s)\n- {lowerChar} lower letter(s)\n- {punctuationMarks} punctuation mark(s)\n- {spaces} space(s)")


if __name__ == '__main__':
    if (len(sys.argv) == 1):
        print("usage: python3 count.py <STRING>")
        exit()

    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument are provided")
        exit()

    text_analyzer(sys.argv[1])
