# Problem: Loop through a voxel dict and print how many points are in each cell.
#          Return a dict of voxel_key -> count.
# Concept: Iterating over a spatial index dict and computing a per-cell summary.
# You are done when:
#   [ ] You loop with .items()
#   [ ] Each count matches the length of the point list for that cell
#   [ ] All test cases print PASS
# Hint: This is the same pattern as day05 problem 05, just applied to spatial data.


def voxel_counts(voxel_dict):
    """
    Return a dict mapping each voxel key to the number of points in that cell.
    """
    pass


if __name__ == "__main__":
    vd = {
        (0, 0, 0): [(0.1, 0.1, 0.1), (0.2, 0.2, 0.1)],
        (1, 0, 0): [(0.9, 0.1, 0.1)],
        (2, 0, 0): [(1.0, 0.0, 0.0)],
    }
    result = voxel_counts(vd)
    expected = {(0, 0, 0): 2, (1, 0, 0): 1, (2, 0, 0): 1}
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
