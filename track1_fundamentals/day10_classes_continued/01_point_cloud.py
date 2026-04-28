# Problem: Write class PointCloud with a list of points and methods:
#          add(point), size(), centroid(), filter_by_box(bbox).
# Concept: A PointCloud class wraps a collection of points and provides domain-specific
#          operations — the same interface used in real LiDAR processing libraries.
# You are done when:
#   [ ] add(point) appends a (x, y, z) tuple to the internal list
#   [ ] size() returns the number of points
#   [ ] centroid() returns (mean_x, mean_y, mean_z)
#   [ ] filter_by_box(bbox) returns a NEW PointCloud containing only points inside bbox
#   [ ] All test cases print PASS
# Hint: filter_by_box should use bbox.contains(point) — compose BoundingBox from day09.

import math


class BoundingBox:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.z_min, self.z_max = z_min, z_max

    def contains(self, point):
        x, y, z = point
        return (self.x_min <= x <= self.x_max and
                self.y_min <= y <= self.y_max and
                self.z_min <= z <= self.z_max)


class PointCloud:
    """A collection of 3D points with spatial operations."""

    def __init__(self):
        pass

    def add(self, point):
        """Append a (x, y, z) tuple to this cloud."""
        pass

    def size(self):
        """Return the number of points."""
        pass

    def centroid(self):
        """Return (mean_x, mean_y, mean_z) of all points."""
        pass

    def filter_by_box(self, bbox):
        """Return a new PointCloud containing only points inside bbox."""
        pass


if __name__ == "__main__":
    pc = PointCloud()
    for pt in [(0.0, 0.0, 0.0), (1.0, 1.0, 0.0), (5.0, 5.0, 0.0), (2.0, 2.0, 0.0)]:
        pc.add(pt)

    print("PASS size" if pc.size() == 4 else f"FAIL size — {pc.size()}")

    c = pc.centroid()
    expected_c = (2.0, 2.0, 0.0)
    ok_c = all(abs(c[i] - expected_c[i]) < 1e-9 for i in range(3))
    print("PASS centroid" if ok_c else f"FAIL centroid — {c}")

    bb = BoundingBox(0.0, 3.0, 0.0, 3.0, -1.0, 1.0)
    filtered = pc.filter_by_box(bb)
    print("PASS filtered size" if filtered.size() == 3 else f"FAIL filtered size — {filtered.size()}")
    print("PASS filtered type" if isinstance(filtered, PointCloud) else "FAIL filtered type")
