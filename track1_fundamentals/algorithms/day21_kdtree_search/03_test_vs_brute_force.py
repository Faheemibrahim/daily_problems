# Problem: Test nearest_neighbour against brute_force_nearest on 500 random points
#          with 50 different queries. All results must match exactly.
# Concept: Systematic correctness testing against a known-correct reference is how
#          you verify a complex algorithm. One mismatch reveals a bug in the backtracking.
# You are done when:
#   [ ] All 50 query results match between KD-tree and brute force
#   [ ] You print a single PASS or a detailed FAIL showing the mismatching query
#   [ ] All test cases print PASS
# Hint: If you get mismatches, the bug is almost always in the plane-distance check during backtracking.

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


def nearest_neighbour(root, query):
    """Paste your solution from problem 01 here."""
    pass


def brute_force_nearest(query, points):
    return min(points, key=lambda p: math.sqrt(sum((p[i]-query[i])**2 for i in range(3))))


if __name__ == "__main__":
    random.seed(42)
    pts = [(random.uniform(-10,10), random.uniform(-10,10), random.uniform(-10,10)) for _ in range(500)]
    root = build_kdtree(pts)
    queries = [(random.uniform(-10,10), random.uniform(-10,10), random.uniform(-10,10)) for _ in range(50)]

    mismatches = 0
    for q in queries:
        kd = nearest_neighbour(root, q)
        bf = brute_force_nearest(q, pts)
        if kd != bf:
            mismatches += 1
            print(f"MISMATCH q={q}\n  kd={kd}\n  bf={bf}")

    print(f"PASS all 50 queries match" if mismatches == 0 else f"FAIL {mismatches}/50 mismatched")
