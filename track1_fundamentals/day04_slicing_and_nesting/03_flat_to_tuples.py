# Problem: Given a flat list [x1, y1, z1, x2, y2, z2, ...] convert it into
#          [(x1, y1, z1), (x2, y2, z2), ...] using a loop.
# Concept: Grouping flat data into structured chunks by stepping through indices.
# You are done when:
#   [ ] You consume the flat list in groups of 3
#   [ ] Each group becomes a tuple
#   [ ] You use a loop (not zip or slicing tricks)
#   [ ] All test cases print PASS
# Hint: Loop with range(0, len(flat), 3) to step through in groups of three.


def flat_to_tuples(flat):
    """
    Convert a flat list of floats (length divisible by 3) into a list of (x, y, z) tuples.
    """
    pass


if __name__ == "__main__":
    flat = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    result = flat_to_tuples(flat)
    expected = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    flat2 = [0.0, 0.0, 0.0]
    result2 = flat_to_tuples(flat2)
    expected2 = [(0.0, 0.0, 0.0)]
    print("PASS" if result2 == expected2 else f"FAIL — got {result2}, expected {expected2}")
