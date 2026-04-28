# Problem: Rewrite the visited logic from Euclidean clustering in isolation —
#          just the visited set: add, check membership, and collect unvisited points.
# Concept: The visited-set pattern is the heart of BFS-based clustering. Getting it
#          right here means you will not trip over it when the full algorithm appears.
# You are done when:
#   [ ] You correctly skip points already in the visited set
#   [ ] You process each unvisited point in index order
#   [ ] The returned list has no duplicates and preserves order of first visit
#   [ ] All test cases print PASS
# Hint: Maintain a set of visited indices and a list of results; check before appending.


def process_unvisited(points):
    """
    Simulate visiting each point by index. Skip already-visited points.
    Return the list of points in the order they were first visited,
    where a point is considered a duplicate if an identical (x, y, z) was seen before.
    """
    pass


if __name__ == "__main__":
    pts = [
        (1.0, 0.0, 0.0),
        (2.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),  # duplicate
        (3.0, 0.0, 0.0),
        (2.0, 0.0, 0.0),  # duplicate
    ]
    result = process_unvisited(pts)
    expected = [(1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (3.0, 0.0, 0.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
