# Problem: Use DFS (recursively or iteratively) to count islands in the same 2D grid.
#          The result must match the BFS version exactly.
# Concept: DFS flood-fill is an alternative to BFS for component labelling.
#          Both are correct; DFS is often simpler to write for grids.
# You are done when:
#   [ ] Island count matches BFS result on all test inputs
#   [ ] You use DFS (stack or recursion) — not BFS
#   [ ] All test cases print PASS
# Hint: Recursive DFS: mark cell as visited (set to 0 in place or use a visited set),
#       then recurse on 4 neighbours that are 1.


def count_islands_dfs(grid):
    """
    Return the number of connected groups of 1s using DFS.
    """
    pass


if __name__ == "__main__":
    import copy
    g1 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]]
    print("PASS 3 islands" if count_islands_dfs(copy.deepcopy(g1)) == 3
          else f"FAIL — {count_islands_dfs(copy.deepcopy(g1))}")

    g2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print("PASS 1 island" if count_islands_dfs(copy.deepcopy(g2)) == 1
          else f"FAIL — {count_islands_dfs(copy.deepcopy(g2))}")

    g3 = [[0, 0], [0, 0]]
    print("PASS 0 islands" if count_islands_dfs(copy.deepcopy(g3)) == 0
          else f"FAIL — {count_islands_dfs(copy.deepcopy(g3))}")
