# Problem: Rewrite Euclidean clustering replacing the inner brute-force loop with
#          KD-tree radius_search. Verify it produces same clusters as brute-force version.
# Concept: KD-tree clustering is O(N log N) vs O(N²) for brute force — this is the
#          actual algorithm used in production LiDAR pipelines for cone detection.
# You are done when:
#   [ ] The outer BFS loop structure is identical to your brute-force version
#   [ ] The only change is radius_search(root, query, epsilon) replaces a linear scan
#   [ ] Cluster sets match the brute-force reference exactly
#   [ ] All test cases print PASS
# Hint: Build the KD-tree once before the clustering loop; each BFS step calls radius_search.

import math
from collections import deque


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


def kdtree_clustering(points, epsilon=0.5, min_size=1):
    """
    Euclidean clustering using KD-tree radius search for the neighbour lookup.
    Return a list of clusters (each is a list of (x,y,z) tuples).
    """
    pass


def brute_clustering(points, epsilon, min_size):
    n = len(points)
    adj = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if math.sqrt(sum((points[i][k]-points[j][k])**2 for k in range(3))) < epsilon:
                adj[i].append(j); adj[j].append(i)
    visited = set(); clusters = []
    for i in range(n):
        if i in visited: continue
        comp = []; q = deque([i]); visited.add(i)
        while q:
            cur = q.popleft(); comp.append(points[cur])
            for nb in adj[cur]:
                if nb not in visited: visited.add(nb); q.append(nb)
        if len(comp) >= min_size: clusters.append(sorted(comp))
    return sorted(clusters)


if __name__ == "__main__":
    import random; random.seed(5)
    pts = ([(random.uniform(0,1), random.uniform(0,1), 0.0) for _ in range(20)] +
           [(random.uniform(5,6), random.uniform(5,6), 0.0) for _ in range(15)])

    kd_result = sorted([sorted(c) for c in kdtree_clustering(pts, epsilon=0.5, min_size=1)])
    bf_result = brute_clustering(pts, epsilon=0.5, min_size=1)
    print("PASS matches brute" if kd_result == bf_result else f"FAIL mismatch\n  kd: {len(kd_result)} clusters\n  bf: {len(bf_result)} clusters")
