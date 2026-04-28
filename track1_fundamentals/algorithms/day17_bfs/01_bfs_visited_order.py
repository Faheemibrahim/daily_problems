# Problem: Write bfs(graph, start) from scratch using collections.deque.
#          Return the order in which nodes were visited.
# Concept: BFS explores level by level using a queue (FIFO). deque with popleft()
#          is the correct data structure — using a list with pop(0) is O(n) per step.
# You are done when:
#   [ ] You use collections.deque — not a plain list
#   [ ] Nodes are visited in breadth-first order (nearest neighbours first)
#   [ ] No node appears more than once in the result
#   [ ] All test cases print PASS
# Hint: Initialise deque([start]), mark start visited, then loop: pop left, add to order,
#       enqueue unvisited neighbours.

from collections import deque


def bfs(graph, start):
    """
    Return a list of nodes in BFS visit order starting from start.
    """
    pass


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

    result = bfs(g, "A")
    print("PASS starts at A" if result[0] == "A" else f"FAIL start — {result[0]}")
    print("PASS all nodes" if set(result) == {"A", "B", "C", "D", "E"} else f"FAIL nodes — {set(result)}")
    print("PASS no dupes" if len(result) == len(set(result)) else f"FAIL dupes — {result}")
    # B and C (depth 1) must both appear before D and E (depth 2+)
    print("PASS BFS levels" if result.index("B") < result.index("D") and
          result.index("C") < result.index("E") else f"FAIL BFS order — {result}")
