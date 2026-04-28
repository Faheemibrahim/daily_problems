# Problem: Write distance(p1, p2) that returns the Euclidean distance between two 3D points.
# Concept: Functions as reusable named computations — this exact function will be called
#          inside clustering, KD-tree search, and nearest-neighbour queries.
# You are done when:
#   [ ] The function accepts two (x, y, z) tuples
#   [ ] It returns a float (the Euclidean distance)
#   [ ] It handles the case where p1 == p2 (returns 0.0)
#   [ ] All test cases print PASS
# Hint: math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

import math


def distance(p1, p2):
    """
    Return the Euclidean distance between two 3D points p1 and p2.
    Each point is a (x, y, z) tuple.
    """
    pass


if __name__ == "__main__":
    print("PASS" if distance((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)) == 1.0 else "FAIL unit x")
    print("PASS" if distance((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)) == 0.0 else "FAIL same point")
    d = distance((1.0, 2.0, 3.0), (4.0, 6.0, 3.0))
    print("PASS" if abs(d - 5.0) < 1e-9 else f"FAIL 3-4-5 — got {d}")
