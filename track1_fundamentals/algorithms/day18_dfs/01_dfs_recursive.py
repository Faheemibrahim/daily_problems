# Problem: Write dfs(graph, start) recursively — return the visit order.
# Concept: DFS explores as deep as possible before backtracking. The recursive call stack
#          acts as an implicit stack. DFS and BFS find the same components but in different order.
# You are done when:
#   [ ] The function calls itself recursively on unvisited neighbours
#   [ ] A visited set prevents infinite recursion on cycles
#   [ ] All nodes in the connected component are visited exactly once
#   [ ] All test cases print PASS
# Hint: Pass the visited set as a parameter so all recursive calls share the same set.


def dfs(graph, start, visited=None):
    """
    Return a list of nodes in DFS visit order (recursive).
    """
    pass


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

    result = dfs(g, "A")
    print("PASS starts A" if result[0] == "A" else f"FAIL start — {result[0]}")
    print("PASS all nodes" if set(result) == {"A", "B", "C", "D", "E"} else f"FAIL nodes — {set(result)}")
    print("PASS no dupes" if len(result) == len(set(result)) else f"FAIL dupes — {result}")

    # DFS goes deep: A->B->D before coming back to C (or A->C->D before B depending on order)
    idx_a = result.index("A")
    idx_d = result.index("D")
    # D must come before E (D is D's only path to E)
    idx_e = result.index("E")
    print("PASS D before E" if idx_d < idx_e else f"FAIL D before E — {result}")
