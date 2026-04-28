# Problem: Write quick_sort(arr) recursively — return a new sorted list.
# Concept: Quick sort is O(n log n) average, O(n²) worst case. It partitions around a
#          pivot and recurses. With random pivots or median-of-three it is extremely fast
#          in practice — the basis of Python's Timsort and C's qsort.
# You are done when:
#   [ ] You choose a pivot (any strategy is fine — last element is simplest)
#   [ ] You partition into less-than, equal-to, greater-than pivot
#   [ ] You recurse and concatenate the results
#   [ ] All test cases print PASS
# Hint: pivot = arr[-1]; left = [x for x in arr[:-1] if x <= pivot]; right = [...if x > pivot]


def quick_sort(arr):
    """Return a new sorted list using recursive quick sort."""
    pass


if __name__ == "__main__":
    a = [5, 3, 8, 1, 9, 2]
    result = quick_sort(a)
    print("PASS" if result == [1, 2, 3, 5, 8, 9] else f"FAIL — {result}")
    print("PASS original unchanged" if a == [5, 3, 8, 1, 9, 2] else "FAIL original modified")
    print("PASS duplicates" if quick_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3] else "FAIL dupes")
    print("PASS empty" if quick_sort([]) == [] else "FAIL empty")
