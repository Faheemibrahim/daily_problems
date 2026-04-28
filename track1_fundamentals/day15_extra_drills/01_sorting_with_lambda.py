# Problem: Given a list of (x, y, z) points, produce three sorted versions:
#          (1) by x ascending, (2) by distance from origin, (3) by z descending.
#          All three sorts must use sorted() with a lambda key — no manual loops.
# Concept: Lambda functions as sort keys let you express any ordering in one line.
#          This pattern replaces custom comparators for spatial data in every algorithm.
# You are done when:
#   [ ] sort_by_x returns points ordered by x from smallest to largest
#   [ ] sort_by_distance returns points ordered by Euclidean distance from origin
#   [ ] sort_by_z_desc returns points ordered by z from largest to smallest
#   [ ] All three use sorted() with a lambda key — no manual loops
#   [ ] All test cases print PASS
# Hint: sorted(items, key=lambda item: some_expression, reverse=False)


import math


def sort_by_x(points):
    """Return points sorted by x value ascending."""
    pass


def sort_by_distance(points):
    """Return points sorted by Euclidean distance from origin ascending."""
    pass


def sort_by_z_desc(points):
    """Return points sorted by z value descending."""
    pass


if __name__ == "__main__":
    pts = [
        (3.0, 0.0, 1.0),
        (1.0, 0.0, 3.0),
        (2.0, 0.0, 2.0),
        (0.0, 0.0, 4.0),
    ]

    result_x = sort_by_x(pts)
    expected_x = [(0.0, 0.0, 4.0), (1.0, 0.0, 3.0), (2.0, 0.0, 2.0), (3.0, 0.0, 1.0)]
    print("PASS sort_by_x" if result_x == expected_x else f"FAIL sort_by_x — {result_x}")

    result_d = sort_by_distance(pts)
    dists = [math.sqrt(x**2 + y**2 + z**2) for x, y, z in result_d]
    sorted_ok = all(dists[i] <= dists[i+1] for i in range(len(dists)-1))
    print("PASS sort_by_distance" if sorted_ok else f"FAIL sort_by_distance — dists {dists}")

    result_z = sort_by_z_desc(pts)
    expected_z = [(0.0, 0.0, 4.0), (1.0, 0.0, 3.0), (2.0, 0.0, 2.0), (3.0, 0.0, 1.0)]
    print("PASS sort_by_z_desc" if result_z == expected_z else f"FAIL sort_by_z_desc — {result_z}")
