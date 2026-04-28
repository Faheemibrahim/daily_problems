# Problem: Write brute_force_nearest(query, points) as a reference implementation.
# Concept: The brute force O(N) linear scan is the correctness baseline for KD-tree search.
#          It is also the algorithm used in day08 — but here it exists explicitly for comparison.
# You are done when:
#   [ ] The function scans every point and returns the closest one
#   [ ] It handles a single-point list correctly
#   [ ] Results are identical to the KD-tree version for all inputs
#   [ ] All test cases print PASS
# Hint: Track (best_dist, best_point) and update when you find a strictly closer point.

import math


def brute_force_nearest(query, points):
    """
    Return the point in points closest to query by linear scan.
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 0.0, 0.0), (5.0, 0.0, 0.0), (2.5, 0.0, 0.0)]

    r = brute_force_nearest((2.3, 0.0, 0.0), pts)
    print("PASS" if r == (2.5, 0.0, 0.0) else f"FAIL — {r}")

    r2 = brute_force_nearest((0.0, 0.0, 0.0), [(3.0, 4.0, 0.0)])
    print("PASS single" if r2 == (3.0, 4.0, 0.0) else f"FAIL single — {r2}")
