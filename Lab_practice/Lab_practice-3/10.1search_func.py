import re

def search_word(text, word):
    pattern = rf"\b{re.escape(word)}\b"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        print(f"'{word}' found in the text!")
    else:
        print(f"'{word}' not found in the text.")

text = "Python is a powerful programming language."
word = input("Enter a word to search: ")
search_word(text, word)
