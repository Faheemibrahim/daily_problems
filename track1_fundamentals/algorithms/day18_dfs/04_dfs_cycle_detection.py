# Problem: Write has_cycle(graph) that detects if a cycle exists in an undirected graph.
# Concept: In an undirected graph, a cycle exists if DFS encounters an already-visited node
#          that is not the immediate parent of the current node. Tracking the parent prevents
#          false positives from the trivial back-edge A->B->A.
# You are done when:
#   [ ] Returns True for any graph containing a cycle
#   [ ] Returns False for trees (connected, no cycles) and forests
#   [ ] Handles disconnected graphs correctly
#   [ ] All test cases print PASS
# Hint: DFS from each unvisited node; pass parent along; if visited and not parent -> cycle.


def has_cycle(graph):
    """Return True if the undirected graph contains any cycle."""
    pass


if __name__ == "__main__":
    # Triangle A-B-C-A: has cycle
    g_cycle = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    print("PASS cycle detected" if has_cycle(g_cycle) else "FAIL should find cycle")

    # Tree A-B-C-D: no cycle
    g_tree = {"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"]}
    print("PASS no cycle" if not has_cycle(g_tree) else "FAIL tree has no cycle")

    # Single node
    g_single = {"X": []}
    print("PASS single node" if not has_cycle(g_single) else "FAIL single should have no cycle")
