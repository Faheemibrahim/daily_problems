# Problem: Write dfs_path(graph, start, target) that finds a path using DFS.
#          Return the path as a list of nodes. Note: DFS does NOT guarantee shortest path.
# Concept: DFS path-finding tracks the current path and backtracks when dead ends are hit.
#          This is the basis of maze-solving and constraint satisfaction.
# You are done when:
#   [ ] The path starts at start and ends at target
#   [ ] Every consecutive pair in the path is a direct edge
#   [ ] Returns None if no path exists
#   [ ] All test cases print PASS
# Hint: Pass the current path as a list; backtrack by not including the node if recursion fails.


def dfs_path(graph, start, target, visited=None):
    """
    Return a list of nodes forming a path from start to target using DFS.
    Returns None if no path exists.
    """
    pass


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

    path = dfs_path(g, "A", "E")
    print("PASS found path" if path is not None else "FAIL no path found")
    if path:
        print("PASS start" if path[0] == "A" else f"FAIL start — {path[0]}")
        print("PASS end" if path[-1] == "E" else f"FAIL end — {path[-1]}")
        valid = all(path[i+1] in g[path[i]] for i in range(len(path)-1))
        print("PASS all edges valid" if valid else f"FAIL invalid edge — {path}")

    g2 = {"X": ["Y"], "Y": ["X"], "Z": []}
    print("PASS no path" if dfs_path(g2, "X", "Z") is None else "FAIL should be None")
