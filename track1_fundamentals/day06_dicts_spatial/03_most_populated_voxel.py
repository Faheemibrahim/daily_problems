# Problem: Find which voxel cell contains the most points.
# Concept: Finding the key with the maximum value in a dict — a pattern that appears
#          constantly in spatial grouping (densest region, most active cell, etc.).
# You are done when:
#   [ ] You return the voxel key (tuple), not the list of points
#   [ ] You handle the case where multiple cells tie (return any one)
#   [ ] You do not use max() with a lambda on an external count — work directly from the dict
#   [ ] All test cases print PASS
# Hint: max(d, key=lambda k: len(d[k])) finds the key whose value list is longest.


def most_populated_voxel(voxel_dict):
    """
    Return the voxel key (vx, vy, vz) that has the most points in its list.
    """
    pass


if __name__ == "__main__":
    vd = {
        (0, 0, 0): [(0.1, 0.1, 0.1), (0.2, 0.2, 0.1), (0.3, 0.3, 0.1)],
        (1, 0, 0): [(0.9, 0.1, 0.1)],
        (2, 0, 0): [(1.0, 0.0, 0.0), (1.1, 0.0, 0.0)],
    }
    result = most_populated_voxel(vd)
    print("PASS" if result == (0, 0, 0) else f"FAIL — got {result}, expected (0, 0, 0)")
