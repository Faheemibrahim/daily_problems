# Problem: Given a sequence of centroid lists (one per frame), use ConeTracker to track
#          cones across 10 frames. Print tracked positions vs raw detections each frame.
# Concept: Multi-frame tracking requires predict -> match -> update each frame.
#          For simplicity, use nearest-centroid matching (not Hungarian yet — that's day29).
# You are done when:
#   [ ] Each frame: predict_all, then greedily match detections to nearest tracked cone
#   [ ] Unmatched detections start new tracked cones
#   [ ] Estimates are printed alongside raw detections each frame
#   [ ] Final estimates are closer to true positions than raw noisy measurements
#   [ ] All test cases print PASS
# Hint: For each detection, find the nearest tracked cone by Euclidean distance;
#       if distance < threshold, update that cone; otherwise add as new cone.

import math
import random


class ConeTracker:
    def __init__(self):
        self.filters = {}
        self._next_id = 0

    def _new_id(self):
        cid = self._next_id; self._next_id += 1; return cid

    def add(self, x, y):
        cid = self._new_id()
        # Simple inline 2D filter
        self.filters[cid] = {"x": x, "y": y, "ux": 1.0, "uy": 1.0}
        return cid

    def predict_all(self, pn=0.05):
        for f in self.filters.values():
            f["ux"] += pn; f["uy"] += pn

    def update(self, cid, mx, my, mn=0.3):
        f = self.filters[cid]
        Kx = f["ux"] / (f["ux"] + mn); f["x"] += Kx * (mx - f["x"]); f["ux"] *= (1 - Kx)
        Ky = f["uy"] / (f["uy"] + mn); f["y"] += Ky * (my - f["y"]); f["uy"] *= (1 - Ky)

    def get_estimates(self):
        return {cid: (f["x"], f["y"]) for cid, f in self.filters.items()}


def run_tracking(frame_detections, match_threshold=1.0):
    """
    Track cones across multiple frames.
    frame_detections: list of lists, each inner list is [(x, y), ...] detections for that frame.
    Return the final estimates dict.
    """
    pass


if __name__ == "__main__":
    random.seed(3)
    # Two true cones at (2, 0) and (-2, 0), 10 frames of noisy detections
    true_cones = [(2.0, 0.0), (-2.0, 0.0)]
    frames = [
        [(x + random.gauss(0, 0.15), y + random.gauss(0, 0.15)) for x, y in true_cones]
        for _ in range(10)
    ]

    final_ests = run_tracking(frames)

    print(f"Tracked {len(final_ests)} cone(s)")
    print("PASS 2 cones" if len(final_ests) == 2 else f"FAIL — {len(final_ests)} tracked")

    errors = [math.sqrt((ex - tx)**2 + (ey - ty)**2)
              for (ex, ey), (tx, ty) in zip(sorted(final_ests.values()), sorted(true_cones))]
    print(f"Final errors: {[f'{e:.3f}' for e in errors]}")
    print("PASS accurate" if all(e < 0.3 for e in errors) else f"FAIL errors — {errors}")
