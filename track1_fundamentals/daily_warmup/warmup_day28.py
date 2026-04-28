# Warmup Day 28 — Kalman Filter retention
# Topics: 5-step 1D Kalman, predict then update, clustering retention
# Fill in each block so all PASS lines print.

import random
import math
from collections import deque
from scipy.spatial import KDTree
import numpy as np

# ── 1. 5-step 1D Kalman filter ────────────────────────────────────────────────
class KF1D:
    def __init__(self, x0, u0, process_noise=0.05, meas_noise=0.5):
        self.x = x0; self.u = u0; self.pn = process_noise; self.mn = meas_noise
    def predict(self):
        self.u += self.pn
    def update(self, z):
        K = self.u / (self.u + self.mn)
        self.x += K * (z - self.x)
        self.u *= (1 - K)

kf = KF1D(x0=0.0, u0=1.0)
true_pos = 3.0
random.seed(5)
for _ in range(5):
    kf.predict()
    kf.update(true_pos + random.gauss(0, 0.5))

print("PASS kalman_1d" if abs(kf.x - true_pos) < 1.0
      else f"FAIL kalman_1d — estimate={kf.x:.3f}, true={true_pos}")

# ── 2. Single predict-update cycle ────────────────────────────────────────────
kf2 = KF1D(x0=0.0, u0=1.0, process_noise=0.05, meas_noise=0.2)
kf2.predict()
u_after_predict = kf2.u
kf2.update(5.0)
x_after_update = kf2.x
# After update toward z=5.0 from x=0.0, estimate should move toward 5.0
print("PASS predict_update" if x_after_update > 0.0 and kf2.u < u_after_predict
      else f"FAIL predict_update — x={x_after_update:.3f}, u={kf2.u:.3f}")

# ── 3. Clustering retention — 2 groups of points ─────────────────────────────
random.seed(1)
a = [(random.gauss(0,0.05), random.gauss(0,0.05), 0.0) for _ in range(8)]
b = [(random.gauss(4,0.05), random.gauss(0,0.05), 0.0) for _ in range(8)]
pts = a + b
arr = np.array(pts); tree = KDTree(arr)
visited = set(); clusters = []
for i in range(len(pts)):
    if i in visited: continue
    comp = []; q = deque([i]); visited.add(i)
    while q:
        cur = q.popleft(); comp.append(pts[cur])
        for nb in tree.query_ball_point(pts[cur], r=0.3):
            if nb not in visited: visited.add(nb); q.append(nb)
    clusters.append(comp)
print("PASS clustering_retention" if len(clusters) == 2
      else f"FAIL clustering_retention — {len(clusters)}")
