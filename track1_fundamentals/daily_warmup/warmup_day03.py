# Warmup Day 03 — Lists + Loops + List Comprehensions
# 4 problems. Target: 5-10 minutes total.

# ── Problem 1 (Lists) ────────────────────────────────────────────────────────
# Concept: negative index
# Return the second-to-last element of a list.

def second_to_last(lst):
    pass

r1 = second_to_last([1, 2, 3, 4, 5])
print("W03-P1 PASS" if r1 == 4 else f"W03-P1 FAIL — got {r1}")

# ── Problem 2 (Loops) ────────────────────────────────────────────────────────
# Concept: counting in a loop
# Count how many elements in a list are > 10 using a for loop.

def count_gt10(numbers):
    pass

r2 = count_gt10([5, 11, 3, 20, 10, 15])
print("W03-P2 PASS" if r2 == 3 else f"W03-P2 FAIL — got {r2}")

# ── Problem 3 (Comprehensions) ───────────────────────────────────────────────
# Concept: filter comprehension
# Return only the even numbers from a list using a comprehension.

def evens(numbers):
    pass

r3 = evens([1, 2, 3, 4, 5, 6])
print("W03-P3 PASS" if r3 == [2, 4, 6] else f"W03-P3 FAIL — got {r3}")

# ── Problem 4 (Comprehensions) ───────────────────────────────────────────────
# Concept: transform comprehension
# Double every value in a list using a comprehension.

def double_all(numbers):
    pass

r4 = double_all([1, 2, 3])
print("W03-P4 PASS" if r4 == [2, 4, 6] else f"W03-P4 FAIL — got {r4}")
