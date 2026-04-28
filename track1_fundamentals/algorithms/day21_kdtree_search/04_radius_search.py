# Problem: Write radius_search(root, query, radius, depth=0) that returns all points
#          within Euclidean distance radius of query.
# Concept: Radius search is the core operation in Euclidean clustering — for each seed
#          point, find all neighbours within epsilon. KD-tree pruning skips subtrees whose
#          bounding region is entirely outside the search sphere.
# You are done when:
#   [ ] All points within radius are returned (no misses)
#   [ ] No points outside radius are returned (no false positives)
#   [ ] Subtrees are pruned when the splitting plane is further than radius
#   [ ] All test cases print PASS
# Hint: Include a point if dist(query, node.point) <= radius; recurse on a subtree only
#       if abs(query[axis] - node.point[axis]) <= radius.

import math


class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point, self.axis, self.left, self.right = point, axis, left, right


def build_kdtree(points, depth=0):
    if not points: return None
    axis = depth % 3
    pts = sorted(points, key=lambda p: p[axis])
    mid = len(pts) // 2
    return KDNode(pts[mid], axis, build_kdtree(pts[:mid], depth+1), build_kdtree(pts[mid+1:], depth+1))


def radius_search(root, query, radius):
    """
    Return a list of all points within Euclidean distance radius of query.
    """
    pass


if __name__ == "__main__":
    pts = [(float(i), 0.0, 0.0) for i in range(10)]
    root = build_kdtree(pts)

    result = radius_search(root, (5.0, 0.0, 0.0), 1.5)
    expected = {(4.0, 0.0, 0.0), (5.0, 0.0, 0.0), (6.0, 0.0, 0.0)}
    print("PASS" if set(result) == expected else f"FAIL — got {set(result)}, expected {expected}")

    result2 = radius_search(root, (0.0, 0.0, 0.0), 0.5)
    print("PASS origin" if set(result2) == {(0.0, 0.0, 0.0)} else f"FAIL origin — {result2}")
