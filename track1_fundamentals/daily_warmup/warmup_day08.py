# Warmup Day 08 — Dicts + Sets + Functions + Comprehensions
# 5 problems. Target: 5-10 minutes total.

# ── Problem 1 (Dicts) ────────────────────────────────────────────────────────
# Concept: grouping by sign
# Group points into dict {"pos": [...], "neg": [...], "zero": [...]} by sign of x.

def group_by_sign(pts):
    pass

r1 = group_by_sign([(1.0, 0.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 0.0, 0.0), (2.0, 0.0, 0.0)])
print("W08-P1 PASS" if len(r1["pos"]) == 2 and len(r1["neg"]) == 1 and len(r1["zero"]) == 1
      else f"W08-P1 FAIL — {r1}")

# ── Problem 2 (Sets) ─────────────────────────────────────────────────────────
# Concept: set difference
# Return elements in list a that are NOT in list b.

def in_a_not_b(a, b):
    pass

r2 = in_a_not_b([1, 2, 3, 4], [3, 4, 5])
print("W08-P2 PASS" if r2 == {1, 2} else f"W08-P2 FAIL — got {r2}")

# ── Problem 3 (Functions) ────────────────────────────────────────────────────
# Concept: default argument
# Write clamp(value, lo=0.0, hi=1.0) that clamps value to [lo, hi].

def clamp(value, lo=0.0, hi=1.0):
    pass

print("W08-P3 PASS" if clamp(0.5) == 0.5 else f"W08-P3 FAIL mid — {clamp(0.5)}")
print("W08-P3 PASS" if clamp(-1.0) == 0.0 else f"W08-P3 FAIL low — {clamp(-1.0)}")
print("W08-P3 PASS" if clamp(2.0) == 1.0 else f"W08-P3 FAIL high — {clamp(2.0)}")
print("W08-P3 PASS" if clamp(5.0, lo=0.0, hi=10.0) == 5.0 else f"W08-P3 FAIL custom — {clamp(5.0, 0.0, 10.0)}")

# ── Problem 4 (Functions) ────────────────────────────────────────────────────
# Concept: multiple return values
# Return both the min and max of a list as a tuple (min_val, max_val).

def min_and_max(numbers):
    pass

r4 = min_and_max([3, 1, 4, 1, 5, 9])
print("W08-P4 PASS" if r4 == (1, 9) else f"W08-P4 FAIL — got {r4}")

# ── Problem 5 (Comprehensions) ───────────────────────────────────────────────
# Concept: function inside a comprehension
# Use clamp() inside a comprehension to clamp every value in a list to [0.0, 1.0].

def clamp_all(values):
    pass

r5 = clamp_all([-0.5, 0.3, 1.5, 0.8])
print("W08-P5 PASS" if r5 == [0.0, 0.3, 1.0, 0.8] else f"W08-P5 FAIL — got {r5}")
