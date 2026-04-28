# Problem: Write class Cluster with a list of points and methods:
#          centroid(), size(), bounding_box() returning a BoundingBox.
# Concept: A Cluster is a PointCloud with identity — it represents one detected object.
#          bounding_box() is used to estimate object size for downstream filtering.
# You are done when:
#   [ ] __init__ accepts a list of points (may be empty initially)
#   [ ] centroid() returns (mean_x, mean_y, mean_z)
#   [ ] size() returns len of the internal list
#   [ ] bounding_box() computes exact axis-aligned bounds and returns a BoundingBox
#   [ ] All test cases print PASS
# Hint: Compute x_min = min(p[0] for p in points) — or manually loop as in day01.

import math


class BoundingBox:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.z_min, self.z_max = z_min, z_max

    def dimensions(self):
        return (self.x_max - self.x_min, self.y_max - self.y_min, self.z_max - self.z_min)


class Cluster:
    """A labelled group of 3D points representing one detected object."""

    def __init__(self, points=None):
        pass

    def size(self):
        """Return number of points."""
        pass

    def centroid(self):
        """Return (mean_x, mean_y, mean_z)."""
        pass

    def bounding_box(self):
        """Return a BoundingBox that tightly fits all points in this cluster."""
        pass


if __name__ == "__main__":
    pts = [(0.0, 0.0, 0.0), (2.0, 0.0, 0.0), (1.0, 3.0, 1.0)]
    cl = Cluster(pts)

    print("PASS size" if cl.size() == 3 else f"FAIL size — {cl.size()}")

    c = cl.centroid()
    expected_c = (1.0, 1.0, 1/3)
    ok_c = all(abs(c[i] - expected_c[i]) < 1e-9 for i in range(3))
    print("PASS centroid" if ok_c else f"FAIL centroid — {c}, expected {expected_c}")

    bb = cl.bounding_box()
    print("PASS bbox type" if isinstance(bb, BoundingBox) else "FAIL bbox type")
    dims = bb.dimensions()
    expected_dims = (2.0, 3.0, 1.0)
    print("PASS dims" if dims == expected_dims else f"FAIL dims — {dims}, expected {expected_dims}")
