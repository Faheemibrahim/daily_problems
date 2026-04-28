# Problem: Write a function that filters clusters by minimum and maximum size.
# Concept: Size filtering removes noise (tiny clusters) and false merges (huge clusters).
#          In cone detection: min_size removes single-point noise; max_size removes merged
#          ground patches that weren't removed by the z filter.
# You are done when:
#   [ ] Clusters with size < min_size are removed
#   [ ] Clusters with size > max_size are removed
#   [ ] If max_size=None, no upper limit is applied
#   [ ] All test cases print PASS
# Hint: A single list comprehension with two conditions handles both bounds.


def filter_by_size(clusters, min_size=5, max_size=None):
    """
    Return only clusters where min_size <= len(cluster) <= max_size.
    If max_size is None, no upper bound is applied.
    Each cluster is a list of points.
    """
    pass


if __name__ == "__main__":
    clusters = [
        [(0.0, 0.0, 0.0)] * 2,   # too small
        [(1.0, 0.0, 0.0)] * 5,   # ok
        [(2.0, 0.0, 0.0)] * 10,  # ok
        [(3.0, 0.0, 0.0)] * 50,  # too large
    ]
    result = filter_by_size(clusters, min_size=5, max_size=20)
    print("PASS" if len(result) == 2 else f"FAIL — {len(result)}")
    print("PASS sizes" if all(5 <= len(c) <= 20 for c in result) else "FAIL sizes")

    result2 = filter_by_size(clusters, min_size=5, max_size=None)
    print("PASS no upper" if len(result2) == 3 else f"FAIL no upper — {len(result2)}")
