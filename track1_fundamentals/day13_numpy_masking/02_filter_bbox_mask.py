# Problem: Filter points inside a bounding box using combined boolean masks — no loop.
# Concept: Combining multiple masks with & (AND) to enforce several conditions simultaneously.
#          In numpy you must use & not `and` when combining element-wise boolean arrays.
# You are done when:
#   [ ] You create a separate mask for each boundary condition
#   [ ] You combine them with & into a single final mask
#   [ ] You index the array once with the combined mask
#   [ ] All test cases print PASS
# Hint: mask = (arr[:, 0] >= x_min) & (arr[:, 0] <= x_max) & ... (one & per condition)

import numpy as np


def filter_bbox(arr, x_min, x_max, y_min, y_max, z_min, z_max):
    """
    Return rows of arr inside the given bounding box using combined boolean masks.
    """
    pass


if __name__ == "__main__":
    arr = np.array([
        [0.0, 0.0, 0.0],
        [1.0, 1.0, 0.0],
        [5.0, 0.0, 0.0],  # outside x
        [0.0, 0.0, 2.0],  # outside z
    ])
    result = filter_bbox(arr, x_min=0.0, x_max=2.0, y_min=0.0, y_max=2.0, z_min=0.0, z_max=1.0)
    expected = np.array([[0.0, 0.0, 0.0], [1.0, 1.0, 0.0]])

    print("PASS shape" if result.shape == (2, 3) else f"FAIL shape — {result.shape}")
    print("PASS values" if np.allclose(result, expected) else f"FAIL values — {result}")
