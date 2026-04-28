# Warmup Day 18 — DFS retention
# Topics: DFS iterative, path A→E, classes retention
# Fill in each block so all PASS lines print.

# ── 1. DFS iterative — visited order from A ───────────────────────────────────
graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
         "D": ["B", "C", "E"], "E": ["D"]}
visited = []
stack = ["A"]
seen = {"A"}
while stack:
    node = stack.pop()
    visited.append(node)
    for nb in graph[node]:
        if nb not in seen:
            seen.add(nb)
            stack.append(nb)
print("PASS dfs_order" if visited[0] == "A" and set(visited) == {"A","B","C","D","E"}
      else f"FAIL dfs_order — {visited}")

# ── 2. Find path A → E using DFS ─────────────────────────────────────────────
def dfs_path(g, start, goal):
    stack = [(start, [start])]
    seen = {start}
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        for nb in g.get(node, []):
            if nb not in seen:
                seen.add(nb)
                stack.append((nb, path + [nb]))
    return None

path = dfs_path(graph, "A", "E")
print("PASS dfs_path" if path is not None and path[0] == "A" and path[-1] == "E"
      else f"FAIL dfs_path — {path}")

# ── 3. Classes retention — simple Point class with distance method ─────────────
class Point:
    def __init__(self, x, y):
        self.x = x; self.y = y
    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

p1 = Point(0.0, 0.0)
p2 = Point(3.0, 4.0)
print("PASS classes" if abs(p1.dist(p2) - 5.0) < 1e-9 else f"FAIL classes — {p1.dist(p2)}")
