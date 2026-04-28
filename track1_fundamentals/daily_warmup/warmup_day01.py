# Warmup Day 01 — Lists and Indexing
# 3 problems. Target: 5-10 minutes total. Each has automatic PASS/FAIL.

# ── Problem 1 ─────────────────────────────────────────────────────────────────
# Concept: list indexing
# Given a list of numbers, return the element at index 2.

def get_index_2(lst):
    pass

r1 = get_index_2([10, 20, 30, 40, 50])
print("W01-P1 PASS" if r1 == 30 else f"W01-P1 FAIL — got {r1}, expected 30")

# ── Problem 2 ─────────────────────────────────────────────────────────────────
# Concept: negative indexing
# Given a list of (x, y, z) tuples, return the last element using a negative index.

def get_last(pts):
    pass

r2 = get_last([(1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (9.0, 9.0, 9.0)])
print("W01-P2 PASS" if r2 == (9.0, 9.0, 9.0) else f"W01-P2 FAIL — got {r2}")

# ── Problem 3 ─────────────────────────────────────────────────────────────────
# Concept: first and last indexing combined
# Given a list, return a tuple of (first_element, last_element).

def first_and_last(lst):
    pass

r3 = first_and_last([5, 10, 15, 20])
print("W01-P3 PASS" if r3 == (5, 20) else f"W01-P3 FAIL — got {r3}, expected (5, 20)")
