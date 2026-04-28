# Problem: Loop through a dict using .items() and return a list of "key: value" strings.
# Concept: Dict iteration with .items(), yielding key-value pairs in insertion order.
# You are done when:
#   [ ] You use .items() — not .keys() + separate lookup
#   [ ] Each entry is formatted as "name: (x, y, z)"
#   [ ] All test cases print PASS
# Hint: for key, value in d.items() unpacks each key-value pair directly.


def format_dict(d):
    """
    Return a list of strings formatted as "key: value" for each item in d.
    """
    pass


if __name__ == "__main__":
    cones = {"A": (1.0, 0.0, 0.0), "B": (2.0, 1.0, 0.0), "C": (3.0, -1.0, 0.0)}
    result = format_dict(cones)
    expected = [
        "A: (1.0, 0.0, 0.0)",
        "B: (2.0, 1.0, 0.0)",
        "C: (3.0, -1.0, 0.0)",
    ]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
