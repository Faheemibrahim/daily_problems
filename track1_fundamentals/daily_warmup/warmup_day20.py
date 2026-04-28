# Warmup Day 20 — KD-Tree Build retention
# Topics: build kdtree from 6 points, verify left child, BFS retention
# Fill in each block so all PASS lines print.

from collections import deque
import math

# ── 1. Build a simple KD-tree from 6 2D points ───────────────────────────────
class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kdtree(pts, depth=0):
    if not pts:
        return None
    axis = depth % len(pts[0])
    pts.sort(key=lambda p: p[axis])
    mid = len(pts) // 2
    return KDNode(pts[mid],
                  build_kdtree(pts[:mid], depth+1),
                  build_kdtree(pts[mid+1:], depth+1))

points_2d = [(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)]
root = build_kdtree(list(points_2d))
print("PASS build_kdtree" if root is not None and root.point is not None
      else "FAIL build_kdtree")

# ── 2. Verify left child exists and has a smaller x than root ────────────────
# At depth=0 axis=0 (x), median splits on x; left subtree has smaller x values.
has_left = root.left is not None
left_x_smaller = root.left.point[0] < root.point[0] if has_left else False
print("PASS left_child" if has_left and left_x_smaller
      else f"FAIL left_child — left={root.left.point if has_left else None}, root={root.point}")

# ── 3. BFS retention — level-order traversal of the tree ────────────────────
def bfs_tree(node):
    if node is None:
        return []
    result = []
    q = deque([node])
    while q:
        n = q.popleft()
        result.append(n.point)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return result

levels = bfs_tree(root)
print("PASS bfs_tree" if len(levels) == 6 else f"FAIL bfs_tree — {len(levels)} nodes")
