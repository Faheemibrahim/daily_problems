# Problem: Given two lists of point indices, find which indices appear in both
#          using set intersection.
# Concept: Set intersection as a fast way to find common elements between two collections.
# You are done when:
#   [ ] You convert both lists to sets
#   [ ] You use the & operator or .intersection() method
#   [ ] The result is the set of common indices
#   [ ] All test cases print PASS
# Hint: set_a & set_b returns a new set of elements that appear in both.


def common_indices(list_a, list_b):
    """
    Return the set of indices that appear in both list_a and list_b.
    """
    pass


if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7, 8]
    result = common_indices(a, b)
    expected = {3, 4, 5}
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    a2 = [1, 2, 3]
    b2 = [4, 5, 6]
    result2 = common_indices(a2, b2)
    print("PASS empty" if result2 == set() else f"FAIL empty — got {result2}")
