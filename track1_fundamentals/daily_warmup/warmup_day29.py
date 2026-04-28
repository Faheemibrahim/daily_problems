# Warmup Day 29 — Hungarian Algorithm retention
# Topics: 3×3 cost matrix scipy assignment, reject pairs > 1.0, Kalman retention
# Fill in each block so all PASS lines print.

import math
import random
import numpy as np
from scipy.optimize import linear_sum_assignment

# ── 1. Optimal assignment on a 3×3 cost matrix ───────────────────────────────
cost = np.array([
    [4.0, 1.0, 3.0],
    [2.0, 0.0, 5.0],
    [3.0, 2.0, 2.0],
])
rows, cols = linear_sum_assignment(cost)
total_cost = cost[rows, cols].sum()
# Optimal: row0→col1 (1.0), row1→col1? No — unique cols.
# row0→col1(1.0), row1→col0(2.0), row2→col2(2.0) = 5.0
print("PASS hungarian" if abs(total_cost - 5.0) < 1e-9
      else f"FAIL hungarian — total={total_cost}, assignments={(list(zip(rows.tolist(),cols.tolist())))}")

# ── 2. Reject matched pairs whose cost > 1.0 ─────────────────────────────────
detections = [(0.0,0.0), (5.0,5.0), (2.0,2.0)]
tracks     = [(0.1,0.1), (5.1,5.1), (9.0,9.0)]
cost2 = np.array([[math.dist(t, d) for d in detections] for t in tracks])
rows2, cols2 = linear_sum_assignment(cost2)
matched = [(tracks[r], detections[c]) for r, c in zip(rows2, cols2) if cost2[r,c] <= 1.0]
# Pair (0.0,0.0)↔(0.1,0.1) and (5.0,5.0)↔(5.1,5.1) are within 1.0; third is not
print("PASS reject_far" if len(matched) == 2 else f"FAIL reject_far — {len(matched)} pairs")

# ── 3. Kalman filter retention — estimate converges to true value ─────────────
class KF1D:
    def __init__(self, x0, u0, pn=0.05, mn=0.2):
        self.x=x0; self.u=u0; self.pn=pn; self.mn=mn
    def predict(self): self.u += self.pn
    def update(self, z):
        K = self.u/(self.u+self.mn); self.x += K*(z-self.x); self.u *= (1-K)

kf = KF1D(0.0, 1.0)
random.seed(3)
true_x = 2.5
for _ in range(8):
    kf.predict(); kf.update(true_x + random.gauss(0, 0.2))
print("PASS kalman_retention" if abs(kf.x - true_x) < 0.5
      else f"FAIL kalman_retention — {kf.x:.3f}")
