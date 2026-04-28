# Problem: Rewrite your euclidean_clustering function completely from scratch using BFS.
#          Must produce identical results to a brute-force reference implementation.
# Concept: Writing an algorithm from scratch cold — without reference — is the test of
#          whether you truly understand it. If you get stuck, go back to day17 problems.
# You are done when:
#   [ ] You write the function from scratch without copying from previous files
#   [ ] Output matches the reference brute-force implementation on all test inputs
#   [ ] Function signature: euclidean_clustering(points, epsilon, min_size) -> list of lists
#   [ ] All test cases print PASS
# Hint: Build graph -> find all BFS components -> filter by min_size -> return point lists.

import math
from collections import deque


def euclidean_clustering(points, epsilon=0.5, min_size=1):
    """
    Group points into clusters where all points within a cluster are
    reachable from each other via hops of distance < epsilon.
    Return a list of clusters, each cluster being a list of (x, y, z) points.
    Only include clusters with >= min_size points.
    Write this completely from scratch.
    """
    pass


# Reference implementation for comparison
def _reference_clustering(points, epsilon, min_size):
    n = len(points)
    adj = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            d = math.sqrt(sum((points[i][k]-points[j][k])**2 for k in range(3)))
            if d < epsilon:
                adj[i].append(j); adj[j].append(i)
    visited = set()
    clusters = []
    for i in range(n):
        if i in visited:
            continue
        comp = []
        q = deque([i]); visited.add(i)
        while q:
            cur = q.popleft(); comp.append(cur)
            for nb in adj[cur]:
                if nb not in visited:
                    visited.add(nb); q.append(nb)
        if len(comp) >= min_size:
            clusters.append(sorted(comp))
    return sorted(clusters)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Deterministic test
    pts = (
        [(i*0.1, 0.0, 0.0) for i in range(6)] +
        [(5.0 + i*0.1, 0.0, 0.0) for i in range(4)] +
        [(20.0, 0.0, 0.0)]
    )
    my = euclidean_clustering(pts, epsilon=0.5, min_size=2)
    ref = _reference_clustering(pts, epsilon=0.5, min_size=2)

    my_sets = sorted([sorted(c) for c in [[pts.index(p) for p in cl] for cl in my]]) if my else []
    print("PASS matches reference" if my_sets == ref else f"FAIL\n  mine: {my_sets}\n  ref:  {ref}")
    print("PASS 2 clusters" if len(my) == 2 else f"FAIL num clusters — {len(my)}")
