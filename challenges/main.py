def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower()
    # TODO: build a set of vowels actually found in `word`,

    # then check if it contains all of `required`
    found = set()

    for char in word:
        if char in required:
            found.add(char)
    return required.issubset(found)

    
print(has_all_vowels("education"))