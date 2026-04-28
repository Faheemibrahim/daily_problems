# Problem: Create a list of 8 (x, y, z) tuples manually, then access the 1st, 3rd, and last element.
# Concept: List creation and indexing with positive and negative indices.
# You are done when:
#   [ ] You built a list of exactly 8 (x, y, z) tuples
#   [ ] You accessed the 1st element using index 0
#   [ ] You accessed the 3rd element using index 2
#   [ ] You accessed the last element using a negative index
#   [ ] All test cases print PASS
# Hint: Python lists are zero-indexed; index -1 refers to the last element.


def access_elements(points):
    """
    Given a list of (x, y, z) tuples, return a tuple of
    (first_element, third_element, last_element).
    """
    pass


if __name__ == "__main__":
    pts = [
        (1.0, 2.0, 3.0),
        (4.0, 5.0, 6.0),
        (7.0, 8.0, 9.0),
        (10.0, 11.0, 12.0),
        (13.0, 14.0, 15.0),
        (16.0, 17.0, 18.0),
        (19.0, 20.0, 21.0),
        (22.0, 23.0, 24.0),
    ]

    result = access_elements(pts)
    expected = ((1.0, 2.0, 3.0), (7.0, 8.0, 9.0), (22.0, 23.0, 24.0))
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
