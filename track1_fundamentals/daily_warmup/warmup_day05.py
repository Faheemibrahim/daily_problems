# Warmup Day 05 — Loops + Comprehensions + Slicing + Dicts
# 5 problems. Target: 5-10 minutes total.

# ── Problem 1 (Loops) ────────────────────────────────────────────────────────
# Concept: manual max — no built-in
# Find the maximum value in a list using a loop — no max().

def manual_max(numbers):
    pass

r1 = manual_max([3, 7, 1, 9, 4])
print("W05-P1 PASS" if r1 == 9 else f"W05-P1 FAIL — got {r1}")

# ── Problem 2 (Comprehensions) ───────────────────────────────────────────────
# Concept: filter points by x
# Return only points where x > 0 using a comprehension.

def positive_x_points(pts):
    pass

r2 = positive_x_points([(1.0, 0.0, 0.0), (-1.0, 0.0, 0.0), (2.0, 0.0, 0.0)])
print("W05-P2 PASS" if r2 == [(1.0, 0.0, 0.0), (2.0, 0.0, 0.0)] else f"W05-P2 FAIL — got {r2}")

# ── Problem 3 (Slicing) ──────────────────────────────────────────────────────
# Concept: step slicing
# Return every other element starting from index 0 using slicing.

def every_other(lst):
    pass

r3 = every_other([0, 1, 2, 3, 4, 5])
print("W05-P3 PASS" if r3 == [0, 2, 4] else f"W05-P3 FAIL — got {r3}")

# ── Problem 4 (Dicts) ────────────────────────────────────────────────────────
# Concept: dict creation and access
# Create a dict {"a": 1, "b": 2, "c": 3} and return the value for key "b".

def dict_lookup():
    pass

r4 = dict_lookup()
print("W05-P4 PASS" if r4 == 2 else f"W05-P4 FAIL — got {r4}")

# ── Problem 5 (Dicts) ────────────────────────────────────────────────────────
# Concept: key existence check
# Return True if "x" is a key in the dict, False otherwise.

def has_key_x(d):
    pass

print("W05-P5 PASS" if has_key_x({"x": 1, "y": 2}) is True else "W05-P5 FAIL True")
print("W05-P5 PASS" if has_key_x({"a": 1}) is False else "W05-P5 FAIL False")
