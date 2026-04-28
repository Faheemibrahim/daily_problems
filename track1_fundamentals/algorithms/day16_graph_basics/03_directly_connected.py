# Problem: Given an adjacency list, check if two nodes are directly connected.
# Concept: Direct neighbour lookup — O(k) where k is the degree of the node.
#          This is the membership check used inside BFS/DFS to find neighbours.
# You are done when:
#   [ ] Returns True only for nodes that share a direct edge
#   [ ] Returns False for nodes connected only via intermediate nodes
#   [ ] Returns False if either node doesn't exist
#   [ ] All test cases print PASS
# Hint: Check if b is in graph.get(a, []) — .get avoids KeyError for missing nodes.


def directly_connected(graph, a, b):
    """Return True if a and b share a direct edge in graph."""
    pass


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

    print("PASS A-B" if directly_connected(g, "A", "B") else "FAIL A-B")
    print("PASS B-A sym" if directly_connected(g, "B", "A") else "FAIL B-A sym")
    print("PASS A-E False" if not directly_connected(g, "A", "E") else "FAIL A-E False")
    print("PASS missing" if not directly_connected(g, "A", "Z") else "FAIL missing")
