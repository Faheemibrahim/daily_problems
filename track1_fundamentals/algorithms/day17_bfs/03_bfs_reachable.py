# Problem: Write bfs_reachable(graph, start) that returns the set of all nodes
#          reachable from start (including start itself).
# Concept: Reachability = connected component. A node is reachable if BFS ever visits it.
#          This is the core question Euclidean clustering answers for each seed point.
# You are done when:
#   [ ] The result includes start
#   [ ] All nodes reachable via any path are included
#   [ ] Nodes in disconnected components are excluded
#   [ ] All test cases print PASS
# Hint: Run normal BFS; the visited set at the end is the reachable set.

from collections import deque


def bfs_reachable(graph, start):
    """Return the set of all nodes reachable from start."""
    pass


if __name__ == "__main__":
    g = {
        "A": ["B", "C"], "B": ["A"], "C": ["A"],
        "X": ["Y"], "Y": ["X"],  # separate component
    }

    r = bfs_reachable(g, "A")
    print("PASS A component" if r == {"A", "B", "C"} else f"FAIL A component — {r}")

    r2 = bfs_reachable(g, "X")
    print("PASS X component" if r2 == {"X", "Y"} else f"FAIL X component — {r2}")

    # single isolated node
    g2 = {"Z": []}
    r3 = bfs_reachable(g2, "Z")
    print("PASS isolated" if r3 == {"Z"} else f"FAIL isolated — {r3}")
