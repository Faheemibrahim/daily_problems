# Problem: Write dfs_iterative(graph, start) using a stack (plain list with .pop()).
# Concept: Iterative DFS uses an explicit stack — LIFO discipline gives depth-first order
#          without recursion limits. For large graphs, this is preferred over recursive DFS.
# You are done when:
#   [ ] You use a list as a stack with .append() and .pop() — no deque, no recursion
#   [ ] Visit order is depth-first (not BFS level order)
#   [ ] All nodes are visited exactly once
#   [ ] All test cases print PASS
# Hint: Push start onto the stack; loop: pop a node, if not visited mark it and push neighbours.


def dfs_iterative(graph, start):
    """
    Return a list of nodes in DFS visit order (iterative, using a stack).
    """
    pass


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

    result = dfs_iterative(g, "A")
    print("PASS starts A" if result[0] == "A" else f"FAIL start — {result[0]}")
    print("PASS all nodes" if set(result) == {"A", "B", "C", "D", "E"} else f"FAIL nodes — {set(result)}")
    print("PASS no dupes" if len(result) == len(set(result)) else f"FAIL dupes — {result}")
