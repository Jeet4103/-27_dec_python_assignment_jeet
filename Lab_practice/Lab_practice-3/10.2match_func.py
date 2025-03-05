import re

def match_word(text, word):
    pattern = rf"^{re.escape(word)}\b"
    match = re.match(pattern, text, re.IGNORECASE)
    if match:
        print(f"'{word}' is at the beginning of the text!")
    else:
        print(f"'{word}' is not at the beginning of the text.")

text = "Python is a powerful programming language."
word = input("Enter a word to match: ")
match_word(text, word)
