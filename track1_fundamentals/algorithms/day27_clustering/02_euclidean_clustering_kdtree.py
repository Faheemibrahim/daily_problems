# Problem: Rewrite Euclidean clustering using KD-tree radius search for the inner lookup.
# Concept: Replacing the O(n) inner scan with O(log n) KD-tree radius search makes the
#          full algorithm O(n log n) instead of O(n²). This is the production version.
# You are done when:
#   [ ] You build the KD-tree once before the clustering loop
#   [ ] Each BFS step calls radius_search instead of a linear scan
#   [ ] Results match the brute-force version exactly
#   [ ] All test cases print PASS
# Hint: Build tree on all points; BFS uses radius_search(root, points[i], epsilon) to find neighbours.

import math
from collections import deque


class KDNode:
    def __init__(self, point, idx, axis, left=None, right=None):
        self.point, self.idx, self.axis, self.left, self.right = point, idx, axis, left, right


def build_kdtree(indexed_points, depth=0):
    """Build KD-tree from list of (point, original_index) tuples."""
    if not indexed_points: return None
    axis = depth % 3
    indexed_points = sorted(indexed_points, key=lambda ip: ip[0][axis])
    mid = len(indexed_points) // 2
    pt, idx = indexed_points[mid]
    return KDNode(pt, idx, axis,
                  build_kdtree(indexed_points[:mid], depth+1),
                  build_kdtree(indexed_points[mid+1:], depth+1))


def radius_search_indices(root, query, radius):
    """Return list of original indices of points within radius of query."""
    pass


def euclidean_clustering_kdtree(points, epsilon=0.5, min_size=1):
    """
    Euclidean clustering using KD-tree radius search.
    Return list of clusters (each a list of (x,y,z) tuples).
    """
    pass


if __name__ == "__main__":
    pts = (
        [(i * 0.1, 0.0, 0.0) for i in range(6)] +
        [(5.0 + i * 0.1, 0.0, 0.0) for i in range(4)] +
        [(20.0, 0.0, 0.0)]
    )
    result = euclidean_clustering_kdtree(pts, epsilon=0.15, min_size=1)
    sizes = sorted(len(c) for c in result)
    print("PASS 3 clusters" if len(result) == 3 else f"FAIL — {len(result)}")
    print("PASS sizes" if sizes == [1, 4, 6] else f"FAIL sizes — {sizes}")
