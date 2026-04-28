# Problem: Time brute force radius search vs KD-tree radius search on 10000 points.
#          Run 100 queries with radius=1.0. Print both times and speedup ratio.
# Concept: Radius search speedup is more variable than nearest-neighbour because it
#          depends on how many points fall within the radius. Sparse queries are fast;
#          dense queries force more backtracking.
# You are done when:
#   [ ] You time 100 radius queries for each method
#   [ ] KD-tree is faster (or you document why it isn't for this radius)
#   [ ] All test cases print PASS
# Hint: Use the same timing pattern as problem 01.

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


def radius_search(root, query, radius):
    """Paste your solution from day21 problem 04 here."""
    pass


def brute_force_radius(query, points, radius):
    return [p for p in points if math.sqrt(sum((p[i]-query[i])**2 for i in range(3))) <= radius]


if __name__ == "__main__":
    random.seed(1)
    N = 10_000
    RADIUS = 1.0
    pts = [(random.uniform(-50,50), random.uniform(-50,50), random.uniform(-50,50)) for _ in range(N)]
    queries = [(random.uniform(-50,50), random.uniform(-50,50), random.uniform(-50,50)) for _ in range(100)]
    root = build_kdtree(pts)

    t0 = time.time()
    for q in queries: brute_force_radius(q, pts, RADIUS)
    bf_time = time.time() - t0

    t0 = time.time()
    for q in queries: radius_search(root, q, RADIUS)
    kd_time = time.time() - t0

    ratio = bf_time / kd_time if kd_time > 0 else float("inf")
    print(f"Brute force: {bf_time:.3f}s | KD-tree: {kd_time:.4f}s | Speedup: {ratio:.1f}x")
    print("PASS KD faster" if kd_time < bf_time else "FAIL — KD not faster (check implementation)")
