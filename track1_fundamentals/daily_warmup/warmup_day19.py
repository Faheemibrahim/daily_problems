# Warmup Day 19 — BFS/DFS Applications retention
# Topics: count connected components, filter small components, sets retention
# Fill in each block so all PASS lines print.

from collections import deque

# ── 1. Count connected components ────────────────────────────────────────────
edges = [(0,1),(1,2),(3,4),(5,6),(6,7),(7,8)]
graph = {}
for u, v in edges:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
all_nodes = set(range(9))

def count_components(g, nodes):
    seen = set()
    count = 0
    for start in nodes:
        if start in seen:
            continue
        count += 1
        q = deque([start])
        seen.add(start)
        while q:
            n = q.popleft()
            for nb in g.get(n, []):
                if nb not in seen:
                    seen.add(nb)
                    q.append(nb)
    return count

num = count_components(graph, all_nodes)
print("PASS components" if num == 3 else f"FAIL components — {num}")

# ── 2. Filter small components (keep only components with ≥ 3 nodes) ─────────
def get_components(g, nodes):
    seen = set()
    comps = []
    for start in nodes:
        if start in seen:
            continue
        comp = []
        q = deque([start])
        seen.add(start)
        while q:
            n = q.popleft()
            comp.append(n)
            for nb in g.get(n, []):
                if nb not in seen:
                    seen.add(nb)
                    q.append(nb)
        comps.append(comp)
    return comps

comps = get_components(graph, all_nodes)
large = [c for c in comps if len(c) >= 3]
print("PASS filter_comps" if len(large) == 2 else f"FAIL filter_comps — {[len(c) for c in large]}")

# ── 3. Sets retention — O(1) membership check ────────────────────────────────
visited = set()
nodes_to_check = [0, 1, 2, 5, 9, 10]
for n in [0, 2, 5]:
    visited.add(n)
not_visited = [n for n in nodes_to_check if n not in visited]
print("PASS sets" if set(not_visited) == {1, 9, 10} else f"FAIL sets — {not_visited}")
