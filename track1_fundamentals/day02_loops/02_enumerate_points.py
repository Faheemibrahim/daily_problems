# Problem: Loop through a list of points using enumerate() and produce "point 0: (x, y, z)" for each.
# Concept: enumerate() gives you both index and value in a single loop variable.
# You are done when:
#   [ ] You use enumerate() — not a manual counter variable
#   [ ] Each string is formatted as "point {i}: {point}"
#   [ ] All test cases print PASS
# Hint: enumerate(iterable) yields (index, element) pairs you can unpack directly in the for line.


def enumerate_points(points):
    """
    Return a list of strings formatted as "point {i}: {(x, y, z)}" for each point.
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]
    result = enumerate_points(pts)
    expected = [
        "point 0: (1.0, 0.0, 0.0)",
        "point 1: (0.0, 1.0, 0.0)",
        "point 2: (0.0, 0.0, 1.0)",
    ]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
