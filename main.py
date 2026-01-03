from stats import count_words, count_characters, sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = count_words(text)
    characters = count_characters(text)
    sorted = sorted_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for i in range(0, len(sorted)):
        character = sorted[i]
        if (character["char"].isalpha()):
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()