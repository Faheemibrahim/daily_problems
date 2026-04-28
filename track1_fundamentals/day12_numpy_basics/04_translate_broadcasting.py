# Problem: Add a translation offset (1.0, 0.5, 0.0) to every point using broadcasting — no loop.
# Concept: Broadcasting lets numpy add a 1D array to every row of a 2D array automatically.
#          This is how all point cloud transformations are applied in numpy pipelines.
# You are done when:
#   [ ] You add a 1D offset array to a 2D point array with a single + operation
#   [ ] No Python for loop is used
#   [ ] All test cases print PASS
# Hint: arr + np.array([dx, dy, dz]) broadcasts the 1D offset across every row.

import numpy as np


def translate(arr, offset):
    """
    Add offset (a 1D array of shape (3,)) to every row of arr (shape (N, 3)).
    Return the translated array — no loop.
    """
    pass


if __name__ == "__main__":
    arr = np.array([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
    offset = np.array([1.0, 0.5, 0.0])
    result = translate(arr, offset)
    expected = np.array([[1.0, 0.5, 0.0], [2.0, 1.5, 1.0]])

    print("PASS shape" if result.shape == (2, 3) else f"FAIL shape — {result.shape}")
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
