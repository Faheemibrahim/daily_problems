# Problem: Extract all x values from a list of (x, y, z) tuples in a single list comprehension.
# Concept: Using tuple unpacking or indexing inside a comprehension to project one field.
# You are done when:
#   [ ] The result is a flat list of numbers, not tuples
#   [ ] You write it in one line as a comprehension
#   [ ] All test cases print PASS
# Hint: You can unpack directly in the for clause: [x for x, y, z in points]


def extract_x(points):
    """
    Return a list of x values (floats) from a list of (x, y, z) tuples.
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    result = extract_x(pts)
    expected = [1.0, 4.0, 7.0]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
