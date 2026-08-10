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

def sort_on(items: tuple[str, int]) -> int:
    return items[1]

def chars_dict_to_sorted_list(items: dict[str, int]) -> list[tuple[str, int]]:
    tuples = []
    for key in items:
        tuples.append((key, items[key]))
    sorted_list = sorted(tuples, key=sort_on, reverse=True)
    return sorted_list
