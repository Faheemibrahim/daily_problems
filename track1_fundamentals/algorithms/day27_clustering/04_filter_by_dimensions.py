# Problem: Write a function that filters clusters by bounding box dimensions.
#          Keep only clusters where x_span < 1.0 and y_span < 1.0 and z_span < 0.8 (cone-sized).
# Concept: Dimension filtering rejects objects too large or too wide to be cones.
#          Combined with size filtering it dramatically reduces false positives in detection.
# You are done when:
#   [ ] You compute x/y/z span as max - min for each axis
#   [ ] All three axis constraints must be satisfied to keep a cluster
#   [ ] All test cases print PASS
# Hint: x_span = max(p[0] for p in cluster) - min(p[0] for p in cluster)


def filter_by_dimensions(clusters, x_max=1.0, y_max=1.0, z_max=0.8):
    """
    Return only clusters whose bounding box fits within (x_max, y_max, z_max).
    """
    pass


if __name__ == "__main__":
    clusters = [
        # cone-sized: 0.3 x 0.3 x 0.5 span
        [(0.0, 0.0, 0.0), (0.3, 0.3, 0.5)],
        # too wide in x: 1.5 span
        [(0.0, 0.0, 0.0), (1.5, 0.0, 0.0)],
        # too tall in z: 0.9 span
        [(0.0, 0.0, 0.0), (0.1, 0.1, 0.9)],
        # barely fits
        [(0.0, 0.0, 0.0), (0.99, 0.99, 0.79)],
    ]
    result = filter_by_dimensions(clusters)
    print("PASS" if len(result) == 2 else f"FAIL — {len(result)} kept (expected 2)")
    print("PASS all fit" if all(
        max(p[0] for p in c) - min(p[0] for p in c) < 1.0 and
        max(p[1] for p in c) - min(p[1] for p in c) < 1.0 and
        max(p[2] for p in c) - min(p[2] for p in c) < 0.8
        for c in result) else "FAIL dimensions")
