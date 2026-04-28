# Problem: Compare linear search vs binary search on 100 000 elements.
#          Time both over many queries and print the speedup.
# Concept: O(log n) vs O(n) is not just theory — binary search on 100k elements
#          needs at most 17 comparisons; linear scan needs up to 100k.
# You are done when:
#   [ ] Both searches return the same results
#   [ ] Binary search is significantly faster
#   [ ] All test cases print PASS
# Hint: Run 10000 queries; time both loops; binary search should be 100-10000x faster.

import time
import random


def binary_search(arr, target):
    """Paste your solution from problem 01 here."""
    pass


def linear_search(arr, target):
    """Return the index of target in arr, or -1."""
    pass


if __name__ == "__main__":
    random.seed(9)
    N = 100_000
    arr = sorted(random.sample(range(N * 10), N))
    targets = [random.choice(arr) for _ in range(5000)] + \
              [random.randint(0, N*10) for _ in range(5000)]
    random.shuffle(targets)

    t0 = time.time()
    linear_results = [linear_search(arr, t) for t in targets]
    linear_time = time.time() - t0

    t0 = time.time()
    binary_results = [binary_search(arr, t) for t in targets]
    binary_time = time.time() - t0

    ratio = linear_time / binary_time if binary_time > 0 else float("inf")
    print(f"Linear: {linear_time:.3f}s | Binary: {binary_time:.4f}s | Speedup: {ratio:.0f}x")
    print("PASS binary faster" if binary_time < linear_time else "FAIL binary not faster")
    print("PASS same results" if linear_results == binary_results else "FAIL result mismatch")
