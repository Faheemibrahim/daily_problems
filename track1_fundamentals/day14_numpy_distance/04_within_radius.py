# Problem: Find all points within radius R of a query point using masking — return indices.
# Concept: Combining distance computation and boolean masking with np.where or nonzero —
#          the foundation of radius search used in Euclidean clustering.
# You are done when:
#   [ ] You compute distances vectorially
#   [ ] You build a boolean mask for distances < radius
#   [ ] You return the indices (not the points) using np.where or np.nonzero
#   [ ] All test cases print PASS
# Hint: np.where(mask)[0] gives you the indices where the condition is True.

import numpy as np


def within_radius(arr, query, radius):
    """
    Return a 1D array of indices of points in arr within radius of query.
    """
    pass


if __name__ == "__main__":
    arr = np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [5.0, 0.0, 0.0],
        [0.5, 0.5, 0.0],
    ])
    query = np.array([0.0, 0.0, 0.0])
    result = within_radius(arr, query, radius=1.5)
    expected_set = {0, 1, 3}
    print("PASS" if set(result.tolist()) == expected_set else f"FAIL — got {result}, expected {expected_set}")
