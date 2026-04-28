# Warmup Day 04 — Lists + Loops + Comprehensions + Slicing
# 5 problems. Target: 5-10 minutes total.

# ── Problem 1 (Lists) ────────────────────────────────────────────────────────
# Concept: membership check
# Return True if 42 is in the list, False otherwise.

def contains_42(lst):
    pass

print("W04-P1 PASS" if contains_42([1, 42, 3]) is True else "W04-P1 FAIL True case")
print("W04-P1 PASS" if contains_42([1, 2, 3]) is False else "W04-P1 FAIL False case")

# ── Problem 2 (Loops) ────────────────────────────────────────────────────────
# Concept: zip — pair two lists
# Using zip, return a list of (a, b) tuples from two lists of equal length.

def zip_together(a, b):
    pass

r2 = zip_together([1, 2, 3], ["x", "y", "z"])
print("W04-P2 PASS" if r2 == [(1, "x"), (2, "y"), (3, "z")] else f"W04-P2 FAIL — got {r2}")

# ── Problem 3 (Comprehensions) ───────────────────────────────────────────────
# Concept: field extraction from tuples
# Extract only the x (first) value from each (x, y, z) tuple — one comprehension.

def extract_x(pts):
    pass

r3 = extract_x([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)])
print("W04-P3 PASS" if r3 == [1.0, 4.0] else f"W04-P3 FAIL — got {r3}")

# ── Problem 4 (Slicing) ──────────────────────────────────────────────────────
# Concept: slice first N elements
# Return the first 3 elements of a list using slicing.

def first_three(lst):
    pass

r4 = first_three([10, 20, 30, 40, 50])
print("W04-P4 PASS" if r4 == [10, 20, 30] else f"W04-P4 FAIL — got {r4}")

# ── Problem 5 (Slicing) ──────────────────────────────────────────────────────
# Concept: reverse with slice
# Reverse a list using the [::-1] idiom — no .reverse().

def reverse_list(lst):
    pass

r5 = reverse_list([1, 2, 3, 4])
print("W04-P5 PASS" if r5 == [4, 3, 2, 1] else f"W04-P5 FAIL — got {r5}")
