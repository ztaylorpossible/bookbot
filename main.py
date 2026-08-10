import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    words = count_words(text)
    characters = count_characters(text)
    sorted_items = chars_dict_to_sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for i in range(0, len(sorted_items)):
        character = sorted_items[i]
        if (character[0].isalpha()):
            print(f"{character[0]}: {character[1]}")
    print("============= END ===============")

main()
