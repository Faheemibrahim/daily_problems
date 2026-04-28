# Warmup Day 23 — Sorting Algorithms retention
# Topics: insertion sort, sort points by lambda, kdtree retention
# Fill in each block so all PASS lines print.

import math
import numpy as np
from scipy.spatial import KDTree

# ── 1. Insertion sort on a list of numbers ────────────────────────────────────
def insertion_sort(lst):
    arr = list(lst)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

data = [5, 2, 8, 1, 9, 3]
result = insertion_sort(data)
print("PASS insertion_sort" if result == sorted(data) else f"FAIL insertion_sort — {result}")

# ── 2. Sort 3D points by distance to origin using a lambda ───────────────────
points = [(3.0,4.0,0.0), (1.0,0.0,0.0), (0.0,0.0,5.0), (2.0,2.0,1.0)]
dist_origin = lambda p: math.sqrt(p[0]**2 + p[1]**2 + p[2]**2)
sorted_pts = sorted(points, key=dist_origin)
dists = [round(dist_origin(p), 4) for p in sorted_pts]
print("PASS sort_lambda" if dists == sorted(dists) else f"FAIL sort_lambda — {dists}")

# ── 3. KD-tree retention — build from 3D points and query nearest ─────────────
pts3d = np.array([(0.0,0.0,0.0),(1.0,0.0,0.0),(0.0,1.0,0.0),(0.0,0.0,1.0),(2.0,2.0,2.0)])
tree = KDTree(pts3d)
_, idx = tree.query((0.1, 0.1, 0.1))
nearest = tuple(pts3d[idx])
print("PASS kdtree_retention" if nearest == (0.0,0.0,0.0)
      else f"FAIL kdtree_retention — {nearest}")
