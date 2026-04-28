# Problem: Write binary_search(arr, target) on a sorted list. Return the index or -1.
# Concept: Binary search halves the search space each step — O(log n) vs O(n) linear.
#          The input MUST be sorted; this precondition is easy to forget and causes bugs.
# You are done when:
#   [ ] You correctly track lo and hi boundaries
#   [ ] You return the index when found, -1 when not found
#   [ ] Works for targets at the start, middle, and end of the list
#   [ ] All test cases print PASS
# Hint: mid = (lo + hi) // 2; if arr[mid] == target return mid; elif arr[mid] < target: lo = mid+1


def binary_search(arr, target):
    """
    Return the index of target in sorted arr, or -1 if not found.
    """
    pass


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]

    print("PASS found 7" if binary_search(arr, 7) == 3 else f"FAIL 7 — {binary_search(arr, 7)}")
    print("PASS found 1" if binary_search(arr, 1) == 0 else f"FAIL 1 — {binary_search(arr, 1)}")
    print("PASS found 15" if binary_search(arr, 15) == 7 else f"FAIL 15 — {binary_search(arr, 15)}")
    print("PASS not found" if binary_search(arr, 6) == -1 else f"FAIL not found — {binary_search(arr, 6)}")
    print("PASS empty" if binary_search([], 5) == -1 else "FAIL empty")
