# Problem: Loop through two lists simultaneously using zip() and collect matching pairs.
# Concept: zip() lets you iterate over two (or more) sequences in lockstep.
# You are done when:
#   [ ] You use zip() — not manual index tracking
#   [ ] You collect each (a, b) pair from the two lists into a result list
#   [ ] You understand that zip stops at the shorter list
#   [ ] All test cases print PASS
# Hint: for a, b in zip(list_a, list_b) unpacks each pair directly.


def zip_pairs(labels, points):
    """
    Return a list of (label, point) tuples by zipping labels and points together.
    """

    store = []

    for labels, points in zip(labels,points):
        store.append((labels,points))
    
    #print(store)
    return store

if __name__ == "__main__":
    labels = ["cone_a", "cone_b", "cone_c"]
    pts = [(1.0, 0.0, 0.0), (2.0, 1.0, 0.0), (3.0, -1.0, 0.0)]
    result = zip_pairs(labels, pts)
    expected = [("cone_a", (1.0, 0.0, 0.0)), ("cone_b", (2.0, 1.0, 0.0)), ("cone_c", (3.0, -1.0, 0.0))]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    # zip stops at shorter list
    result2 = zip_pairs(["a", "b"], [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0), (2.0, 2.0, 2.0)])
    expected2 = [("a", (0.0, 0.0, 0.0)), ("b", (1.0, 1.0, 1.0))]
    print("PASS" if result2 == expected2 else f"FAIL — got {result2}, expected {expected2}")
