# Warmup Day 22 — KD-Tree Applications retention
# Topics: time kdtree vs brute, scipy KDTree, numpy distance retention
# Fill in each block so all PASS lines print.

import math
import time
import random
import numpy as np
from scipy.spatial import KDTree

random.seed(42)

# ── 1. Time kdtree build vs brute force nearest neighbour ────────────────────
N = 500
pts = [(random.uniform(-10,10), random.uniform(-10,10)) for _ in range(N)]
query = (0.0, 0.0)

t0 = time.time()
brute_nn = min(pts, key=lambda p: math.dist(p, query))
t_brute = time.time() - t0

arr = np.array(pts)
t0 = time.time()
kd = KDTree(arr)
_, idx = kd.query(query)
kd_nn = tuple(arr[idx])
t_kd_build_query = time.time() - t0

print("PASS timing_ran" if t_brute >= 0 and t_kd_build_query >= 0 else "FAIL timing_ran")

# ── 2. scipy KDTree radius search ─────────────────────────────────────────────
pts2 = np.array([(0.0,0.0), (0.5,0.5), (1.0,1.0), (3.0,3.0), (0.3,0.8)])
kd2 = KDTree(pts2)
indices = kd2.query_ball_point((0.0, 0.0), r=1.0)
within = pts2[indices]
expected_count = sum(1 for p in pts2 if math.dist(p, (0.0,0.0)) <= 1.0)
print("PASS scipy_radius" if len(within) == expected_count
      else f"FAIL scipy_radius — got {len(within)}, expected {expected_count}")

# ── 3. Numpy distance retention — pairwise distances via broadcasting ─────────
a = np.array([[0.0,0.0,0.0], [1.0,0.0,0.0], [0.0,1.0,0.0]])
diffs = a[:, None, :] - a[None, :, :]
dists = np.sqrt((diffs**2).sum(axis=2))
print("PASS numpy_dist" if abs(dists[0,1] - 1.0) < 1e-9 and abs(dists[0,2] - 1.0) < 1e-9
      else f"FAIL numpy_dist — {dists}")
