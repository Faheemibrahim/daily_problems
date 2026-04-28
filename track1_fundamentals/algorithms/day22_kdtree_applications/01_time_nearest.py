# Problem: Time brute force nearest vs KD-tree nearest on 10000 points — run 100 queries.
#          Print both times and the speedup ratio.
# Concept: Measuring algorithmic speedup experimentally anchors the theory. You should
#          see roughly 10-100x speedup depending on N and query distribution.
# You are done when:
#   [ ] You time exactly 100 queries against each method
#   [ ] KD-tree is faster (print PASS) or you diagnose why it isn't
#   [ ] All test cases print PASS
# Hint: time.time() before and after the 100-query loop gives wall-clock time.

import math
import random
import time


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
    """Paste your solution from day21 problem 01 here."""
    pass


def brute_force_nearest(query, points):
    return min(points, key=lambda p: math.sqrt(sum((p[i]-query[i])**2 for i in range(3))))


if __name__ == "__main__":
    random.seed(0)
    N = 10_000
    pts = [(random.uniform(-50,50), random.uniform(-50,50), random.uniform(-50,50)) for _ in range(N)]
    queries = [(random.uniform(-50,50), random.uniform(-50,50), random.uniform(-50,50)) for _ in range(100)]

    root = build_kdtree(pts)

    t0 = time.time()
    for q in queries: brute_force_nearest(q, pts)
    bf_time = time.time() - t0

    t0 = time.time()
    for q in queries: nearest_neighbour(root, q)
    kd_time = time.time() - t0

    ratio = bf_time / kd_time if kd_time > 0 else float("inf")
    print(f"Brute force: {bf_time:.3f}s | KD-tree: {kd_time:.4f}s | Speedup: {ratio:.1f}x")
    print("PASS KD faster" if kd_time < bf_time else "FAIL — KD-tree was not faster (check your implementation)")
