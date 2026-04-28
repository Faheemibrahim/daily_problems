# Problem: Build a tree from [(2,3,0),(5,4,0),(9,6,0),(4,7,0),(8,1,0),(7,2,0)],
#          print it, and verify its structure matches a hand-drawn tree.
# Concept: Manual verification forces you to trace the algorithm step by step.
#          Sorting by x at depth 0: [2,4,5,7,8,9] -> median is 7 (index 3). Root = (7,2,0).
#          Left subtree has x in {2,4,5}; right has x in {8,9}.
# You are done when:
#   [ ] You can predict which point becomes the root before running the code
#   [ ] The root's left subtree contains only points with x < root.x
#   [ ] The root's right subtree contains only points with x > root.x
#   [ ] All test cases print PASS
# Hint: Trace the sort-and-median process for each level by hand first.


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


def collect_left(node):
    """Return all points in the left subtree."""
    if node is None or node.left is None: return []
    result = [node.left.point]
    result += collect_left(node.left) + collect_right(node.left)
    return result

def collect_right(node):
    """Return all points in the right subtree."""
    if node is None or node.right is None: return []
    result = [node.right.point]
    result += collect_left(node.right) + collect_right(node.right)
    return result


if __name__ == "__main__":
    pts = [(2.0,3.0,0.0),(5.0,4.0,0.0),(9.0,6.0,0.0),(4.0,7.0,0.0),(8.0,1.0,0.0),(7.0,2.0,0.0)]
    root = build_kdtree(pts)

    print(f"Root: {root.point} (axis={root.axis})")

    left_pts = collect_left(root)
    right_pts = collect_right(root)

    print("PASS root axis 0" if root.axis == 0 else f"FAIL root axis — {root.axis}")
    print("PASS all left x < root.x" if all(p[0] < root.point[0] for p in left_pts)
          else f"FAIL left — {[p[0] for p in left_pts]} vs root.x={root.point[0]}")
    print("PASS all right x > root.x" if all(p[0] > root.point[0] for p in right_pts)
          else f"FAIL right — {[p[0] for p in right_pts]} vs root.x={root.point[0]}")
    print("PASS 6 total" if len(pts) == 1 + len(left_pts) + len(right_pts) else
          f"FAIL count — root + {len(left_pts)} left + {len(right_pts)} right")
