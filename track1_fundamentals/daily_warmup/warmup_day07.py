# Warmup Day 07 — Dicts + Dicts Spatial + Sets + Loops
# 5 problems. Target: 5-10 minutes total.

# ── Problem 1 (Dicts) ────────────────────────────────────────────────────────
# Concept: frequency count
# Count how many times each value appears in a list. Return a dict.

def count_values(lst):
    pass

r1 = count_values([1, 2, 1, 3, 2, 1])
print("W07-P1 PASS" if r1 == {1: 3, 2: 2, 3: 1} else f"W07-P1 FAIL — got {r1}")

# ── Problem 2 (Dicts Spatial) ────────────────────────────────────────────────
# Concept: centroid of a flat list of points
# Return (mean_x, mean_y, mean_z) for a list of (x, y, z) tuples.

def centroid(pts):
    pass

r2 = centroid([(0.0, 0.0, 0.0), (2.0, 0.0, 0.0)])
print("W07-P2 PASS" if r2 == (1.0, 0.0, 0.0) else f"W07-P2 FAIL — got {r2}")

# ── Problem 3 (Sets) ─────────────────────────────────────────────────────────
# Concept: set deduplication
# Return the unique elements of a list as a set.

def unique(lst):
    pass

r3 = unique([1, 2, 2, 3, 3, 3])
print("W07-P3 PASS" if r3 == {1, 2, 3} else f"W07-P3 FAIL — got {r3}")

# ── Problem 4 (Sets) ─────────────────────────────────────────────────────────
# Concept: set intersection
# Return the elements that appear in both list_a and list_b.

def common(a, b):
    pass

r4 = common([1, 2, 3, 4], [3, 4, 5, 6])
print("W07-P4 PASS" if r4 == {3, 4} else f"W07-P4 FAIL — got {r4}")

# ── Problem 5 (Loops) ────────────────────────────────────────────────────────
# Concept: visited set in a loop
# Loop through a list. Skip any element already seen. Return the list of first occurrences.

def first_occurrences(lst):
    pass

r5 = first_occurrences([3, 1, 4, 1, 5, 9, 2, 6, 5])
print("W07-P5 PASS" if r5 == [3, 1, 4, 5, 9, 2, 6] else f"W07-P5 FAIL — got {r5}")
