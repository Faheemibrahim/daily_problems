# Problem: Write find_nearest(query, points) that returns the closest point using brute force.
# Concept: Linear scan to find a minimum — the naive nearest-neighbour search that
#          KD-trees later replace for large point clouds.
# You are done when:
#   [ ] You compute distance from query to every point in a loop
#   [ ] You track the current minimum and the corresponding point
#   [ ] You return the nearest point as a tuple (not its index)
#   [ ] All test cases print PASS
# Hint: Reuse distance() from problem 01 if you like, or inline the formula.

import math


def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)


def find_nearest(query, points):
    """
    Return the (x, y, z) point in points that is closest to query.
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 0.0, 0.0), (5.0, 0.0, 0.0), (2.0, 0.0, 0.0)]
    result = find_nearest((1.5, 0.0, 0.0), pts)
    print("PASS" if result == (1.0, 0.0, 0.0) else f"FAIL — got {result}")

    result2 = find_nearest((4.9, 0.0, 0.0), pts)
    print("PASS" if result2 == (5.0, 0.0, 0.0) else f"FAIL — got {result2}")
