# Problem: Compute the distance from every point to the origin in one numpy operation.
# Concept: np.linalg.norm with axis=1 computes the L2 norm of each row simultaneously —
#          replacing a loop that called math.sqrt for every point.
# You are done when:
#   [ ] You use np.linalg.norm with axis=1 (not a loop)
#   [ ] The result is a 1D array of shape (N,)
#   [ ] All test cases print PASS
# Hint: np.linalg.norm(arr, axis=1) treats each row as a vector and returns its magnitude.

import numpy as np


def distances_to_origin(arr):
    """
    Return a 1D array of Euclidean distances from each point (row) to the origin.
    """
    pass


if __name__ == "__main__":
    arr = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [3.0, 4.0, 0.0]])
    result = distances_to_origin(arr)
    expected = np.array([1.0, 0.0, 5.0])

    print("PASS shape" if result.shape == (3,) else f"FAIL shape — {result.shape}")
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
