# Problem: Write class Point3D with x, y, z attributes, a distance_to(other) method,
#          and a __repr__ method.
# Concept: Classes bundle data (attributes) and behaviour (methods) together.
#          __repr__ gives a readable string form; distance_to is the same formula from day08.
# You are done when:
#   [ ] Point3D stores x, y, z set in __init__
#   [ ] distance_to(other) returns float Euclidean distance to another Point3D
#   [ ] __repr__ returns "Point3D(x=..., y=..., z=...)" with the actual values
#   [ ] All test cases print PASS
# Hint: Access the other point's attributes with other.x, other.y, other.z inside distance_to.

import math


class Point3D:
    """A point in 3D space."""

    def __init__(self, x, y, z):
        pass

    def distance_to(self, other):
        """Return Euclidean distance from self to other."""
        pass

    def __repr__(self):
        pass


if __name__ == "__main__":
    p1 = Point3D(0.0, 0.0, 0.0)
    p2 = Point3D(3.0, 4.0, 0.0)

    print("PASS x" if p1.x == 0.0 else f"FAIL x — {p1.x}")
    print("PASS distance" if p1.distance_to(p2) == 5.0 else f"FAIL distance — {p1.distance_to(p2)}")
    print("PASS repr" if repr(p2) == "Point3D(x=3.0, y=4.0, z=0.0)" else f"FAIL repr — {repr(p2)}")
    print("PASS self distance" if p1.distance_to(p1) == 0.0 else "FAIL self distance")
