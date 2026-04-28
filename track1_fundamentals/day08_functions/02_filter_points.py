# Problem: Write filter_points(points, z_min=-0.5, z_max=0.3, x_range=5.0, y_range=5.0)
#          using default arguments. Remove points outside those bounds.
# Concept: Functions with default arguments let callers use sensible defaults or override them.
#          This mirrors the exact filter step in a LiDAR pipeline.
# You are done when:
#   [ ] All four parameters have default values that match the signature above
#   [ ] A point is kept only if z_min <= z <= z_max AND |x| <= x_range AND |y| <= y_range
#   [ ] Calling with no keyword args uses the defaults
#   [ ] All test cases print PASS
# Hint: abs(x) <= x_range tests both x > -x_range and x < x_range in one check.


def filter_points(points, z_min=-0.5, z_max=0.3, x_range=5.0, y_range=5.0):
    """
    Return points that fall within the specified bounding region.
    """
    pass


if __name__ == "__main__":
    pts = [
        (0.0, 0.0, 0.0),    # inside
        (0.0, 0.0, 1.0),    # z too high
        (6.0, 0.0, 0.0),    # x out of range
        (0.0, 0.0, -0.6),   # z too low
        (4.9, 4.9, 0.1),    # inside
    ]
    result = filter_points(pts)
    expected = [(0.0, 0.0, 0.0), (4.9, 4.9, 0.1)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    # custom bounds
    result2 = filter_points(pts, z_min=0.0, z_max=0.5, x_range=10.0, y_range=10.0)
    expected2 = [(0.0, 0.0, 0.0), (4.9, 4.9, 0.1)]
    print("PASS custom" if result2 == expected2 else f"FAIL custom — got {result2}")
