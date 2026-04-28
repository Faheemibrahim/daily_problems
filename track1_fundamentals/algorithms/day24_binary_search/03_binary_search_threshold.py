# Problem: Given a list of points sorted by x coordinate, use binary search to find
#          the first point where x > threshold.
# Concept: Binary search on a derived key — the search criterion is not equality but
#          a threshold crossing. This is used to efficiently find candidate points
#          in spatial algorithms where points are pre-sorted along one axis.
# You are done when:
#   [ ] You binary-search on the x values without building an intermediate array
#   [ ] You return the point (not index) where x first exceeds threshold
#   [ ] You return None if no point exceeds the threshold
#   [ ] All test cases print PASS
# Hint: Binary search for the leftmost index where points[mid][0] > threshold.


def first_point_exceeding_x(points, threshold):
    """
    Given a list of (x, y, z) tuples sorted by x, return the first point where x > threshold.
    Returns None if no such point exists.
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (3.0, 0.0, 0.0),
           (4.0, 0.0, 0.0), (5.0, 0.0, 0.0)]

    r = first_point_exceeding_x(pts, 2.5)
    print("PASS" if r == (3.0, 0.0, 0.0) else f"FAIL — {r}")

    r2 = first_point_exceeding_x(pts, 0.5)
    print("PASS first" if r2 == (1.0, 0.0, 0.0) else f"FAIL first — {r2}")

    r3 = first_point_exceeding_x(pts, 10.0)
    print("PASS none" if r3 is None else f"FAIL none — {r3}")
