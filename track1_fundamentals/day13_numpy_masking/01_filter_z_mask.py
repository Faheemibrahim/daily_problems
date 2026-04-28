# Problem: Filter all points where z > 0 using a boolean mask — no loop.
# Concept: Boolean indexing: arr[mask] where mask is a bool array selects rows in one step.
#          This is the numpy replacement for the comprehension from day03.
# You are done when:
#   [ ] You create a boolean mask with a single comparison (no loop)
#   [ ] You use the mask to index the array in one step
#   [ ] The result shape is (K, 3) where K <= N
#   [ ] All test cases print PASS
# Hint: mask = arr[:, 2] > 0 creates a bool array; arr[mask] returns matching rows.

import numpy as np


def filter_z_positive(arr):
    """
    Return rows of arr where z (column 2) > 0, using a boolean mask.
    """
    pass


if __name__ == "__main__":
    arr = np.array([
        [1.0, 2.0, -1.0],
        [1.0, 2.0,  3.0],
        [0.0, 0.0, -0.5],
        [4.0, 4.0,  0.1],
    ])
    result = filter_z_positive(arr)
    expected = np.array([[1.0, 2.0, 3.0], [4.0, 4.0, 0.1]])

    print("PASS shape" if result.shape == (2, 3) else f"FAIL shape — {result.shape}")
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
