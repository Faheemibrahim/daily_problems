# Problem: Compute the centroid of all points in one line using np.mean with the axis argument.
# Concept: np.mean(arr, axis=0) reduces rows to a single row of per-column means —
#          the numpy equivalent of the centroid() function from day08.
# You are done when:
#   [ ] You use np.mean with axis=0 (not axis=1)
#   [ ] The result is a 1D array of shape (3,)
#   [ ] All test cases print PASS
# Hint: axis=0 collapses along the row axis, giving one mean per column.

import numpy as np


def centroid_numpy(arr):
    """
    Return the centroid of a (N, 3) numpy array as a 1D array of shape (3,).
    Use np.mean with the axis argument — one line.
    """
    pass


if __name__ == "__main__":
    arr = np.array([[0.0, 0.0, 0.0], [2.0, 0.0, 0.0], [1.0, 3.0, 0.0]])
    result = centroid_numpy(arr)
    expected = np.array([1.0, 1.0, 0.0])

    print("PASS shape" if result.shape == (3,) else f"FAIL shape — {result.shape}")
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
