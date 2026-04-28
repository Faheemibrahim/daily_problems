# Problem: Rewrite the entire filter() function from a LiDAR pipeline using numpy masks —
#          no for loops. Filter removes points outside z ∈ [-0.5, 0.3] and
#          x, y outside [-5.0, 5.0].
# Concept: Replacing a Python loop-based filter with a single vectorised mask operation.
#          This is the exact transformation that makes numpy code 10-100x faster than
#          pure Python for large point clouds.
# You are done when:
#   [ ] No Python for loop appears in your solution
#   [ ] All six boundary conditions are enforced with combined masks
#   [ ] The output is a numpy array of the surviving rows
#   [ ] All test cases print PASS
# Hint: Build six masks (z_min, z_max, x_min, x_max, y_min, y_max) and combine with &.

import numpy as np


def lidar_filter(arr, z_min=-0.5, z_max=0.3, xy_range=5.0):
    """
    Return rows of arr where z ∈ [z_min, z_max] and |x| <= xy_range and |y| <= xy_range.
    No Python loops.
    """
    pass


if __name__ == "__main__":
    arr = np.array([
        [0.0,  0.0,  0.0],   # inside
        [0.0,  0.0,  1.0],   # z too high
        [6.0,  0.0,  0.0],   # x out of range
        [0.0,  0.0, -0.6],   # z too low
        [4.9,  4.9,  0.1],   # inside
        [-4.9, 4.9,  0.0],   # inside
    ])
    result = lidar_filter(arr)
    expected = np.array([[0.0, 0.0, 0.0], [4.9, 4.9, 0.1], [-4.9, 4.9, 0.0]])

    print("PASS shape" if result.shape == (3, 3) else f"FAIL shape — {result.shape}")
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
