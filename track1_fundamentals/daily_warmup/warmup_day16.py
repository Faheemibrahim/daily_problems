# Warmup Day 16 — Graph Basics retention
# Topics: adjacency list from edges, find neighbours, dict retention
# Fill in each block so all PASS lines print.

# ── 1. Build adjacency list from edge list ────────────────────────────────────
edges = [(0,1), (0,2), (1,3), (2,3), (3,4)]
graph = {}
for u, v in edges:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
print("PASS adj_list" if sorted(graph[3]) == [1, 2, 4] else f"FAIL adj_list — {graph[3]}")

# ── 2. Find all neighbours of node 0 ─────────────────────────────────────────
neighbours_0 = graph.get(0, [])
print("PASS neighbours" if set(neighbours_0) == {1, 2} else f"FAIL neighbours — {neighbours_0}")

# ── 3. Dict retention — group nodes by degree ────────────────────────────────
degree = {node: len(nbrs) for node, nbrs in graph.items()}
nodes_with_degree_2 = [n for n, d in degree.items() if d == 2]
# Nodes 0, 1, 2, 4 each have degree 2; node 3 has degree 3
print("PASS degree_group" if len(nodes_with_degree_2) == 4
      else f"FAIL degree_group — {nodes_with_degree_2}")
