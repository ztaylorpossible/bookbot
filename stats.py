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