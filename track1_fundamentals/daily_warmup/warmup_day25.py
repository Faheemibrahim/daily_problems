# Warmup Day 25 — Recursion retention
# Topics: flatten 3-level nested list, kdtree depth recursively, binary search retention
# Fill in each block so all PASS lines print.

import math

# ── 1. Flatten a 3-level nested list ─────────────────────────────────────────
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], [[7], [8, [9]]]]
flat = flatten(nested)
print("PASS flatten" if flat == list(range(1,10)) else f"FAIL flatten — {flat}")

# ── 2. Compute depth of a KD-tree recursively ────────────────────────────────
class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point; self.left = left; self.right = right

def build_kdtree(pts, depth=0):
    if not pts: return None
    axis = depth % len(pts[0])
    pts = sorted(pts, key=lambda p: p[axis])
    mid = len(pts) // 2
    return KDNode(pts[mid], build_kdtree(pts[:mid], depth+1), build_kdtree(pts[mid+1:], depth+1))

def tree_depth(node):
    if node is None: return 0
    return 1 + max(tree_depth(node.left), tree_depth(node.right))

pts = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14)]
root = build_kdtree(list(pts))
depth = tree_depth(root)
import math as _math
expected_min = _math.floor(_math.log2(len(pts))) + 1
print("PASS tree_depth" if depth >= expected_min else f"FAIL tree_depth — depth={depth}")

# ── 3. Binary search retention ────────────────────────────────────────────────
def binary_search(arr, target):
    if not arr: return -1
    mid = len(arr) // 2
    if arr[mid] == target: return mid
    if arr[mid] < target:
        r = binary_search(arr[mid+1:], target)
        return mid + 1 + r if r != -1 else -1
    return binary_search(arr[:mid], target)

arr = [2, 4, 6, 8, 10, 12]
print("PASS bsearch_retention" if binary_search(arr, 8) != -1 and binary_search(arr, 7) == -1
      else "FAIL bsearch_retention")
