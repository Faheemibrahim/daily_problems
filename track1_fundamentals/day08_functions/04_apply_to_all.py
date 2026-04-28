# Problem: Write apply_to_all(points, func) that takes a function as an argument
#          and applies it to every point, returning the list of results.
# Concept: Functions as first-class objects — passing a function as an argument
#          is the basis of map(), callbacks, and higher-order operations.
# You are done when:
#   [ ] apply_to_all accepts any callable as its second argument
#   [ ] It returns a list with func applied to each element
#   [ ] It works with a lambda, a named function, and a built-in
#   [ ] All test cases print PASS
# Hint: This is the manual version of Python's built-in map(func, points).


def apply_to_all(points, func):
    """
    Apply func to every element in points and return the results as a list.
    """
    pass


if __name__ == "__main__":
    import math

    pts = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (3.0, 4.0, 0.0)]
    origin = (0.0, 0.0, 0.0)

    def dist_from_origin(p):
        return math.sqrt(p[0]**2 + p[1]**2 + p[2]**2)

    result = apply_to_all(pts, dist_from_origin)
    expected = [0.0, 1.0, 5.0]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    result2 = apply_to_all([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)], lambda p: p[0])
    print("PASS lambda" if result2 == [1.0, 4.0] else f"FAIL lambda — got {result2}")
