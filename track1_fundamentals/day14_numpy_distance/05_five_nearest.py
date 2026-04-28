# Problem: Find the 5 nearest points to a query point using np.argsort.
# Concept: np.argsort returns the indices that would sort an array — slicing the first K
#          gives the K nearest neighbours without a full sort or loop.
# You are done when:
#   [ ] You compute distances in one operation
#   [ ] You use np.argsort to get sorted indices
#   [ ] You return the K nearest points (as a (K, 3) array), not just indices
#   [ ] All test cases print PASS
# Hint: sorted_idx = np.argsort(distances); arr[sorted_idx[:K]] gives the K nearest rows.

import numpy as np


def k_nearest(arr, query, k=5):
    """
    Return the k nearest points to query as a (k, 3) numpy array, sorted nearest-first.
    """
    pass


if __name__ == "__main__":
    np.random.seed(42)
    arr = np.random.rand(20, 3) * 10
    query = np.array([5.0, 5.0, 5.0])

    result = k_nearest(arr, query, k=5)
    print("PASS shape" if result.shape == (5, 3) else f"FAIL shape — {result.shape}")

    # verify result is actually sorted nearest-first
    dists = np.linalg.norm(result - query, axis=1)
    is_sorted = all(dists[i] <= dists[i+1] for i in range(len(dists)-1))
    print("PASS sorted" if is_sorted else f"FAIL sorted — distances {dists}")

    # verify they are among the 5 true nearest
    all_dists = np.linalg.norm(arr - query, axis=1)
    true_top5 = set(np.argsort(all_dists)[:5].tolist())
    result_rows = {tuple(row) for row in result}
    true_rows = {tuple(arr[i]) for i in true_top5}
    print("PASS correct points" if result_rows == true_rows else f"FAIL correct points")
