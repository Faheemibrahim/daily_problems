# Problem: Integrate match_centroids into ConeTracker so it correctly pairs new
#          detections to existing cones using Hungarian assignment instead of greedy nearest.
# Concept: This completes the tracking loop: detect -> match (Hungarian) -> update (Kalman).
#          Greedy matching breaks when two cones pass close to each other; Hungarian doesn't.
# You are done when:
#   [ ] ConeTracker.process_frame(detections) calls predict_all, then match_centroids,
#       then updates matched cones, then adds unmatched detections as new cones
#   [ ] Tracked cone estimates are accurate after 10 frames
#   [ ] All test cases print PASS
# Hint: Use match_centroids to get (old_idx, new_idx) pairs; map old_idx to cone_id via a list.

import math
import random
import numpy as np
from scipy.optimize import linear_sum_assignment


def match_centroids(old_centroids, new_centroids, max_dist=1.0):
    if not old_centroids or not new_centroids:
        return [], list(range(len(new_centroids)))
    cost = np.array([[math.sqrt((ox-nx)**2 + (oy-ny)**2)
                      for nx, ny in new_centroids] for ox, oy in old_centroids])
    rows, cols = linear_sum_assignment(cost)
    pairs = [(r, c) for r, c in zip(rows, cols) if cost[r, c] <= max_dist]
    matched_new = {c for _, c in pairs}
    unmatched = [j for j in range(len(new_centroids)) if j not in matched_new]
    return pairs, unmatched


class ConeTracker:
    """
    Full cone tracker: Hungarian matching + Kalman filtering.
    """

    def __init__(self, max_dist=1.0, process_noise=0.05, measurement_noise=0.2):
        pass

    def process_frame(self, detections):
        """
        detections: list of (x, y) tuples — new cone positions this frame.
        1. predict_all
        2. match_centroids(old_estimates, detections)
        3. update matched, add unmatched as new cones
        """
        pass

    def get_estimates(self):
        """Return {cone_id: (est_x, est_y)}."""
        pass


if __name__ == "__main__":
    random.seed(7)
    tracker = ConeTracker(max_dist=1.0)

    true_cones = [(2.0, 1.0), (-2.0, 1.0), (0.0, 3.0)]

    for frame in range(15):
        detections = [(x + random.gauss(0, 0.1), y + random.gauss(0, 0.1)) for x, y in true_cones]
        tracker.process_frame(detections)

    ests = tracker.get_estimates()
    print(f"Tracked {len(ests)} cone(s)")
    print("PASS 3 cones" if len(ests) == 3 else f"FAIL — {len(ests)}")

    est_vals = sorted(ests.values())
    true_vals = sorted(true_cones)
    errors = [math.sqrt((ex-tx)**2 + (ey-ty)**2) for (ex,ey),(tx,ty) in zip(est_vals, true_vals)]
    print(f"Errors: {[f'{e:.3f}' for e in errors]}")
    print("PASS all accurate" if all(e < 0.3 for e in errors) else f"FAIL errors — {errors}")
