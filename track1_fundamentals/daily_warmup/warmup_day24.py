# Warmup Day 24 — Binary Search retention
# Topics: binary search, find first x > threshold, sorting retention
# Fill in each block so all PASS lines print.

# ── 1. Binary search on a sorted list ─────────────────────────────────────────
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print("PASS binary_search" if binary_search(arr, 7) == 3 and binary_search(arr, 6) == -1
      else f"FAIL binary_search")

# ── 2. Find index of first element > threshold ───────────────────────────────
def first_above(arr, threshold):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= threshold:
            lo = mid + 1
        else:
            hi = mid
    return lo if lo < len(arr) else -1

xs = [0.1, 0.5, 1.2, 2.4, 3.0, 4.7]
idx = first_above(xs, 1.0)
print("PASS first_above" if idx == 2 and xs[idx] == 1.2
      else f"FAIL first_above — idx={idx}")

# ── 3. Sorting retention — merge sort ────────────────────────────────────────
def merge_sort(lst):
    if len(lst) <= 1: return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: result.append(left[i]); i += 1
        else: result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

data = [8, 3, 1, 5, 2, 7, 4, 6]
print("PASS merge_sort" if merge_sort(data) == sorted(data) else "FAIL merge_sort")
