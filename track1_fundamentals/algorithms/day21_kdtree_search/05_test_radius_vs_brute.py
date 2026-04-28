# Problem: Write brute_force_radius and test it against radius_search on 500 points.
#          All results must match exactly (as sets) for all queries.
# Concept: Same systematic correctness test as problem 03 but for radius search.
#          A radius search bug often manifests only for queries near splitting planes.
# You are done when:
#   [ ] All 50 radius queries return identical point sets from both methods
#   [ ] All test cases print PASS
# Hint: brute_force_radius is just a list comprehension — no tree needed.

import math
import random


class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point, self.axis, self.left, self.right = point, axis, left, right


def build_kdtree(points, depth=0):
    if not points: return None
    axis = depth % 3
    pts = sorted(points, key=lambda p: p[axis])
    mid = len(pts) // 2
    return KDNode(pts[mid], axis, build_kdtree(pts[:mid], depth+1), build_kdtree(pts[mid+1:], depth+1))


def radius_search(root, query, radius):
    """Paste your solution from problem 04 here."""
    pass


def brute_force_radius(query, points, radius):
    """Return all points within radius of query by linear scan."""
    pass


if __name__ == "__main__":
    random.seed(7)
    pts = [(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(500)]
    root = build_kdtree(pts)
    queries = [(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(50)]
    radius = 1.0

    mismatches = 0
    for q in queries:
        kd = set(radius_search(root, q, radius))
        bf = set(brute_force_radius(q, pts, radius))
        if kd != bf:
            mismatches += 1
            print(f"MISMATCH q={q}: kd has {len(kd)}, bf has {len(bf)}")
            print(f"  in bf not kd: {bf - kd}")
            print(f"  in kd not bf: {kd - bf}")

    print(f"PASS all 50 match" if mismatches == 0 else f"FAIL {mismatches}/50 mismatched")
