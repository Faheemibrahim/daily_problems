# Problem: Represent a graph as an adjacency list using a dict.
#          Nodes: A B C D E
#          Edges: A-B  A-C  B-D  C-D  D-E
# Concept: An adjacency list (dict of node -> list of neighbours) is the standard
#          graph representation for BFS/DFS. Each node maps to its direct neighbours.
# You are done when:
#   [ ] Every node appears as a key in the dict
#   [ ] Every edge is represented in both directions (undirected graph)
#   [ ] You can look up the neighbours of any node in O(1)
#   [ ] All test cases print PASS
# Hint: For an undirected graph, edge A-B means A's list contains B AND B's list contains A.


def build_graph():
    """
    Return the adjacency list for:
      Nodes: A B C D E
      Edges: A-B  A-C  B-D  C-D  D-E
    as a dict of {node: [neighbour, ...]}
    """
    pass


if __name__ == "__main__":
    g = build_graph()

    print("PASS all nodes" if set(g.keys()) == {"A", "B", "C", "D", "E"} else f"FAIL nodes — {set(g.keys())}")
    print("PASS A neighbours" if set(g["A"]) == {"B", "C"} else f"FAIL A — {g['A']}")
    print("PASS D neighbours" if set(g["D"]) == {"B", "C", "E"} else f"FAIL D — {g['D']}")
    print("PASS E neighbours" if set(g["E"]) == {"D"} else f"FAIL E — {g['E']}")
    # undirected: B contains A
    print("PASS undirected B-A" if "A" in g["B"] else "FAIL undirected B-A")
