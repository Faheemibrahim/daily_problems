# Problem: Represent a point cloud as a graph where each point is a node (by index)
#          and two points are connected if their Euclidean distance < epsilon.
#          Build the adjacency list from a list of 10 3D points.
# Concept: A point cloud graph is exactly what Euclidean clustering builds internally.
#          Every cluster is a connected component in this graph.
# You are done when:
#   [ ] Nodes are integer indices (0..N-1), not the points themselves
#   [ ] An edge i-j exists iff distance(points[i], points[j]) < epsilon
#   [ ] No self-edges (i != j)
#   [ ] All test cases print PASS
# Hint: Nested loop over indices i and j where j > i; add edges both ways when close enough.

import math


def build_point_graph(points, epsilon=0.5):
    """
    Return an adjacency list {index: [neighbour_indices, ...]} for points
    where an edge exists between i and j iff distance < epsilon.
    """
    pass


if __name__ == "__main__":
    # Two tight clusters: indices 0-3 near origin, 4-6 near (5,5,0)
    pts = [
        (0.0, 0.0, 0.0), (0.1, 0.0, 0.0), (0.2, 0.0, 0.0), (0.1, 0.1, 0.0),
        (5.0, 5.0, 0.0), (5.1, 5.0, 0.0), (5.2, 5.0, 0.0),
        (10.0, 10.0, 0.0),  # isolated
    ]
    g = build_point_graph(pts, epsilon=0.5)

    print("PASS num nodes" if len(g) == len(pts) else f"FAIL num nodes — {len(g)}")
    print("PASS 0-1 connected" if 1 in g[0] else f"FAIL 0-1 — {g[0]}")
    print("PASS 0-4 not connected" if 4 not in g[0] else "FAIL 0-4 should not be connected")
    print("PASS isolated 7" if g[7] == [] else f"FAIL isolated 7 — {g[7]}")
    print("PASS no self-loops" if all(i not in g[i] for i in range(len(pts))) else "FAIL self-loop")
