# Problem: Write insertion_sort(arr) from scratch.
# Concept: Insertion sort builds a sorted prefix by inserting each element into its
#          correct position in the already-sorted left portion. O(n²) worst case,
#          but O(n) for nearly-sorted data — useful in practice for small arrays.
# You are done when:
#   [ ] The function maintains a sorted prefix that grows by one each outer iteration
#   [ ] Elements are shifted right (not swapped) to make room for the inserted element
#   [ ] All test cases print PASS
# Hint: For each i, store key = arr[i], shift elements > key to the right, insert key.


def insertion_sort(arr):
    """Sort arr in ascending order in place using insertion sort. Return arr."""
    pass


if __name__ == "__main__":
    a = [5, 3, 8, 1, 9, 2]
    result = insertion_sort(a)
    print("PASS" if result == [1, 2, 3, 5, 8, 9] else f"FAIL — {result}")
    print("PASS in place" if a == [1, 2, 3, 5, 8, 9] else "FAIL in-place")
    print("PASS already sorted" if insertion_sort([1, 2, 3]) == [1, 2, 3] else "FAIL sorted")
    print("PASS single" if insertion_sort([7]) == [7] else "FAIL single")
