# Problem: Rewrite day02 problem 03 (filter points where x > 0) as a single list comprehension.
# Concept: List comprehension syntax with an if-condition replaces a loop + append pattern.
# You are done when:
#   [ ] The entire filter is written as one list comprehension on one line
#   [ ] You use no explicit for loop or append()
#   [ ] The output matches the loop version from day02
#   [ ] All test cases print PASS
# Hint: [expr for item in iterable if condition] is the full three-part comprehension form.


def filter_positive_x(points):
    """
    Return a new list of points where x > 0, using a list comprehension.
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
