# Problem: Write nearest_neighbour(root, query, depth=0) that traverses the KD-tree
#          and returns the single closest point to query.
# Concept: KD-tree nearest search descends to the leaf like a BST, then backtracks
#          to check whether the "other side" of each split could have a closer point.
#          This backtracking check is the key insight that makes KD-tree search sub-linear.
# You are done when:
#   [ ] You traverse the correct subtree first based on the split axis
#   [ ] You check the other subtree only if the splitting plane is closer than current best
#   [ ] Results match brute force on all test cases
#   [ ] All test cases print PASS
# Hint: After finding the best in one subtree, check abs(query[axis] - node.point[axis]) < best_dist
#       to decide if the other subtree needs checking.

import math


class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point, self.axis, self.left, self.right = point, axis, left, right


def build_kdtree(points, depth=0):
    if not points: return None
    axis = depth % 3
    points = sorted(points, key=lambda p: p[axis])
    mid = len(points) // 2
    return KDNode(points[mid], axis, build_kdtree(points[:mid], depth+1), build_kdtree(points[mid+1:], depth+1))


def nearest_neighbour(root, query):
    """
    Return the (x, y, z) point in the KD-tree closest to query.
    """
    pass


if __name__ == "__main__":
    import random
    random.seed(1)
    pts = [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(100)]
    root = build_kdtree(pts)

    for _ in range(10):
        q = (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10))
        kd_result = nearest_neighbour(root, q)
        brute = min(pts, key=lambda p: math.sqrt(sum((p[i]-q[i])**2 for i in range(3))))
        print("PASS" if kd_result == brute else f"FAIL q={q}\n  kd={kd_result}\n  bf={brute}")
