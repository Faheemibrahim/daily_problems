# Problem: Add a ConeTracker that maintains cone positions across multiple pipeline calls.
# Concept: The final architecture: each frame runs detect_cones, then match_centroids,
#          then update the tracker. The tracker publishes smoothed cone positions.
#          This is the shape of the real autonomy node.
# You are done when:
#   [ ] ConeTracker is created once and survives across frame calls
#   [ ] Each frame: run pipeline, extract 2D centroids, call tracker.process_frame
#   [ ] Tracked estimates are returned alongside raw detections
#   [ ] Estimates stabilise (stop jumping) after a few frames
#   [ ] All test cases print PASS
# Hint: tracker.process_frame(detections_2d) handles predict+match+update internally.

import math
import random
import numpy as np
from collections import deque
from scipy.spatial import KDTree
from scipy.optimize import linear_sum_assignment


class ConeTracker:
    def __init__(self, max_dist=1.0, pn=0.05, mn=0.2):
        self.filters = {}; self._nid = 0; self.max_dist = max_dist; self.pn = pn; self.mn = mn

    def _kf(self, x, y):
        return {"x": x, "y": y, "ux": 1.0, "uy": 1.0}

    def _predict_one(self, f):
        f["ux"] += self.pn; f["uy"] += self.pn

    def _update_one(self, f, mx, my):
        Kx = f["ux"]/(f["ux"]+self.mn); f["x"] += Kx*(mx-f["x"]); f["ux"] *= (1-Kx)
        Ky = f["uy"]/(f["uy"]+self.mn); f["y"] += Ky*(my-f["y"]); f["uy"] *= (1-Ky)

    def process_frame(self, detections_2d):
        for f in self.filters.values(): self._predict_one(f)
        if not self.filters:
            for x, y in detections_2d: self.filters[self._nid] = self._kf(x, y); self._nid += 1
            return
        ids = list(self.filters.keys())
        old_pos = [(self.filters[cid]["x"], self.filters[cid]["y"]) for cid in ids]
        if not detections_2d: return
        cost = np.array([[math.sqrt((ox-nx)**2+(oy-ny)**2) for nx,ny in detections_2d]
                         for ox,oy in old_pos])
        rows, cols = linear_sum_assignment(cost)
        matched_new = set()
        for r, c in zip(rows, cols):
            if cost[r, c] <= self.max_dist:
                self._update_one(self.filters[ids[r]], *detections_2d[c]); matched_new.add(c)
        for j, (x, y) in enumerate(detections_2d):
            if j not in matched_new: self.filters[self._nid] = self._kf(x, y); self._nid += 1

    def get_estimates(self):
        return {cid: (f["x"], f["y"]) for cid, f in self.filters.items()}


def detect_cones_simple(raw_points, z_min=-0.5, z_max=0.3, xy_range=5.0,
                         voxel_size=0.1, epsilon=0.3, min_size=5, max_size=200,
                         max_x_span=1.0, max_y_span=1.0, max_z_span=0.8):
    """
    Run the detection pipeline (from problem 01) and return list of cone dicts.
    Paste your detect_cones() implementation here.
    """
    pass


def run_pipeline_with_tracker(frame_raw_points_list):
    """
    Process a sequence of raw point clouds with a persistent ConeTracker.
    Return the final tracker estimates.
    """
    pass


if __name__ == "__main__":
    random.seed(1)

    def make_cone(cx, cy, n=25):
        return [(cx+random.gauss(0,0.05), cy+random.gauss(0,0.05), random.uniform(0.0,0.3)) for _ in range(n)]

    true_cones = [(2.0, 0.5), (-2.0, 0.5), (0.0, 3.0)]
    frames = [make_cone(*c) for c in true_cones for _ in range(1)]
    # 10 frames of the same scene with slight noise variation
    all_frames = []
    for _ in range(10):
        frame = []
        for cx, cy in true_cones:
            frame += [(cx+random.gauss(0,0.05), cy+random.gauss(0,0.05), random.uniform(0.0,0.3)) for _ in range(25)]
        all_frames.append(frame)

    final_ests = run_pipeline_with_tracker(all_frames)
    print(f"Tracked {len(final_ests)} cone(s)")
    print("PASS 3 cones" if len(final_ests) == 3 else f"FAIL — {len(final_ests)}")
