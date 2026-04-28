# Warmup Day 13 — Dicts + Numpy Basics + Numpy Masking + Comprehensions
# 5 problems. Target: 5-10 minutes total.

import numpy as np


# ── Problem 1 (Dicts) ────────────────────────────────────────────────────────
# Concept: dict comprehension for per-cell counts
# Given a voxel dict (key -> list), return a dict of key -> count using a dict comprehension.

vd1 = {(0,0,0): [1,2,3], (1,0,0): [4,5]}
counts1 = {k: len(v) for k, v in vd1.items()}
print("W13-P1 PASS" if counts1 == {(0,0,0): 3, (1,0,0): 2} else f"W13-P1 FAIL — {counts1}")

# ── Problem 2 (Numpy Basics) ─────────────────────────────────────────────────
# Concept: reshape a flat 1D array into (N, 3)
flat = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
arr2 = flat.reshape(-1, 3)
print("W13-P2 PASS" if arr2.shape == (2, 3) else f"W13-P2 FAIL — shape {arr2.shape}")

# ── Problem 3 (Numpy Masking) ────────────────────────────────────────────────
# Concept: filter rows where column 0 > 0
arr3 = np.array([[1.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
mask3 = arr3[:, 0] > 0
result3 = arr3[mask3]
expected3 = np.array([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
print("W13-P3 PASS" if np.allclose(result3, expected3) else f"W13-P3 FAIL — {result3}")

# ── Problem 4 (Numpy Masking) ────────────────────────────────────────────────
# Concept: 2D bounding box mask — combine x and y conditions
arr4 = np.array([
    [1.0, 1.0, 0.0],
    [5.0, 1.0, 0.0],  # x out
    [1.0, 5.0, 0.0],  # y out
    [2.0, 2.0, 0.0],
])
mask4 = (arr4[:, 0] <= 3.0) & (arr4[:, 1] <= 3.0)
result4 = arr4[mask4]
print("W13-P4 PASS" if result4.shape == (2, 3) else f"W13-P4 FAIL shape — {result4.shape}")

# ── Problem 5 (Comprehensions) ───────────────────────────────────────────────
# Concept: extract z values where z > 0 from list of tuples — comprehension
pts5 = [(1.0, 0.0, 0.5), (2.0, 0.0, -0.3), (3.0, 0.0, 0.1)]
z_pos = [z for x, y, z in pts5 if z > 0]
print("W13-P5 PASS" if z_pos == [0.5, 0.1] else f"W13-P5 FAIL — {z_pos}")
