# Problem: Compute the distance from every point to a query point in one numpy line — no loop.
# Concept: Subtracting a query point (broadcasting) then taking row-wise norms gives all
#          distances to that query in a single vectorised expression.
# You are done when:
#   [ ] You subtract the query from every row using broadcasting in one step
#   [ ] You apply np.linalg.norm with axis=1 to the result
#   [ ] No Python loop is used
#   [ ] All test cases print PASS
# Hint: arr - query broadcasts if query has shape (3,); then norm the differences.

import numpy as np


def distances_to_query(arr, query):
    """
    Return a 1D array of distances from each point in arr to the query point.
    query is a 1D array of shape (3,).
    """
    pass


if __name__ == "__main__":
    arr = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [4.0, 3.0, 0.0]])
    query = np.array([1.0, 0.0, 0.0])
    result = distances_to_query(arr, query)
    expected = np.array([1.0, 0.0, 5.0])

    print("PASS shape" if result.shape == (3,) else f"FAIL shape — {result.shape}")
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
