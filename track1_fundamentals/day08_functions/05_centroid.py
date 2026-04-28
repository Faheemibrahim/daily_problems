# Problem: Write centroid(points) that returns the mean x, mean y, mean z as a tuple.
# Concept: Computing a per-axis mean from a list of 3D points — used in every clustering
#          algorithm to find the centre of a group.
# You are done when:
#   [ ] You compute the mean of x, y, and z independently
#   [ ] You return a (mean_x, mean_y, mean_z) tuple
#   [ ] You handle a single-point list correctly
#   [ ] All test cases print PASS
# Hint: sum(p[0] for p in points) / len(points) is the mean x using a generator expression.


def centroid(points):
    """
    Return the centroid of a list of (x, y, z) tuples as a (mean_x, mean_y, mean_z) tuple.
    """
    pass


if __name__ == "__main__":
    pts = [(0.0, 0.0, 0.0), (2.0, 0.0, 0.0), (1.0, 3.0, 0.0)]
    result = centroid(pts)
    expected = (1.0, 1.0, 0.0)
    ok = all(abs(result[i] - expected[i]) < 1e-9 for i in range(3))
    print("PASS" if ok else f"FAIL — got {result}, expected {expected}")

    single = [(5.0, 7.0, 2.0)]
    result2 = centroid(single)
    print("PASS single" if result2 == (5.0, 7.0, 2.0) else f"FAIL single — got {result2}")
