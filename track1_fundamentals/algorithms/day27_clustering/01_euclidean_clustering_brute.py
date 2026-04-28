# Problem: Rewrite Euclidean clustering from scratch — brute force O(n²) version.
#          No reference allowed. Write it cold from memory.
# Concept: This is the algorithm test. If you can write it without looking anything up,
#          you understand it. Graph build + BFS component finding + min_size filter.
# You are done when:
#   [ ] You write the function without copying from any previous file
#   [ ] It produces correct clusters verified against a known reference
#   [ ] Function signature: euclidean_clustering(points, epsilon, min_size) -> list of lists
#   [ ] All test cases print PASS
# Hint: Build adjacency list -> find all components with BFS -> filter by size -> return point lists.

import math
from collections import deque


def euclidean_clustering(points, epsilon=0.5, min_size=1):
    """
    Cluster 3D points by connecting all pairs within epsilon distance.
    Return a list of clusters, each cluster being a list of (x, y, z) tuples.
    Only return clusters with >= min_size points.
    Write this entirely from scratch.
    """
    pass


if __name__ == "__main__":
    # Two clear clusters + one isolated point
    pts = (
        [(i * 0.1, 0.0, 0.0) for i in range(6)] +      # cluster A: 6 points near origin
        [(5.0 + i * 0.1, 0.0, 0.0) for i in range(4)] + # cluster B: 4 points near x=5
        [(20.0, 0.0, 0.0)]                                # isolated
    )
    result = euclidean_clustering(pts, epsilon=0.15, min_size=1)

    sizes = sorted(len(c) for c in result)
    print("PASS 3 clusters" if len(result) == 3 else f"FAIL num clusters — {len(result)}")
    print("PASS sizes" if sizes == [1, 4, 6] else f"FAIL sizes — {sizes}")

    result2 = euclidean_clustering(pts, epsilon=0.15, min_size=4)
    print("PASS min_size filter" if len(result2) == 2 else f"FAIL filter — {len(result2)}")
