# Problem: Scale all points by a factor of 2.0 in one operation — no loop.
# Concept: Scalar multiplication in numpy applies to every element simultaneously.
#          This is the simplest form of broadcasting: scalar * array.
# You are done when:
#   [ ] You multiply the entire array by a scalar in one expression
#   [ ] No loop is used
#   [ ] All test cases print PASS
# Hint: arr * 2.0 multiplies every element; arr * factor works for any float factor.

import numpy as np


def scale(arr, factor):
    """
    Return a new array with every point scaled by factor.
    """
    pass


if __name__ == "__main__":
    arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    result = scale(arr, 2.0)
    expected = np.array([[2.0, 4.0, 6.0], [8.0, 10.0, 12.0]])

    print("PASS" if np.allclose(result, expected) else f"FAIL — {result}")

    result2 = scale(arr, 0.5)
    expected2 = np.array([[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]])
    print("PASS 0.5x" if np.allclose(result2, expected2) else f"FAIL 0.5x — {result2}")
