# Warmup Day 21 — KD-Tree Search retention
# Topics: nearest neighbour in small kdtree, radius search, DFS retention
# Fill in each block so all PASS lines print.

import math
from collections import deque

class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point; self.left = left; self.right = right

def build_kdtree(pts, depth=0):
    if not pts: return None
    axis = depth % len(pts[0])
    pts = sorted(pts, key=lambda p: p[axis])
    mid = len(pts) // 2
    return KDNode(pts[mid], build_kdtree(pts[:mid], depth+1), build_kdtree(pts[mid+1:], depth+1))

# ── 1. Nearest neighbour search ───────────────────────────────────────────────
pts = [(1.0,2.0), (4.0,5.0), (7.0,1.0), (3.0,8.0), (5.0,3.0), (2.0,6.0)]
tree = build_kdtree(list(pts))

def nearest(node, target, depth=0, best=None):
    if node is None: return best
    d = math.dist(node.point, target)
    if best is None or d < math.dist(best, target): best = node.point
    axis = depth % len(target)
    diff = target[axis] - node.point[axis]
    close, far = (node.left, node.right) if diff < 0 else (node.right, node.left)
    best = nearest(close, target, depth+1, best)
    if far and abs(diff) < math.dist(best, target):
        best = nearest(far, target, depth+1, best)
    return best

query = (4.0, 4.0)
nn = nearest(tree, query)
expected = min(pts, key=lambda p: math.dist(p, query))
print("PASS nearest" if nn == expected else f"FAIL nearest — got {nn}, expected {expected}")

# ── 2. Radius search (r=2.0) ──────────────────────────────────────────────────
def radius_search(node, target, r, depth=0, result=None):
    if result is None: result = []
    if node is None: return result
    if math.dist(node.point, target) <= r: result.append(node.point)
    axis = depth % len(target)
    diff = target[axis] - node.point[axis]
    close, far = (node.left, node.right) if diff < 0 else (node.right, node.left)
    radius_search(close, target, r, depth+1, result)
    if abs(diff) <= r:
        radius_search(far, target, r, depth+1, result)
    return result

found = radius_search(tree, (4.0, 4.0), 2.0)
brute = [p for p in pts if math.dist(p, (4.0,4.0)) <= 2.0]
print("PASS radius" if set(found) == set(brute) else f"FAIL radius — got {found}, expected {brute}")

# ── 3. DFS retention — iterative DFS on a graph ──────────────────────────────
g = {"A": ["B","C"], "B": ["D"], "C": ["D"], "D": []}
stack = ["A"]; seen = {"A"}; order = []
while stack:
    n = stack.pop(); order.append(n)
    for nb in g.get(n, []):
        if nb not in seen: seen.add(nb); stack.append(nb)
print("PASS dfs_retention" if set(order) == {"A","B","C","D"} and order[0] == "A"
      else f"FAIL dfs_retention — {order}")
