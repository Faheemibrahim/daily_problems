# Problem: Convert a list of (x, y, z) tuples to a numpy array of shape (N, 3).
# Concept: np.array() is the entry point to numpy — shape (N, 3) is the standard
#          representation of a point cloud in all numpy-based LiDAR code.
# You are done when:
#   [ ] The output is a numpy ndarray, not a list
#   [ ] Shape is (N, 3) where N is number of points
#   [ ] dtype is float64
#   [ ] All test cases print PASS
# Hint: np.array(list_of_tuples) automatically creates a 2D array with one row per tuple.

import numpy as np


def to_numpy(points):
    """
    Convert a list of (x, y, z) tuples to a numpy array of shape (N, 3).
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    result = to_numpy(pts)

    print("PASS type" if isinstance(result, np.ndarray) else f"FAIL type — {type(result)}")
    print("PASS shape" if result.shape == (3, 3) else f"FAIL shape — {result.shape}")
    print("PASS value" if result[1, 1] == 5.0 else f"FAIL value — {result[1, 1]}")
