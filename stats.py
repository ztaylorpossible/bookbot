def count_words(text):
    words = text.split()
    count = len(words)
    return f"Found {count} total words"

def count_characters(text):
    characters = {}
    for character in text:
        lower = character.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters

def sorted_characters(char_dict):
    characters = []
    for key in char_dict:
        new_dict = {"char": key, "num": char_dict[key]}
        characters.append(new_dict)
    characters.sort(reverse=True, key=sort_on)
    return characters

def sort_on(items):
    return items["num"]