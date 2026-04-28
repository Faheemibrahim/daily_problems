# Problem: Given a point cloud graph (from day16 problem 05), use BFS to find all points
#          reachable from a starting point index — this is one cluster.
# Concept: One BFS starting from an unvisited seed point identifies exactly one cluster.
#          The visited set prevents double-counting; the output is a list of point indices.
# You are done when:
#   [ ] You use the point cloud graph (nodes are indices)
#   [ ] BFS returns all indices in the same connected component as start_idx
#   [ ] Points in other components are not included
#   [ ] All test cases print PASS
# Hint: Same BFS as problem 01 but on the integer-indexed point graph.

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


def bfs_cluster(graph, start_idx):
    """
    Return a sorted list of all node indices reachable from start_idx using BFS.
    """
    pass


if __name__ == "__main__":
    pts = [
        (0.0, 0.0, 0.0), (0.1, 0.0, 0.0), (0.2, 0.0, 0.0),  # cluster 0: indices 0,1,2
        (5.0, 5.0, 0.0), (5.1, 5.0, 0.0),                    # cluster 1: indices 3,4
    ]
    g = build_point_graph(pts, epsilon=0.5)
    cluster0 = bfs_cluster(g, 0)
    cluster1 = bfs_cluster(g, 3)

    print("PASS cluster0" if set(cluster0) == {0, 1, 2} else f"FAIL cluster0 — {cluster0}")
    print("PASS cluster1" if set(cluster1) == {3, 4} else f"FAIL cluster1 — {cluster1}")
