# Problem: Write fibonacci(n) recursively, then iteratively. Compare performance on n=35.
# Concept: Naive recursive fibonacci is O(2^n) — exponential — because it recomputes
#          the same subproblems. Iterative is O(n). This is the canonical example of
#          why memoisation and dynamic programming exist.
# You are done when:
#   [ ] Both implementations return the same values
#   [ ] The iterative version is dramatically faster for n=35
#   [ ] You can explain WHY the recursive version is slow (recomputation)
#   [ ] All test cases print PASS
# Hint: Iterative: maintain two variables (a, b) and loop n times, updating: a, b = b, a+b

import time


def fibonacci_recursive(n):
    """Return the n-th Fibonacci number recursively (0-indexed: fib(0)=0, fib(1)=1)."""
    pass


def fibonacci_iterative(n):
    """Return the n-th Fibonacci number iteratively."""
    pass


if __name__ == "__main__":
    for n in [0, 1, 5, 10]:
        r = fibonacci_recursive(n)
        i = fibonacci_iterative(n)
        print(f"PASS fib({n})" if r == i else f"FAIL fib({n}) — recursive={r}, iterative={i}")

    N = 35
    t0 = time.time(); rec = fibonacci_recursive(N); rec_time = time.time() - t0
    t0 = time.time(); it = fibonacci_iterative(N); it_time = time.time() - t0
    print(f"fib({N}) = {rec} | recursive: {rec_time:.3f}s | iterative: {it_time:.6f}s")
    print("PASS iterative much faster" if it_time * 100 < rec_time else "FAIL — iterative should be faster")
