# Problem: Find the index of the nearest point to a query using np.argmin.
# Concept: np.argmin(distances) returns the index of the minimum value in one call —
#          the numpy equivalent of the manual tracking loop from day08 problem 03.
# You are done when:
#   [ ] You compute distances to all points in one operation (from problem 02)
#   [ ] You use np.argmin to get the index — no loop
#   [ ] The return value is an integer index, not the point itself
#   [ ] All test cases print PASS
# Hint: np.argmin(arr) returns the index of the smallest element.

import numpy as np


def nearest_index(arr, query):
    """
    Return the integer index of the point in arr closest to query.
    """
    pass


if __name__ == "__main__":
    arr = np.array([[5.0, 0.0, 0.0], [1.0, 0.0, 0.0], [3.0, 0.0, 0.0]])
    query = np.array([1.1, 0.0, 0.0])
    result = nearest_index(arr, query)
    print("PASS" if result == 1 else f"FAIL — got {result}, expected 1")

    query2 = np.array([4.9, 0.0, 0.0])
    result2 = nearest_index(arr, query2)
    print("PASS" if result2 == 0 else f"FAIL — got {result2}, expected 0")
