# Problem: Write class BoundingBox with x_min, x_max, y_min, y_max, z_min, z_max attributes,
#          a contains(point) method, and a dimensions() method returning (width, depth, height).
# Concept: A bounding box is used everywhere in spatial computing to quickly reject
#          points that can't be in a cluster without computing full distances.
# You are done when:
#   [ ] __init__ stores all six bounds
#   [ ] contains(point) returns True if point is inside (inclusive boundaries)
#   [ ] dimensions() returns (x_max - x_min, y_max - y_min, z_max - z_min)
#   [ ] All test cases print PASS
# Hint: contains checks all six inequalities: x_min <= px <= x_max, etc.


class BoundingBox:
    """Axis-aligned bounding box in 3D."""

    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        pass

    def contains(self, point):
        """Return True if (x, y, z) tuple point is inside this bounding box (inclusive)."""
        pass

    def dimensions(self):
        """Return (width, depth, height) as a tuple."""
        pass


if __name__ == "__main__":
    bb = BoundingBox(0.0, 2.0, 0.0, 3.0, 0.0, 1.0)

    print("PASS inside" if bb.contains((1.0, 1.5, 0.5)) else "FAIL inside")
    print("PASS on edge" if bb.contains((0.0, 0.0, 0.0)) else "FAIL on edge")
    print("PASS outside x" if not bb.contains((3.0, 1.0, 0.5)) else "FAIL outside x")
    print("PASS outside z" if not bb.contains((1.0, 1.0, 2.0)) else "FAIL outside z")

    dims = bb.dimensions()
    expected_dims = (2.0, 3.0, 1.0)
    print("PASS dims" if dims == expected_dims else f"FAIL dims — got {dims}, expected {expected_dims}")
