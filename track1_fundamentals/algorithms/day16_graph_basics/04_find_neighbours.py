# Problem: Given an adjacency list, find all neighbours of a given node.
# Concept: Neighbour retrieval is the inner step of both BFS and DFS — every algorithm
#          that traverses a graph calls this repeatedly.
# You are done when:
#   [ ] Returns the list of direct neighbours for any existing node
#   [ ] Returns an empty list (not an error) for a node with no edges
#   [ ] Returns an empty list for a node not in the graph
#   [ ] All test cases print PASS
# Hint: graph.get(node, []) returns [] safely for missing keys.


def get_neighbours(graph, node):
    """Return the list of all direct neighbours of node."""
    pass


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

    print("PASS A" if set(get_neighbours(g, "A")) == {"B", "C"} else f"FAIL A — {get_neighbours(g, 'A')}")
    print("PASS E" if get_neighbours(g, "E") == ["D"] else f"FAIL E — {get_neighbours(g, 'E')}")
    print("PASS missing" if get_neighbours(g, "Z") == [] else f"FAIL missing — {get_neighbours(g, 'Z')}")
