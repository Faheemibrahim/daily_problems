# Problem: Three error-handling sub-problems:
#   1. centroid(points) raises ValueError with a clear message if points is empty.
#   2. safe_divide(a, b) returns None if b is zero instead of crashing.
#   3. safe_call(func, *args) wraps a call in try/except, logs the error, returns None on failure.
# Concept: try/except and raise let you control failure modes explicitly.
#          Silent failures (returning wrong values) are worse than loud ones (exceptions).
# You are done when:
#   [ ] centroid([]) raises ValueError — not returns None or crashes with ZeroDivisionError
#   [ ] safe_divide(5, 0) returns None without raising
#   [ ] safe_call(bad_func, ...) catches the exception, prints a message, returns None
#   [ ] All test cases print PASS
# Hint: raise ValueError("message") inside an if-check at the top of the function.


def centroid(points):
    """
    Return (mean_x, mean_y, mean_z). Raise ValueError if points is empty.
    """
    pass


def safe_divide(a, b):
    """
    Return a / b, or None if b is zero.
    """
    pass


def safe_call(func, *args):
    """
    Call func(*args). If it raises any exception, print the error and return None.
    """
    pass


if __name__ == "__main__":
    # centroid raises on empty
    try:
        centroid([])
        print("FAIL centroid empty — should have raised ValueError")
    except ValueError as e:
        print(f"PASS centroid empty — raised ValueError: {e}")

    # centroid works normally
    c = centroid([(0.0, 0.0, 0.0), (2.0, 0.0, 0.0)])
    print("PASS centroid normal" if c == (1.0, 0.0, 0.0) else f"FAIL centroid normal — {c}")

    # safe_divide
    print("PASS safe_divide zero" if safe_divide(5, 0) is None else "FAIL safe_divide zero")
    print("PASS safe_divide normal" if safe_divide(10, 2) == 5.0 else f"FAIL safe_divide — {safe_divide(10, 2)}")

    # safe_call
    def bad(): raise RuntimeError("something went wrong")
    result = safe_call(bad)
    print("PASS safe_call" if result is None else f"FAIL safe_call — {result}")

    result2 = safe_call(lambda: 42)
    print("PASS safe_call success" if result2 == 42 else f"FAIL safe_call success — {result2}")
