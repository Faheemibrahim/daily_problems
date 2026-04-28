# Problem: Loop through a list of (x, y, z) points and collect only those where x > 0
#          into a new list. Use a regular for loop — no list comprehension.
# Concept: Conditional filtering inside a loop, building a result list incrementally.
# You are done when:
#   [ ] You use a plain for loop (no comprehension, no filter())
#   [ ] You correctly include only points where x is strictly greater than 0
#   [ ] You do not modify the original list
#   [ ] All test cases print PASS
# Hint: Create an empty list before the loop and append to it inside an if block.


def filter_positive_x(points):
    """
    Return a new list containing only the points where x > 0.
    Use a plain for loop.
    """
    pass


if __name__ == "__main__":
    pts = [
        (1.0, 2.0, 3.0),
        (-1.0, 2.0, 3.0),
        (0.0, 1.0, 1.0),
        (5.0, -1.0, 0.0),
        (-3.0, 0.0, 0.0),
    ]
    result = filter_positive_x(pts)
    expected = [(1.0, 2.0, 3.0), (5.0, -1.0, 0.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    pts2 = [(-1.0, 0.0, 0.0), (-2.0, 0.0, 0.0)]
    result2 = filter_positive_x(pts2)
    expected2 = []
    print("PASS" if result2 == expected2 else f"FAIL — got {result2}, expected {expected2}")
