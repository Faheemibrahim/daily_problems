# Problem: Write depth(node) that returns the maximum depth of a KD-tree using recursion.
# Concept: Maximum depth = 1 + max(depth(left), depth(right)). Base case: None = 0.
#          This directly verifies the log2(N) property of balanced KD-trees from day20.
# You are done when:
#   [ ] Returns 0 for a None node
#   [ ] Returns 1 for a single-node tree (leaf)
#   [ ] Returns the correct max depth for multi-level trees
#   [ ] All test cases print PASS
# Hint: return 1 + max(depth(node.left), depth(node.right)) when node is not None.


class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point, self.axis, self.left, self.right = point, axis, left, right


def build_kdtree(points, depth_=0):
    if not points: return None
    axis = depth_ % 3
    pts = sorted(points, key=lambda p: p[axis])
    mid = len(pts) // 2
    return KDNode(pts[mid], axis, build_kdtree(pts[:mid], depth_+1), build_kdtree(pts[mid+1:], depth_+1))


def depth(node):
    """Return the maximum depth of the KD-tree rooted at node."""
    pass


if __name__ == "__main__":
    import math
    print("PASS empty" if depth(None) == 0 else "FAIL empty")
    print("PASS single" if depth(build_kdtree([(1.0, 0.0, 0.0)])) == 1 else "FAIL single")

    import random; random.seed(0)
    pts = [(random.random(), random.random(), random.random()) for _ in range(127)]
    root = build_kdtree(pts)
    d = depth(root)
    expected = math.log2(len(pts))
    print(f"N=127 depth={d}, log2(N)={expected:.1f}")
    print("PASS depth in range" if expected - 2 <= d <= expected + 2 else f"FAIL depth — {d}")
