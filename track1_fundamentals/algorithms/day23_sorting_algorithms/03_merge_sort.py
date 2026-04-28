# Problem: Write merge_sort(arr) recursively — return a new sorted list.
# Concept: Merge sort is O(n log n) and stable. It recursively splits the array in half
#          and merges the sorted halves. Understanding it is a prerequisite for understanding
#          many divide-and-conquer algorithms.
# You are done when:
#   [ ] The function is recursive with a base case for len <= 1
#   [ ] The merge step correctly interleaves two sorted arrays
#   [ ] Returns a new list (does not modify the original)
#   [ ] All test cases print PASS
# Hint: Split at midpoint; recurse on each half; merge by comparing heads of each half.


def merge_sort(arr):
    """Return a new sorted list using recursive merge sort."""
    pass


if __name__ == "__main__":
    a = [5, 3, 8, 1, 9, 2]
    result = merge_sort(a)
    print("PASS" if result == [1, 2, 3, 5, 8, 9] else f"FAIL — {result}")
    print("PASS original unchanged" if a == [5, 3, 8, 1, 9, 2] else "FAIL original modified")
    print("PASS already sorted" if merge_sort([1, 2, 3]) == [1, 2, 3] else "FAIL sorted")
    print("PASS empty" if merge_sort([]) == [] else "FAIL empty")
    print("PASS single" if merge_sort([99]) == [99] else "FAIL single")
