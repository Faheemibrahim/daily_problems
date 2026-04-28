# Problem: Time all four sorts plus Python's built-in sorted() on 10000 elements.
#          Print a comparison table of all five times.
# Concept: Empirical timing confirms what Big-O analysis predicts: bubble/insertion are
#          dramatically slower than merge/quick for large N. Always measure, never guess.
# You are done when:
#   [ ] All five sorts produce identical results (verify this!)
#   [ ] Times are printed in a readable table
#   [ ] sorted() and merge_sort/quick_sort are all significantly faster than bubble/insertion
#   [ ] All test cases print PASS
# Hint: Use time.time() before/after each sort call; sort a fresh copy each time.

import time
import random


def bubble_sort(arr):
    """Paste your solution from problem 01."""
    pass

def insertion_sort(arr):
    """Paste your solution from problem 02."""
    pass

def merge_sort(arr):
    """Paste your solution from problem 03."""
    pass

def quick_sort(arr):
    """Paste your solution from problem 04."""
    pass


if __name__ == "__main__":
    random.seed(42)
    data = [random.randint(0, 100_000) for _ in range(10_000)]

    results = {}
    times = {}
    for name, fn in [("bubble", bubble_sort), ("insertion", insertion_sort),
                     ("merge", merge_sort), ("quick", quick_sort), ("builtin", sorted)]:
        copy = data[:]
        t0 = time.time()
        results[name] = fn(copy) if name not in ("bubble", "insertion") else (fn(copy), copy)[1]
        times[name] = time.time() - t0

    # bubble and insertion sort in place, others return new list
    reference = sorted(data)
    print("\n=== Sort timing (N=10000) ===")
    for name in ["bubble", "insertion", "merge", "quick", "builtin"]:
        t = times[name]
        r = results[name] if results[name] is not None else "?"
        ok = (bubble_sort([3,1,2]) == [1,2,3])  # placeholder — check your impl
        print(f"{name:12s}: {t:.4f}s")
    print()
    print("PASS all sorted correctly" if all(
        sorted(data) == (results[n] if results[n] else data) for n in times
    ) else "FAIL some sorts incorrect — check implementations")
    slow_ok = times["bubble"] > times["builtin"] or times["insertion"] > times["builtin"]
    print("PASS builtin fastest" if times["builtin"] == min(times.values()) else "NOTE builtin not fastest (check)")
