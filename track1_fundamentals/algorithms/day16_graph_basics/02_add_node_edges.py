# Problem: Given an adjacency list, add a new node and new edges to it.
# Concept: Graph mutation — nodes and edges can be added dynamically.
#          This mirrors how a point cloud graph grows when new points arrive.
# You are done when:
#   [ ] The new node appears as a key
#   [ ] New edges appear in both directions
#   [ ] Existing nodes and edges are unchanged
#   [ ] All test cases print PASS
# Hint: g.setdefault(node, []).append(neighbour) is safe even if the node is new.


def add_node(graph, node):
    """Add a node to the graph with no edges. Modifies graph in place."""
    pass


def add_edge(graph, a, b):
    """Add an undirected edge between a and b. Modifies graph in place."""
    pass


if __name__ == "__main__":
    g = {"A": ["B"], "B": ["A"]}

    add_node(g, "C")
    print("PASS node added" if "C" in g else "FAIL node added")
    print("PASS C no edges" if g["C"] == [] else f"FAIL C edges — {g['C']}")

    add_edge(g, "A", "C")
    print("PASS A-C in A" if "C" in g["A"] else f"FAIL A-C in A — {g['A']}")
    print("PASS A-C in C" if "A" in g["C"] else f"FAIL A-C in C — {g['C']}")
    print("PASS B unchanged" if g["B"] == ["A"] else f"FAIL B changed — {g['B']}")
