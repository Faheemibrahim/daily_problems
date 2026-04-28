# Problem: Given two clusters, find the shortest path (in hops) between their closest
#          point pair using BFS on the full point graph.
# Concept: Shortest path between cluster representatives — a building block for
#          hierarchical clustering and motion planning between detected objects.
# You are done when:
#   [ ] You identify the closest pair of points (one from each cluster) by brute force
#   [ ] You use BFS to find the path between those two point indices
#   [ ] The returned path is a list of point indices
#   [ ] All test cases print PASS
# Hint: Find closest pair first (O(n*m)), then run bfs_shortest_path between those indices.

import math
from collections import deque


def bfs_shortest_path(graph, start, target):
    if start == target:
        return [start]
    visited = {start}
    parent = {start: None}
    q = deque([start])
    while q:
        cur = q.popleft()
        for nb in graph[cur]:
            if nb not in visited:
                visited.add(nb)
                parent[nb] = cur
                if nb == target:
                    path = []
                    node = nb
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]
                q.append(nb)
    return None


def path_between_clusters(graph, points, cluster_a, cluster_b):
    """
    Find the closest pair (one point from each cluster) by Euclidean distance,
    then return the BFS shortest path between those two point indices.
    cluster_a and cluster_b are lists of point indices.
    """
    pass


if __name__ == "__main__":
    import math
    pts = [(float(i) * 0.3, 0.0, 0.0) for i in range(8)]
    # cluster A: 0,1,2  cluster B: 5,6,7  (bridge at 3,4)
    from collections import deque

    def build_graph(ps, eps):
        g = {i: [] for i in range(len(ps))}
        for i in range(len(ps)):
            for j in range(i+1, len(ps)):
                d = math.sqrt(sum((ps[i][k]-ps[j][k])**2 for k in range(3)))
                if d < eps:
                    g[i].append(j); g[j].append(i)
        return g

    g = build_graph(pts, 0.35)
    path = path_between_clusters(g, pts, [0, 1, 2], [5, 6, 7])

    print("PASS path found" if path is not None else "FAIL no path")
    if path:
        print("PASS start in A" if path[0] in [0,1,2] else f"FAIL start — {path[0]}")
        print("PASS end in B" if path[-1] in [5,6,7] else f"FAIL end — {path[-1]}")
