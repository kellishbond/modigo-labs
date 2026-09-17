def count_unique_coordinates(coordinates):
    unique = []
    for coord in coordinates:
        unique.append(coord)
    return len(set(unique))


print(count_unique_coordinates([(0,0), (1,0), (0,1)]))