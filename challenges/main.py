def same_point(point1, point2):
    # TODO: return True if point1 and point2 represent the same location
    return point1 == point2

print(same_point((1, 2), (1, 2)))
print(same_point((1, 2), (2, 1)))
print(same_point((0, 0), (0, 0)))