# Problem: Given a list of (x, y, z) tuples, unpack each into x, y, z variables inside
#          a loop and return a list of separate (x, y, z) strings.
# Concept: Tuple unpacking directly in the for loop header.
# You are done when:
#   [ ] You unpack using "for x, y, z in points" not "for p in points: x = p[0]"
#   [ ] Each triple is formatted as a readable string
#   [ ] All test cases print PASS
# Hint: Python allows "for a, b, c in list_of_triples" to unpack each element immediately.


def unpack_and_format(points):
    """
    Return a list of strings formatted as "x={x}, y={y}, z={z}" for each point.
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]
    result = unpack_and_format(pts)
    expected = ["x=1.0, y=2.0, z=3.0", "x=4.0, y=5.0, z=6.0"]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
