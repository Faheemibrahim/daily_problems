# Problem: Given a 2D grid of 0s and 1s (1 = occupied cell), use BFS to find all
#          connected groups of 1s and return the count of groups (island counting).
# Concept: 2D grid BFS is the direct analogue of 3D point cloud clustering —
#          each occupied cell is a "point", 4-connectivity defines neighbours.
#          Every cluster in Euclidean clustering is an "island" in a 3D grid.
# You are done when:
#   [ ] You find every group of connected 1s (4-connectivity: up/down/left/right)
#   [ ] You use BFS with a deque
#   [ ] Each cell is visited at most once
#   [ ] All test cases print PASS
# Hint: Treat (row, col) pairs as nodes; neighbours are the 4 adjacent cells that are 1.

from collections import deque


def count_islands_bfs(grid):
    """
    Return the number of connected groups of 1s in the 2D grid.
    grid is a list of lists of ints (0 or 1).
    """
    pass


if __name__ == "__main__":
    g1 = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
    ]
    print("PASS 3 islands" if count_islands_bfs(g1) == 3 else f"FAIL — {count_islands_bfs(g1)}")

    g2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print("PASS 1 island" if count_islands_bfs(g2) == 1 else f"FAIL — {count_islands_bfs(g2)}")

    g3 = [[0, 0], [0, 0]]
    print("PASS 0 islands" if count_islands_bfs(g3) == 0 else f"FAIL — {count_islands_bfs(g3)}")
