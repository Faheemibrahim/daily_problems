# Problem: Given a list of (x, y, z) points, find the point with the largest x value
#          using a loop and a tracking variable. No built-ins like max().
# Concept: Manual iteration, tracking a running maximum with a variable.
# You are done when:
#   [ ] You loop through the list without using max() or sorted()
#   [ ] You keep a variable that stores the current best point
#   [ ] You correctly update it when you find a larger x
#   [ ] All test cases print PASS
# Hint: Start your tracking variable with the first element, then compare each subsequent element.


def largest_x(points):
    """
    Return the (x, y, z) tuple that has the largest x value.
    Use a loop and a tracking variable — no built-in max().
    """
    pass


if __name__ == "__main__":
    pts = [
        (3.0, 1.0, 0.0),
        (7.0, 2.0, 1.0),
        (1.0, 5.0, 2.0),
        (9.5, 0.0, 0.0),
        (4.0, 4.0, 4.0),
    ]
    result = largest_x(pts)
    expected = (9.5, 0.0, 0.0)
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    pts2 = [(0.0, 0.0, 0.0), (-1.0, 1.0, 1.0), (0.5, 0.0, 0.0)]
    result2 = largest_x(pts2)
    expected2 = (0.5, 0.0, 0.0)
    print("PASS" if result2 == expected2 else f"FAIL — got {result2}, expected {expected2}")
