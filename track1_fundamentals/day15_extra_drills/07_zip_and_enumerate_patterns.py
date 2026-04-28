# Problem: Three zip/enumerate sub-problems:
#   1. Pair two centroid lists from frame1 and frame2 using zip, print each pair with its index.
#   2. Assign each cluster an ID using enumerate and store as list of dicts.
#   3. Using zip, find centroid pairs across two frames that are within distance 0.5.
# Concept: zip and enumerate are the idiomatic replacements for range(len()) when
#          you need indices or want to walk two sequences in lockstep.
# You are done when:
#   [ ] Problem 1 uses zip and enumerate together — no range(len())
#   [ ] Problem 2 uses enumerate to assign IDs — no manual counter
#   [ ] Problem 3 pairs frames with zip and filters by distance — no index math
#   [ ] All test cases print PASS
# Hint: for i, (a, b) in enumerate(zip(list_a, list_b)) combines both in one loop.

import math


def print_centroid_pairs(frame1, frame2):
    """
    Return a list of strings: "pair {i}: {c1} -> {c2}" for each matched pair.
    Use zip and enumerate together.
    """
    pass


def assign_ids(clusters):
    """
    Given a list of (centroid, size) tuples, return a list of dicts
    {'id': i, 'centroid': centroid, 'size': size} using enumerate.
    """
    pass


def find_close_pairs(old_centroids, new_centroids, max_dist=0.5):
    """
    Return a list of (old, new) pairs where distance between centroids <= max_dist.
    Use zip — no index arithmetic.
    """
    pass


if __name__ == "__main__":
    f1 = [(0.0, 0.0, 0.0), (3.0, 0.0, 0.0)]
    f2 = [(0.1, 0.0, 0.0), (3.5, 0.0, 0.0)]

    pairs = print_centroid_pairs(f1, f2)
    print("PASS pairs len" if len(pairs) == 2 else f"FAIL pairs len — {pairs}")
    print("PASS pairs idx" if "pair 0:" in pairs[0] else f"FAIL pairs fmt — {pairs[0]}")

    raw_clusters = [((1.0, 2.0, 0.0), 5), ((3.0, 4.0, 0.0), 8)]
    result = assign_ids(raw_clusters)
    print("PASS assign ids" if result[0]["id"] == 0 and result[1]["id"] == 1
          else f"FAIL assign ids — {result}")

    close = find_close_pairs(f1, f2, max_dist=0.5)
    print("PASS close pairs" if len(close) == 2 else f"FAIL close pairs — {close}")

    far_f2 = [(0.1, 0.0, 0.0), (10.0, 0.0, 0.0)]
    close2 = find_close_pairs(f1, far_f2, max_dist=0.5)
    print("PASS one close" if len(close2) == 1 else f"FAIL one close — {close2}")
