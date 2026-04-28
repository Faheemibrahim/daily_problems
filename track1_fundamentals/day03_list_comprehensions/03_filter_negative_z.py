# Problem: Extract all points where z is negative using a single list comprehension.
# Concept: Filtering on a specific field of a tuple inside a comprehension.
# You are done when:
#   [ ] Only points with z < 0 appear in the result
#   [ ] Written as one comprehension line
#   [ ] All test cases print PASS
# Hint: Unpack (x, y, z) in the for clause so you can reference z directly in the condition.


def filter_negative_z(points):
    """
    Return a list of (x, y, z) tuples where z < 0.
    """
    pass


if __name__ == "__main__":
    pts = [
        (1.0, 2.0, -1.0),
        (1.0, 2.0, 3.0),
        (0.0, 0.0, -0.5),
        (4.0, 4.0, 0.0),
        (-1.0, -1.0, -2.0),
    ]
    result = filter_negative_z(pts)
    expected = [(1.0, 2.0, -1.0), (0.0, 0.0, -0.5), (-1.0, -1.0, -2.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
