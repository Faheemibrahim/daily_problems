# Problem: Replace all z values below -0.5 with exactly -0.5 using np.clip — no loop.
# Concept: np.clip applies element-wise clamping to any array slice in one call.
#          Clipping z values is used in LiDAR pipelines to remove ground reflections
#          without discarding the points entirely.
# You are done when:
#   [ ] All z values < z_min become z_min in the output
#   [ ] x and y values are unchanged
#   [ ] No Python loop is used
#   [ ] The function accepts a (N, 3) array and returns a (N, 3) array
#   [ ] All test cases print PASS
# Hint: np.clip(arr[:, 2], a_min, a_max) clips column 2; assign back with arr[:, 2] = ...

import numpy as np


def clip_z(arr, z_min=-0.5):
    """
    Return a copy of arr where all z values (column 2) are clipped to >= z_min.
    """
    pass


if __name__ == "__main__":
    arr = np.array([
        [1.0,  0.0,  0.1],
        [2.0,  0.0, -0.3],
        [3.0,  0.0, -1.5],  # z too low, should become -0.5
        [4.0,  0.0, -0.5],  # exactly at boundary, unchanged
    ])
    result = clip_z(arr)

    print("PASS shape" if result.shape == arr.shape else f"FAIL shape — {result.shape}")
    print("PASS clipped" if result[2, 2] == -0.5 else f"FAIL clipped — {result[2, 2]}")
    print("PASS ok value" if result[1, 2] == -0.3 else f"FAIL ok value — {result[1, 2]}")
    print("PASS boundary" if result[3, 2] == -0.5 else f"FAIL boundary — {result[3, 2]}")
    print("PASS x unchanged" if np.allclose(result[:, 0], arr[:, 0]) else "FAIL x unchanged")
    original_z = arr[2, 2]
    print("PASS no mutation" if original_z == -1.5 else f"FAIL no mutation — arr was modified")
