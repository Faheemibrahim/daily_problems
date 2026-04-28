# Problem: Given a voxel dict, compute the centroid (mean x, mean y, mean z) of each cell
#          and store in a new dict with the same keys.
# Concept: Per-group aggregation — computing statistics per spatial cell without numpy.
# You are done when:
#   [ ] Each cell's centroid is computed as the mean of all points in that cell
#   [ ] The result dict has the same keys as the input dict
#   [ ] Values are (mean_x, mean_y, mean_z) tuples
#   [ ] All test cases print PASS
# Hint: sum(p[0] for p in pts) / len(pts) gives the mean x for a cell's point list.


def voxel_centroids(voxel_dict):
    """
    Return a dict mapping each voxel key to its centroid (mean_x, mean_y, mean_z).
    """
    pass


if __name__ == "__main__":
    vd = {
        (0, 0, 0): [(0.0, 0.0, 0.0), (2.0, 2.0, 2.0)],
        (1, 0, 0): [(1.0, 0.0, 0.0)],
    }
    result = voxel_centroids(vd)
    expected = {
        (0, 0, 0): (1.0, 1.0, 1.0),
        (1, 0, 0): (1.0, 0.0, 0.0),
    }
    ok = result.keys() == expected.keys() and all(
        all(abs(result[k][i] - expected[k][i]) < 1e-9 for i in range(3))
        for k in expected
    )
    print("PASS" if ok else f"FAIL — got {result}, expected {expected}")
