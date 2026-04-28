# Problem: Sort a list of 3D points by distance from origin using each of your four
#          sorting algorithms. Verify all four produce the same result.
# Concept: Applying sorting to domain-specific data — you need a comparison key
#          (distance from origin). Your sorting algorithms operate on values, so you
#          pre-compute distances and sort (distance, point) pairs.
# You are done when:
#   [ ] All four algorithms produce the same sorted order
#   [ ] The sort key is Euclidean distance from origin
#   [ ] All test cases print PASS
# Hint: Create a list of (distance, point) tuples; sort that; extract the points.

import math


def bubble_sort(arr): pass   # paste from problem 01
def insertion_sort(arr): pass  # paste from problem 02
def merge_sort(arr): pass  # paste from problem 03
def quick_sort(arr): pass  # paste from problem 04


def sort_points_by_distance(points, sort_fn):
    """
    Sort points by distance from origin using sort_fn.
    Return a list of (x, y, z) tuples in ascending distance order.
    """
    pass


if __name__ == "__main__":
    import random
    random.seed(7)
    pts = [(random.uniform(-5,5), random.uniform(-5,5), random.uniform(-5,5)) for _ in range(20)]

    reference = sorted(pts, key=lambda p: math.sqrt(p[0]**2 + p[1]**2 + p[2]**2))
    for name, fn in [("bubble", bubble_sort), ("insertion", insertion_sort),
                     ("merge", merge_sort), ("quick", quick_sort)]:
        result = sort_points_by_distance(pts, fn)
        print(f"PASS {name}" if result == reference else f"FAIL {name} — {result[:3]}...")
