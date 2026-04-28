# Problem: Write class KDNode with point, left, right, axis attributes and a __repr__ method.
# Concept: KDNode is the building block of the KD-tree — each node stores one point and
#          two subtree pointers. The axis indicates which coordinate was used to split at
#          this level (0=x, 1=y, 2=z cycling with depth).
# You are done when:
#   [ ] __init__ sets point, left=None, right=None, axis
#   [ ] __repr__ returns a readable string showing the point and axis
#   [ ] left and right can hold other KDNode instances or None
#   [ ] All test cases print PASS
# Hint: axis = depth % 3 for 3D trees; KDNode stores a single (x, y, z) tuple.


class KDNode:
    """One node in a KD-tree."""

    def __init__(self, point, axis, left=None, right=None):
        pass

    def __repr__(self):
        pass


if __name__ == "__main__":
    root = KDNode((1.0, 2.0, 3.0), axis=0)
    left = KDNode((0.0, 0.0, 0.0), axis=1)
    root.left = left

    print("PASS point" if root.point == (1.0, 2.0, 3.0) else f"FAIL point — {root.point}")
    print("PASS axis" if root.axis == 0 else f"FAIL axis — {root.axis}")
    print("PASS left" if root.left is left else "FAIL left")
    print("PASS right None" if root.right is None else "FAIL right")
    print("PASS repr" if "1.0" in repr(root) and "axis=0" in repr(root) else f"FAIL repr — {repr(root)}")
