# Warmup Day 12 — Classes + Functions + Numpy Basics + Broadcasting
# 5 problems. Target: 5-10 minutes total.

import numpy as np


# ── Problem 1 (Classes) ──────────────────────────────────────────────────────
# Concept: BoundingBox contains check
class BoundingBox:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.z_min, self.z_max = z_min, z_max
    def contains(self, p):
        pass

bb = BoundingBox(0.0, 2.0, 0.0, 2.0, 0.0, 1.0)
print("W12-P1 PASS inside" if bb.contains((1.0, 1.0, 0.5)) else "W12-P1 FAIL inside")
print("W12-P1 PASS outside" if not bb.contains((3.0, 1.0, 0.5)) else "W12-P1 FAIL outside")

# ── Problem 2 (Functions) ────────────────────────────────────────────────────
# Concept: brute-force nearest neighbour using numpy
import math

def find_nearest(query, pts):
    pass

pts2 = [(1.0, 0.0, 0.0), (5.0, 0.0, 0.0), (2.0, 0.0, 0.0)]
r2 = find_nearest((1.4, 0.0, 0.0), pts2)
print("W12-P2 PASS" if r2 == (1.0, 0.0, 0.0) else f"W12-P2 FAIL — got {r2}")

# ── Problem 3 (Numpy Basics) ─────────────────────────────────────────────────
# Concept: np.mean with axis=0
arr3 = np.array([[0.0, 0.0, 0.0], [2.0, 4.0, 6.0]])
mean3 = np.mean(arr3, axis=0)
print("W12-P3 PASS" if np.allclose(mean3, [1.0, 2.0, 3.0]) else f"W12-P3 FAIL — {mean3}")

# ── Problem 4 (Numpy Basics) ─────────────────────────────────────────────────
# Concept: element-wise max between two arrays
arr4a = np.array([1.0, 5.0, 3.0])
arr4b = np.array([4.0, 2.0, 6.0])
result4 = np.maximum(arr4a, arr4b)
print("W12-P4 PASS" if np.allclose(result4, [4.0, 5.0, 6.0]) else f"W12-P4 FAIL — {result4}")

# ── Problem 5 (Broadcasting) ─────────────────────────────────────────────────
# Concept: subtract a 1D vector from all rows of a 2D array
arr5 = np.array([[3.0, 3.0, 3.0], [1.0, 1.0, 1.0]])
offset5 = np.array([1.0, 1.0, 1.0])
result5 = arr5 - offset5
expected5 = np.array([[2.0, 2.0, 2.0], [0.0, 0.0, 0.0]])
print("W12-P5 PASS" if np.allclose(result5, expected5) else f"W12-P5 FAIL — {result5}")
