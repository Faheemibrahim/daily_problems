# Problem: Use DFS to find all connected components. Compare with BFS version from day17.
#          Both must find the same components (same sets of nodes, possibly different order).
# Concept: DFS and BFS find identical connected components — the algorithm differs,
#          the result is equivalent. Verifying this builds confidence in both implementations.
# You are done when:
#   [ ] DFS finds the same number of components as BFS
#   [ ] Each component's node set matches between DFS and BFS exactly
#   [ ] All test cases print PASS
# Hint: Use the same outer loop as BFS all-clusters: iterate over all nodes, DFS from unvisited ones.

from collections import deque


def dfs_all_components(graph):
    """Return a list of sets, each set being one connected component (via DFS)."""
    pass


def bfs_all_components(graph):
    """Return a list of sets, each set being one connected component (via BFS)."""
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            comp = set()
            q = deque([node])
            visited.add(node)
            while q:
                cur = q.popleft()
                comp.add(cur)
                for nb in graph[cur]:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            components.append(comp)
    return components


if __name__ == "__main__":
    g = {
        "A": ["B", "C"], "B": ["A"], "C": ["A"],
        "X": ["Y"], "Y": ["X"],
        "Z": [],
    }
    dfs_comps = dfs_all_components(g)
    bfs_comps = bfs_all_components(g)

    dfs_sorted = sorted(dfs_comps, key=lambda s: sorted(s)[0])
    bfs_sorted = sorted(bfs_comps, key=lambda s: sorted(s)[0])

    print("PASS num components" if len(dfs_comps) == 3 else f"FAIL num — {len(dfs_comps)}")
    print("PASS matches BFS" if dfs_sorted == bfs_sorted else f"FAIL mismatch\n  DFS: {dfs_sorted}\n  BFS: {bfs_sorted}")
