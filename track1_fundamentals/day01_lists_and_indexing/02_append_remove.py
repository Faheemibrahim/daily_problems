# Problem: Append a new point to a list of (x, y, z) tuples, then remove the 2nd point, and return the result.
# Concept: Mutating lists with append() and pop()/del/remove().
# You are done when:
#   [ ] You appended a new point to the end of the list
#   [ ] You removed the element at index 1 (the 2nd point)
#   [ ] The returned list has length original + 1 - 1 = original
#   [ ] All test cases print PASS
# Hint: Lists are mutable — append() and del both modify the list in place.


def append_and_remove(points, new_point):
    """
    Append new_point to points, then remove the element at index 1.
    Return the modified list.
    """
    pass


if __name__ == "__main__":
    pts = [
        (1.0, 0.0, 0.0),
        (2.0, 0.0, 0.0),
        (3.0, 0.0, 0.0),
        (4.0, 0.0, 0.0),
    ]
    new = (9.0, 9.0, 9.0)
    result = append_and_remove(pts, new)
    expected = [(1.0, 0.0, 0.0), (3.0, 0.0, 0.0), (4.0, 0.0, 0.0), (9.0, 9.0, 9.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
