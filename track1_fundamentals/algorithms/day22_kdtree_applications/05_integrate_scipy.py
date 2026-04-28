# Problem: Integrate scipy KDTree into the full clustering pipeline. Measure the
#          performance difference on a large simulated point cloud.
# Concept: Replacing the inner brute-force search with scipy KDTree is the last step
#          in making clustering production-ready. Measure and document the improvement.
# You are done when:
#   [ ] The pipeline runs end-to-end: build tree, cluster with radius search, filter
#   [ ] You time brute-force clustering vs scipy-KDTree clustering on N=5000 points
#   [ ] The speedup is printed and confirmed with PASS/FAIL
#   [ ] All test cases print PASS
# Hint: Build the scipy KDTree once before the clustering loop, then call query_ball_point
#       inside the BFS instead of the inner brute-force loop.

import math
import time
import random
import numpy as np
from scipy.spatial import KDTree
from collections import deque


def scipy_kdtree_clustering(points, epsilon=0.5, min_size=1):
    """
    Euclidean clustering using scipy KDTree.query_ball_point for neighbour lookup.
    """
    pass


def brute_clustering(points, epsilon, min_size):
    n = len(points)
    visited = set(); clusters = []
    for i in range(n):
        if i in visited: continue
        comp = []; q = deque([i]); visited.add(i)
        while q:
            cur = q.popleft(); comp.append(points[cur])
            for j in range(n):
                if j not in visited and math.sqrt(sum((points[cur][k]-points[j][k])**2 for k in range(3))) < epsilon:
                    visited.add(j); q.append(j)
        if len(comp) >= min_size: clusters.append(comp)
    return clusters


if __name__ == "__main__":
    random.seed(42)
    N = 2000  # use 2000 so brute force finishes in reasonable time
    pts = ([(random.uniform(0,2), random.uniform(0,2), 0.0) for _ in range(N//2)] +
           [(random.uniform(5,7), random.uniform(5,7), 0.0) for _ in range(N//2)])

    t0 = time.time()
    bf = brute_clustering(pts, epsilon=0.5, min_size=5)
    bf_time = time.time() - t0

    t0 = time.time()
    kd = scipy_kdtree_clustering(pts, epsilon=0.5, min_size=5)
    kd_time = time.time() - t0

    ratio = bf_time / kd_time if kd_time > 0 else float("inf")
    print(f"Brute: {bf_time:.3f}s | SciPy KD: {kd_time:.3f}s | Speedup: {ratio:.1f}x")
    print("PASS faster" if kd_time < bf_time else "FAIL — scipy not faster")
    print("PASS same num clusters" if len(bf) == len(kd) else f"FAIL cluster count bf={len(bf)} kd={len(kd)}")
