# Problem: Reverse a list of points using slicing — no .reverse() or reversed().
# Concept: The [::-1] slice idiom as a concise way to reverse any sequence.
# You are done when:
#   [ ] The result is a new list in reverse order
#   [ ] You use slice notation, not a loop or .reverse()
#   [ ] The original list is not modified
#   [ ] All test cases print PASS
# Hint: list[::-1] creates a shallow copy of the list in reversed order.


def reverse_points(points):
    """
    Return a new list that is the reverse of points, using slicing.
    """
   
    print(points[::-1])
    return points[::-1]






if __name__ == "__main__":
    pts = [(1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (3.0, 0.0, 0.0)]
    result = reverse_points(pts)
    expected = [(3.0, 0.0, 0.0), (2.0, 0.0, 0.0), (1.0, 0.0, 0.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    original = pts[:]
    _ = reverse_points(pts)
    print("PASS original unchanged" if pts == original else "FAIL original was modified")
