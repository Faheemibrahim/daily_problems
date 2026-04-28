# Problem: Write match_centroids(old_centroids, new_centroids, max_dist=1.0) that uses
#          scipy Hungarian and rejects pairs further than max_dist apart.
#          Return (matched_pairs, unmatched_new) where unmatched_new are new cones.
# Concept: This is the real pairing logic used between frames in a tracking system.
#          max_dist prevents matching a cone to a detection on the other side of the track.
#          Unmatched new detections become new tracked cones.
# You are done when:
#   [ ] You build a cost matrix of pairwise distances
#   [ ] You run Hungarian assignment
#   [ ] You reject pairs where distance > max_dist
#   [ ] Unmatched new detections are returned separately
#   [ ] All test cases print PASS
# Hint: Build cost matrix, run linear_sum_assignment, then filter by distance threshold.

import math
import numpy as np
from scipy.optimize import linear_sum_assignment


def match_centroids(old_centroids, new_centroids, max_dist=1.0):
    """
    Match old centroids to new centroids using Hungarian algorithm.
    old_centroids: list of (x, y) tuples
    new_centroids: list of (x, y) tuples
    Return (matched_pairs, unmatched_new_indices)
    where matched_pairs = list of (old_idx, new_idx) tuples with distance <= max_dist
    and unmatched_new_indices = list of new_centroid indices with no valid match.
    """
    pass


if __name__ == "__main__":
    old = [(0.0, 0.0), (3.0, 0.0), (6.0, 0.0)]
    new = [(0.1, 0.05), (3.0, 0.1), (6.1, -0.1), (10.0, 0.0)]  # 3 close, 1 new

    pairs, unmatched = match_centroids(old, new, max_dist=1.0)
    print(f"Matched pairs: {pairs}")
    print(f"Unmatched new: {unmatched}")
    print("PASS 3 pairs" if len(pairs) == 3 else f"FAIL pairs — {len(pairs)}")
    print("PASS 1 unmatched" if len(unmatched) == 1 else f"FAIL unmatched — {len(unmatched)}")
    print("PASS unmatched is far one" if 3 in unmatched else f"FAIL unmatched idx — {unmatched}")
