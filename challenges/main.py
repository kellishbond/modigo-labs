def dedupe_preserve_order(items):
    # TODO: use a set to track seen values while building a new list
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    # that preserves the original order of first appearances
    return result

print(dedupe_preserve_order([3, 1, 3, 2, 1]))