# Problem: Given a list of 3D points and epsilon=0.5, build the graph and find all
#          clusters using BFS. Filter out clusters smaller than 3 points.
# Concept: This is Euclidean clustering end-to-end: graph construction + BFS traversal
#          + size filtering. The output is the raw cluster list used in detection pipelines.
# You are done when:
#   [ ] You build the point graph correctly (edges where distance < epsilon)
#   [ ] You find all connected components using BFS
#   [ ] You filter out clusters with fewer than min_size points
#   [ ] All test cases print PASS
# Hint: Reuse build_point_graph from day16 and bfs_all_clusters from day17.

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


def euclidean_cluster_bfs(points, epsilon=0.5, min_size=3):
    """
    Return a list of clusters. Each cluster is a list of (x, y, z) points.
    Only clusters with >= min_size points are returned.
    """
    pass


if __name__ == "__main__":
    pts = (
        [(0.0 + i*0.1, 0.0, 0.0) for i in range(5)] +   # 5-point cluster near origin
        [(5.0 + i*0.1, 0.0, 0.0) for i in range(2)] +   # 2-point cluster (filtered out)
        [(10.0, 0.0, 0.0)]                                 # isolated
    )
    result = euclidean_cluster_bfs(pts, epsilon=0.5, min_size=3)

    print("PASS num clusters" if len(result) == 1 else f"FAIL num — {len(result)}")
    print("PASS cluster size" if len(result[0]) == 5 else f"FAIL size — {len(result[0])}")
