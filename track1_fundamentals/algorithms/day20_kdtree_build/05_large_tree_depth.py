# Problem: Build a tree from 1000 random 3D points and verify the tree depth is
#          roughly log2(1000) ≈ 10 levels.
# Concept: A balanced KD-tree halves the remaining points at each level, so depth ≈ log2(N).
#          This is what makes search O(log N) instead of O(N). Verifying depth builds
#          intuition for why the algorithm is fast.
# You are done when:
#   [ ] You compute the actual maximum depth of the built tree
#   [ ] Depth is between log2(N) - 2 and log2(N) + 2
#   [ ] All test cases print PASS
# Hint: Write tree_depth(node) recursively: 0 if leaf, 1 + max(depth(left), depth(right)).

import math
import random


class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point, self.axis, self.left, self.right = point, axis, left, right


def build_kdtree(points, depth=0):
    if not points: return None
    axis = depth % 3
    points = sorted(points, key=lambda p: p[axis])
    mid = len(points) // 2
    return KDNode(points[mid], axis,
                  build_kdtree(points[:mid], depth+1),
                  build_kdtree(points[mid+1:], depth+1))


def tree_depth(node):
    """Return the maximum depth of the KD-tree rooted at node."""
    pass


if __name__ == "__main__":
    random.seed(0)
    N = 1000
    pts = [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10))
           for _ in range(N)]

    root = build_kdtree(pts)
    depth = tree_depth(root)
    expected = math.log2(N)

    print(f"N={N}, tree depth={depth}, log2(N)={expected:.1f}")
    print("PASS depth in range" if expected - 2 <= depth <= expected + 2
          else f"FAIL depth out of range — depth={depth}, expected≈{expected:.1f}")
