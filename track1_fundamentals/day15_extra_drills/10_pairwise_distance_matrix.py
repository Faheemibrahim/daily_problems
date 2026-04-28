# Problem: Compute the full (N x N) pairwise distance matrix for N points using
#          numpy broadcasting — no Python loops.
# Concept: Reshaping to (N, 1, 3) and subtracting (N, 3) yields (N, N, 3) differences
#          in one operation. This is the vectorised form of the O(n²) distance loop
#          from day02 — same result, but computed entirely inside numpy.
# You are done when:
#   [ ] result[i][j] == result[j][i] for all i, j (symmetric)
#   [ ] result[i][i] == 0.0 for all i (diagonal is zero)
#   [ ] No Python for loop is used
#   [ ] All test cases print PASS
# Hint: diff = arr[:, None, :] - arr[None, :, :] gives shape (N, N, 3);
#       np.linalg.norm(diff, axis=2) gives shape (N, N).

import numpy as np


def pairwise_distance_matrix(arr):
    """
    Return an (N, N) array of pairwise Euclidean distances.
    arr has shape (N, 3).
    """
    pass


if __name__ == "__main__":
    pts = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    D = pairwise_distance_matrix(pts)

    print("PASS shape" if D.shape == (3, 3) else f"FAIL shape — {D.shape}")
    print("PASS diagonal" if np.allclose(np.diag(D), 0.0) else f"FAIL diagonal — {np.diag(D)}")
    print("PASS symmetric" if np.allclose(D, D.T) else "FAIL symmetric")
    print("PASS d01" if abs(D[0, 1] - 1.0) < 1e-9 else f"FAIL d01 — {D[0, 1]}")
    print("PASS d12" if abs(D[1, 2] - np.sqrt(2)) < 1e-9 else f"FAIL d12 — {D[1, 2]}")
