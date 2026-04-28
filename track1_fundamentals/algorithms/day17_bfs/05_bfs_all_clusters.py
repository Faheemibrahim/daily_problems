# Problem: Find ALL clusters by running BFS from every unvisited point.
#          This is Euclidean clustering implemented with BFS.
# Concept: The outer loop seeds BFS from each unvisited node. When BFS finishes,
#          all found indices are marked visited so the outer loop skips them.
#          Repeat until every node has been assigned to a cluster.
# You are done when:
#   [ ] Every point ends up in exactly one cluster
#   [ ] Clusters are lists of point indices
#   [ ] The number of clusters equals the number of connected components
#   [ ] All test cases print PASS
# Hint: Maintain a global visited set; only start BFS if the current node is not in it.

import math
from collections import deque


def build_point_graph(points, epsilon):
    g = {i: [] for i in range(len(points))}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.sqrt(sum((points[i][k]-points[j][k])**2 for k in range(3)))
            if d < epsilon:
                g[i].append(j)
                g[j].append(i)
    return g


def bfs_all_clusters(graph):
    """
    Return a list of clusters, where each cluster is a sorted list of node indices.
    """
    pass


if __name__ == "__main__":
    pts = [
        (0.0, 0.0, 0.0), (0.1, 0.0, 0.0), (0.2, 0.0, 0.0),
        (5.0, 5.0, 0.0), (5.1, 5.0, 0.0),
        (10.0, 10.0, 0.0),  # isolated
    ]
    g = build_point_graph(pts, epsilon=0.5)
    clusters = bfs_all_clusters(g)

    sizes = sorted(len(c) for c in clusters)
    print("PASS num clusters" if len(clusters) == 3 else f"FAIL num clusters — {len(clusters)}")
    print("PASS cluster sizes" if sizes == [1, 2, 3] else f"FAIL sizes — {sizes}")

    all_indices = sorted(idx for cl in clusters for idx in cl)
    print("PASS all covered" if all_indices == list(range(len(pts))) else f"FAIL coverage — {all_indices}")
