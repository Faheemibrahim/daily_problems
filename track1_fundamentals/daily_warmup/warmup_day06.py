# Warmup Day 06 — Comprehensions + Dicts + Spatial Voxels
# 4 problems. Target: 5-10 minutes total.

# ── Problem 1 (Comprehensions) ───────────────────────────────────────────────
# Concept: transform comprehension on a tuple field
# Return a new list of tuples where every z value is shifted by +1.0.

def shift_z(pts):
    pass

r1 = shift_z([(0.0, 0.0, 0.0), (1.0, 2.0, 3.0)])
print("W06-P1 PASS" if r1 == [(0.0, 0.0, 1.0), (1.0, 2.0, 4.0)] else f"W06-P1 FAIL — got {r1}")

# ── Problem 2 (Dicts) ────────────────────────────────────────────────────────
# Concept: filter dict keys by value
# Return a list of keys where the value is > 0.

def keys_with_positive_value(d):
    pass

r2 = keys_with_positive_value({"a": 1, "b": -2, "c": 3, "d": 0})
print("W06-P2 PASS" if sorted(r2) == ["a", "c"] else f"W06-P2 FAIL — got {sorted(r2)}")

# ── Problem 3 (Dicts Spatial) ────────────────────────────────────────────────
# Concept: group points into cells using floor(x) as the cell key
# Group a list of (x, y, z) points into a dict keyed by int(x) (integer part of x only).

def group_by_int_x(pts):
    pass

pts3 = [(0.2, 0.0, 0.0), (0.9, 0.0, 0.0), (1.5, 0.0, 0.0), (1.8, 0.0, 0.0)]
r3 = group_by_int_x(pts3)
print("W06-P3 PASS" if len(r3.get(0, [])) == 2 and len(r3.get(1, [])) == 2 else f"W06-P3 FAIL — {r3}")

# ── Problem 4 (Dicts Spatial) ────────────────────────────────────────────────
# Concept: find the densest cell
# Given the dict from problem 3 (or similar), return the key with the most points.

def densest_cell(cell_dict):
    pass

d4 = {0: [1, 2, 3], 1: [4, 5], 2: [6, 7, 8, 9]}
r4 = densest_cell(d4)
print("W06-P4 PASS" if r4 == 2 else f"W06-P4 FAIL — got {r4}, expected 2")
