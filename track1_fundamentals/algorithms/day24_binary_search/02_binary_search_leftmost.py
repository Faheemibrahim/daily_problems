# Problem: Write binary_search_leftmost(arr, target) that returns the index of the
#          FIRST occurrence when duplicates exist.
# Concept: When duplicates are present, standard binary search may land on any occurrence.
#          The leftmost variant (lower bound) continues searching left even after finding
#          a match — used in range queries and sorted-array lookups.
# You are done when:
#   [ ] Returns the smallest index where arr[index] == target
#   [ ] Returns -1 if target is not in arr
#   [ ] All test cases print PASS
# Hint: When arr[mid] == target, record mid but continue: hi = mid - 1 to find earlier occurrences.


def binary_search_leftmost(arr, target):
    """
    Return the index of the first occurrence of target in sorted arr, or -1 if absent.
    """
    pass


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5]

    print("PASS leftmost 2" if binary_search_leftmost(arr, 2) == 1 else f"FAIL — {binary_search_leftmost(arr, 2)}")
    print("PASS unique 1" if binary_search_leftmost(arr, 1) == 0 else f"FAIL 1 — {binary_search_leftmost(arr, 1)}")
    print("PASS not found" if binary_search_leftmost(arr, 9) == -1 else "FAIL not found")
    print("PASS last elem" if binary_search_leftmost(arr, 5) == 6 else f"FAIL last — {binary_search_leftmost(arr, 5)}")
