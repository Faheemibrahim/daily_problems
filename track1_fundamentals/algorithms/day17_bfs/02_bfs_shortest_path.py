# Problem: Write bfs_shortest_path(graph, start, target) that returns the shortest path
#          from start to target as a list of nodes.
# Concept: BFS guarantees the shortest path (fewest hops) in an unweighted graph.
#          Track the predecessor of each visited node to reconstruct the path.
# You are done when:
#   [ ] The returned path starts with start and ends with target
#   [ ] The path length is the minimum number of hops
#   [ ] Returns None (or empty list) if target is unreachable
#   [ ] All test cases print PASS
# Hint: Store a parent dict {node: predecessor} during BFS; walk it backwards to build path.

from collections import deque


def bfs_shortest_path(graph, start, target):
    """
    Return a list of nodes representing the shortest path from start to target.
    Returns None if no path exists.
    """
    pass


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

    path = bfs_shortest_path(g, "A", "E")
    print("PASS start" if path and path[0] == "A" else f"FAIL start — {path}")
    print("PASS end" if path and path[-1] == "E" else f"FAIL end — {path}")
    print("PASS length" if path and len(path) == 4 else f"FAIL length — {path}")

    same = bfs_shortest_path(g, "A", "A")
    print("PASS same node" if same == ["A"] else f"FAIL same — {same}")

    g2 = {"X": ["Y"], "Y": ["X"], "Z": []}
    no_path = bfs_shortest_path(g2, "X", "Z")
    print("PASS no path" if no_path is None else f"FAIL no path — {no_path}")
