from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    words = count_words(text)
    characters = count_characters(text)
    print(words)
    print(characters)

main()