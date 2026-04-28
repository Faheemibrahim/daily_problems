# Warmup Day 14 — Numpy Masking + Numpy Distance + Classes + Numpy+Functions
# 5 problems. Target: 5-10 minutes total.

import numpy as np
import math


# ── Problem 1 (Numpy Masking) ────────────────────────────────────────────────
# Concept: filter points within radius using a distance mask
arr1 = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [5.0, 0.0, 0.0], [0.5, 0.5, 0.0]])
query1 = np.array([0.0, 0.0, 0.0])
dists1 = np.linalg.norm(arr1 - query1, axis=1)
mask1 = dists1 < 1.5
result1 = arr1[mask1]
print("W14-P1 PASS" if result1.shape[0] == 3 else f"W14-P1 FAIL — {result1.shape[0]} rows, expected 3")

# ── Problem 2 (Numpy Distance) ───────────────────────────────────────────────
# Concept: distance from each point to origin — np.linalg.norm axis=1
arr2 = np.array([[3.0, 4.0, 0.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
dists2 = np.linalg.norm(arr2, axis=1)
print("W14-P2 PASS" if np.allclose(dists2, [5.0, 0.0, 1.0]) else f"W14-P2 FAIL — {dists2}")

# ── Problem 3 (Numpy Distance) ───────────────────────────────────────────────
# Concept: index of nearest point — np.argmin
arr3 = np.array([[5.0, 0.0, 0.0], [1.0, 0.0, 0.0], [3.0, 0.0, 0.0]])
query3 = np.array([1.1, 0.0, 0.0])
idx3 = np.argmin(np.linalg.norm(arr3 - query3, axis=1))
print("W14-P3 PASS" if idx3 == 1 else f"W14-P3 FAIL — got idx {idx3}, expected 1")

# ── Problem 4 (Classes) ──────────────────────────────────────────────────────
# Concept: PointCloud bounding box — use min/max over points
class PointCloud:
    def __init__(self): self.points = []
    def add(self, p): self.points.append(p)
    def bounding_box(self):
        pass  # return (x_min, x_max, y_min, y_max, z_min, z_max)

pc4 = PointCloud()
for p in [(0.0, 0.0, 0.0), (3.0, 4.0, 1.0), (-1.0, 2.0, -2.0)]:
    pc4.add(p)
bb4 = pc4.bounding_box()
print("W14-P4 PASS" if bb4 == (-1.0, 3.0, 0.0, 4.0, -2.0, 1.0) else f"W14-P4 FAIL — {bb4}")

# ── Problem 5 (Numpy + Functions) ────────────────────────────────────────────
# Concept: write a function that takes a numpy point cloud and returns the nearest
#          point to a query using only numpy operations (no Python loop).

def numpy_nearest(arr, query):
    pass

arr5 = np.array([[1.0, 0.0, 0.0], [5.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
q5 = np.array([1.9, 0.0, 0.0])
r5 = numpy_nearest(arr5, q5)
print("W14-P5 PASS" if np.allclose(r5, [2.0, 0.0, 0.0]) else f"W14-P5 FAIL — {r5}")
