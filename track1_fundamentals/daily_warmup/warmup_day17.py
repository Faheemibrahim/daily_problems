# Warmup Day 17 — BFS retention
# Topics: BFS on 5-node graph, reachable nodes, numpy masking retention
# Fill in each block so all PASS lines print.

from collections import deque
import numpy as np

# ── 1. BFS traversal order from node 0 ───────────────────────────────────────
graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
visited = []
seen = set([0])
q = deque([0])
while q:
    node = q.popleft()
    visited.append(node)
    for nb in graph[node]:
        if nb not in seen:
            seen.add(nb)
            q.append(nb)
print("PASS bfs_order" if visited[0] == 0 and set(visited) == {0,1,2,3,4}
      else f"FAIL bfs_order — {visited}")

# ── 2. Reachable nodes from node 0 ───────────────────────────────────────────
def reachable(g, start):
    seen = {start}
    q = deque([start])
    while q:
        n = q.popleft()
        for nb in g.get(n, []):
            if nb not in seen:
                seen.add(nb)
                q.append(nb)
    return seen

r = reachable(graph, 0)
print("PASS reachable" if r == {0, 1, 2, 3, 4} else f"FAIL reachable — {r}")

# ── 3. Numpy masking retention — filter array by column value ────────────────
arr = np.array([[0, 1, 0.1], [1, 2, 0.6], [2, 3, 0.2], [3, 4, 0.8]])
mask = arr[:, 2] > 0.5
filtered = arr[mask]
print("PASS numpy_mask" if len(filtered) == 2 else f"FAIL numpy_mask — {filtered}")
