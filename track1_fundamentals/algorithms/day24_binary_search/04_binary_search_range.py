# Problem: Given a sorted list of distances, use binary search to find all distances
#          within range [low, high] efficiently.
# Concept: Range query on a sorted array: find the leftmost index >= low and the
#          rightmost index <= high using two binary searches, then slice.
#          This is O(log n + k) vs O(n) linear scan.
# You are done when:
#   [ ] You use two binary searches: one for the left boundary, one for the right
#   [ ] You return the sublist (slice) between those boundaries
#   [ ] Result matches a linear scan reference
#   [ ] All test cases print PASS
# Hint: Find lo_idx = first index where arr[i] >= low; hi_idx = last index where arr[i] <= high.
#       Return arr[lo_idx:hi_idx+1].


def distances_in_range(sorted_distances, low, high):
    """
    Return all values in sorted_distances that fall within [low, high].
    Use two binary searches to find the boundaries.
    """
    pass


if __name__ == "__main__":
    dists = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

    r = distances_in_range(dists, 1.0, 3.0)
    print("PASS" if r == [1.0, 1.5, 2.0, 2.5, 3.0] else f"FAIL — {r}")

    r2 = distances_in_range(dists, 0.0, 0.3)
    print("PASS low" if r2 == [0.1] else f"FAIL low — {r2}")

    r3 = distances_in_range(dists, 5.0, 10.0)
    print("PASS empty" if r3 == [] else f"FAIL empty — {r3}")
