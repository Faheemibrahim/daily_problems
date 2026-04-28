# Problem: Given a list of (x, y, z) tuples that may contain duplicates, remove
#          duplicates using a set. Return results in a consistent order.
# Concept: Sets eliminate duplicates automatically because they require hashable,
#          unique elements — tuples of floats are hashable.
# You are done when:
#   [ ] You use a set to deduplicate
#   [ ] You return the unique points as a sorted list for deterministic output
#   [ ] All test cases print PASS
# Hint: set(list_of_tuples) removes duplicates; sorted() gives a stable order.


def remove_duplicates(points):
    """
    Return a sorted list of unique (x, y, z) tuples from points.
    """
    pass


if __name__ == "__main__":
    pts = [
        (1.0, 0.0, 0.0),
        (2.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (3.0, 0.0, 0.0),
        (2.0, 0.0, 0.0),
    ]
    result = remove_duplicates(pts)
    expected = [(1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (3.0, 0.0, 0.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
