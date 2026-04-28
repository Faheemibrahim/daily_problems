# Problem: Given a list of (x, y, z) points, build a voxel lookup dict where
#          key = (vx, vy, vz) using floor division by voxel_size=0.5,
#          and value = list of points that fall into that cell.
# Concept: Discretising continuous space into grid cells — foundational for voxel downsampling.
# You are done when:
#   [ ] Each key is a tuple of integers from int(coord // voxel_size)
#   [ ] Each value is a list of original points (not rounded points)
#   [ ] A point is in exactly one cell
#   [ ] All test cases print PASS
# Hint: int(x // voxel_size) converts a float coordinate into a voxel index.

import math


def build_voxel_dict(points, voxel_size=0.5):
    """
    Return a dict mapping (vx, vy, vz) voxel keys to lists of (x, y, z) points.
    """
    pass


if __name__ == "__main__":
    pts = [
        (0.1, 0.1, 0.1),
        (0.2, 0.2, 0.1),
        (0.9, 0.1, 0.1),
        (1.0, 0.0, 0.0),
    ]
    result = build_voxel_dict(pts, voxel_size=0.5)

    # (0.1, 0.1, 0.1) -> voxel (0, 0, 0); (0.2, 0.2, 0.1) -> (0, 0, 0)
    # (0.9, 0.1, 0.1) -> (1, 0, 0); (1.0, 0.0, 0.0) -> (2, 0, 0)
    print("PASS cell (0,0,0) size" if len(result.get((0, 0, 0), [])) == 2 else f"FAIL (0,0,0): {result.get((0,0,0))}")
    print("PASS cell (1,0,0) size" if len(result.get((1, 0, 0), [])) == 1 else f"FAIL (1,0,0): {result.get((1,0,0))}")
    print("PASS cell (2,0,0) size" if len(result.get((2, 0, 0), [])) == 1 else f"FAIL (2,0,0): {result.get((2,0,0))}")
