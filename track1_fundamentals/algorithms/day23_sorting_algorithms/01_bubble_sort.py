# Problem: Write bubble_sort(arr) from scratch — no built-in sort functions.
# Concept: Bubble sort repeatedly swaps adjacent elements that are out of order.
#          O(n²) worst case. Understanding it makes every other sort easier to grasp.
# You are done when:
#   [ ] You implement the swap-based inner loop correctly
#   [ ] The function sorts the list in place AND returns it
#   [ ] It handles already-sorted and reverse-sorted inputs
#   [ ] All test cases print PASS
# Hint: Outer loop N-1 times; inner loop compares arr[j] and arr[j+1], swaps if needed.


def bubble_sort(arr):
    """Sort arr in ascending order in place using bubble sort. Return arr."""
    pass


if __name__ == "__main__":
    a = [5, 3, 8, 1, 9, 2]
    result = bubble_sort(a)
    print("PASS" if result == [1, 2, 3, 5, 8, 9] else f"FAIL — {result}")
    print("PASS in place" if a == [1, 2, 3, 5, 8, 9] else "FAIL in-place")

    print("PASS already sorted" if bubble_sort([1, 2, 3]) == [1, 2, 3] else "FAIL sorted")
    print("PASS reverse" if bubble_sort([3, 2, 1]) == [1, 2, 3] else "FAIL reverse")
    print("PASS single" if bubble_sort([42]) == [42] else "FAIL single")
