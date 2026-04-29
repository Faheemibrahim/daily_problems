# Problem: Loop through a list of (x, y, z) points and print each one on its own line.
# Concept: Basic for loop over a list, printing structured data.
# You are done when:
#   [ ] You loop through every point without skipping any
#   [ ] Each point is printed on its own line
#   [ ] The function returns a list of the string representations for testing
#   [ ] All test cases print PASS
# Hint: A for loop variable takes on each element of the list in sequence.


def points_to_lines(points):
    """
    Return a list of strings, one per point, formatted as "(x, y, z)".
    The caller can print them; this function returns the strings for testing.
    """
    # for point in points:
    #     for i in point:
    #         print(i)
    # return i

    store = [] 
    for point in points:
        print(point)
        store.append(str(point))
    return store 


if __name__ == "__main__":
    pts = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    result = points_to_lines(pts)
    expected = ["(1.0, 2.0, 3.0)", "(4.0, 5.0, 6.0)", "(7.0, 8.0, 9.0)"]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
