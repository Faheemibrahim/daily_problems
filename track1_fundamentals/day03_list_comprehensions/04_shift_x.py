# Problem: Create a new list where every point is shifted by adding 1.0 to x, using a comprehension.
# Concept: Transforming each element of a list into a new element inside a comprehension.
# You are done when:
#   [ ] Every output point has x increased by exactly 1.0
#   [ ] y and z are unchanged
#   [ ] Written as one comprehension line
#   [ ] All test cases print PASS
# Hint: The expression part of a comprehension can construct a new tuple: (x+1.0, y, z)


def shift_x(points, delta=1.0):
    """
    Return a new list of tuples where each x has delta added to it.
    """
    pass


if __name__ == "__main__":
    pts = [(0.0, 1.0, 2.0), (3.0, 4.0, 5.0), (-1.0, 0.0, 0.0)]
    result = shift_x(pts)
    expected = [(1.0, 1.0, 2.0), (4.0, 4.0, 5.0), (0.0, 0.0, 0.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    result2 = shift_x(pts, delta=2.0)
    expected2 = [(2.0, 1.0, 2.0), (5.0, 4.0, 5.0), (1.0, 0.0, 0.0)]
    print("PASS" if result2 == expected2 else f"FAIL — got {result2}, expected {expected2}")
