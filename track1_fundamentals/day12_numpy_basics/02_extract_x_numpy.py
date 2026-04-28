# Problem: Extract all x values from a (N, 3) numpy array using slicing — no loop.
# Concept: Column slicing with [:, 0] extracts a whole axis from a 2D array in one operation.
#          This replaces a list comprehension with a single vectorised expression.
# You are done when:
#   [ ] You use array[:, 0] notation (no loop, no list comprehension)
#   [ ] The result is a 1D numpy array of length N
#   [ ] All test cases print PASS
# Hint: arr[:, 0] means "all rows, column 0" — equivalent to [p[0] for p in points].

import numpy as np


def extract_x(arr):
    """
    Return a 1D numpy array of all x values from a (N, 3) array.
    """
    pass


if __name__ == "__main__":
    arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    result = extract_x(arr)

    print("PASS type" if isinstance(result, np.ndarray) else f"FAIL type — {type(result)}")
    print("PASS shape" if result.shape == (3,) else f"FAIL shape — {result.shape}")
    expected = np.array([1.0, 4.0, 7.0])
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
