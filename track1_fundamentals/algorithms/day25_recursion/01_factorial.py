# Problem: Write factorial(n) recursively.
# Concept: Recursion = a function that calls itself with a smaller input + a base case.
#          Factorial is the simplest example: n! = n * (n-1)! with 0! = 1.
# You are done when:
#   [ ] Base case handles n == 0 (returns 1)
#   [ ] Recursive case calls factorial(n-1) and multiplies by n
#   [ ] Raises or handles negative inputs gracefully
#   [ ] All test cases print PASS
# Hint: if n == 0: return 1 — every recursive function must have at least one base case.


def factorial(n):
    """Return n! recursively. n must be a non-negative integer."""
    pass


if __name__ == "__main__":
    print("PASS 0!" if factorial(0) == 1 else f"FAIL 0! — {factorial(0)}")
    print("PASS 1!" if factorial(1) == 1 else f"FAIL 1! — {factorial(1)}")
    print("PASS 5!" if factorial(5) == 120 else f"FAIL 5! — {factorial(5)}")
    print("PASS 10!" if factorial(10) == 3628800 else f"FAIL 10! — {factorial(10)}")
