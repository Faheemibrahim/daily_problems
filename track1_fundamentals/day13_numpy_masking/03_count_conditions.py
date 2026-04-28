# Problem: Count how many points satisfy multiple conditions simultaneously using
#          np.sum on a boolean mask.
# Concept: np.sum(bool_array) counts True values — the numpy idiom for conditional counting.
#          This avoids a loop and an accumulator variable entirely.
# You are done when:
#   [ ] You build a combined boolean mask with & for multiple conditions
#   [ ] You use np.sum() on the mask to count matches
#   [ ] The result is an integer (or numpy integer)
#   [ ] All test cases print PASS
# Hint: np.sum(mask) treats True as 1 and False as 0 — the count of matching rows.

import numpy as np


def count_in_region(arr, x_min, x_max, z_min, z_max):
    """
    Count rows where x is in [x_min, x_max] AND z is in [z_min, z_max].
    """
    pass


if __name__ == "__main__":
    arr = np.array([
        [1.0, 0.0, 0.0],  # x in range, z in range
        [3.0, 0.0, 0.0],  # x out of range
        [1.0, 0.0, 5.0],  # z out of range
        [2.0, 0.0, 0.1],  # both in range
    ])
    result = count_in_region(arr, x_min=0.0, x_max=2.5, z_min=-1.0, z_max=1.0)
    print("PASS" if result == 2 else f"FAIL — got {result}, expected 2")
