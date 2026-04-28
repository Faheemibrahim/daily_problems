# Problem: Compute the centroid of a point cloud, then subtract it from every point
#          so the cloud is centred at the origin.
# Concept: Mean subtraction (centring) is a preprocessing step before PCA, ICP, and
#          other algorithms that assume zero-mean data. Broadcasting makes it one line.
# You are done when:
#   [ ] The centroid of the returned array is (0, 0, 0) within floating-point tolerance
#   [ ] The relative distances between points are preserved (shape is unchanged)
#   [ ] No loop is used — only numpy operations
#   [ ] All test cases print PASS
# Hint: np.mean(arr, axis=0) gives the centroid; arr - centroid broadcasts across rows.

import numpy as np


def centre_cloud(arr):
    """
    Return a copy of arr shifted so its centroid is at the origin.
    """
    pass


if __name__ == "__main__":
    arr = np.array([[1.0, 2.0, 3.0], [3.0, 4.0, 5.0], [5.0, 6.0, 7.0]])
    result = centre_cloud(arr)

    centroid = np.mean(result, axis=0)
    print("PASS centroid at origin" if np.allclose(centroid, [0.0, 0.0, 0.0])
          else f"FAIL centroid — {centroid}")

    # distances between pairs should be preserved
    d_before = np.linalg.norm(arr[0] - arr[1])
    d_after  = np.linalg.norm(result[0] - result[1])
    print("PASS distances preserved" if abs(d_before - d_after) < 1e-9
          else f"FAIL distances — before={d_before}, after={d_after}")

    # original array should not be modified
    print("PASS no mutation" if arr[0, 0] == 1.0 else "FAIL no mutation")
