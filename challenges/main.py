def word_lengths(words):
    lengths = {}
    # TODO: loop through `words` and populate `lengths` with word -> length of word
    for word in words:
        if word not in lengths:
            lengths[word] = len(word)

    return lengths

print(word_lengths(["cat", "elephant", "ox"]))
print(word_lengths([]))
print(word_lengths(["hi", "hi"]))