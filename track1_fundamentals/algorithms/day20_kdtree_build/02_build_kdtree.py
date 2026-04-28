# Problem: Write build_kdtree(points, depth=0) recursively. Split on the alternating
#          axis (depth % 3) and use the median point as the node.
# Concept: A KD-tree partitions space by alternately splitting along x, y, z axes.
#          The median split keeps the tree balanced (O(log n) depth), making searches
#          O(log n) on average instead of O(n) for brute force.
# You are done when:
#   [ ] The root's axis is 0 (split on x at depth 0)
#   [ ] Points with smaller axis value go left; larger go right
#   [ ] The tree handles 1-point and 0-point base cases without crashing
#   [ ] All test cases print PASS
# Hint: Sort points by points[axis_index]; pick middle as node; recurse on left half and right half.


class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point, self.axis, self.left, self.right = point, axis, left, right
    def __repr__(self):
        return f"KDNode(point={self.point}, axis={self.axis})"


def build_kdtree(points, depth=0):
    """
    Build and return the root KDNode of a KD-tree from a list of (x, y, z) tuples.
    Returns None for an empty list.
    """
    pass


if __name__ == "__main__":
    pts = [(2.0, 3.0, 0.0), (5.0, 4.0, 0.0), (9.0, 6.0, 0.0),
           (4.0, 7.0, 0.0), (8.0, 1.0, 0.0), (7.0, 2.0, 0.0)]
    root = build_kdtree(pts)

    print("PASS root is node" if isinstance(root, KDNode) else "FAIL root type")
    print("PASS root axis 0" if root.axis == 0 else f"FAIL root axis — {root.axis}")
    print("PASS has children" if root.left or root.right else "FAIL no children")

    # All points with x < root.point[0] should be in left subtree
    def collect(node):
        if node is None: return []
        return [node.point] + collect(node.left) + collect(node.right)
    all_pts = set(collect(root))
    print("PASS all 6 points" if len(all_pts) == 6 else f"FAIL point count — {len(all_pts)}")

    print("PASS empty" if build_kdtree([]) is None else "FAIL empty")
