# Problem: Filter points that are within distance 3.0 from the origin, computing the
#          distance inside the comprehension itself.
# Concept: Embedding an expression (distance formula) directly in the comprehension condition.
# You are done when:
#   [ ] Distance from origin is computed inline, not in a separate function call
#   [ ] Only points with distance < 3.0 are included
#   [ ] Written as one comprehension
#   [ ] All test cases print PASS
# Hint: You can write math.sqrt(x**2 + y**2 + z**2) directly in the if clause.

import math


def filter_within_distance(points, radius=3.0):
    """
    Return points whose Euclidean distance from the origin is less than radius.
    """
    store = [point for point in points if math.sqrt(point[0]**2 + point[1]**2 + point[2]**2) < radius]

    return store 


if __name__ == "__main__":
    pts = [
        (0.0, 0.0, 0.0),
        (1.0, 1.0, 1.0),
        (2.0, 2.0, 0.0),
        (3.0, 0.0, 0.0),
        (0.0, 4.0, 0.0),
    ]
    result = filter_within_distance(pts)
    expected = [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0), (2.0, 2.0, 0.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
