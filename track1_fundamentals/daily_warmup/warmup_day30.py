# Warmup Day 30 — Full Pipeline retention
# Topics: full pipeline on 100 points, verify cone detected, Hungarian retention
# Fill in each block so all PASS lines print.

import math
import random
import numpy as np
from collections import deque
from scipy.spatial import KDTree
from scipy.optimize import linear_sum_assignment

random.seed(42)

# ── 1. Mini full pipeline on 100 points with one cone ────────────────────────
ground = [(random.uniform(-5,5), random.uniform(-5,5), random.gauss(0,0.02)) for _ in range(75)]
cone   = [(random.gauss(2.0,0.05), random.gauss(0.0,0.05), random.uniform(0.05,0.3)) for _ in range(25)]
raw = ground + cone

# Step 1: bbox filter
arr = np.array(raw)
mask = ((arr[:,2] >= -0.1) & (arr[:,2] <= 0.35) &
        (np.abs(arr[:,0]) <= 5.0) & (np.abs(arr[:,1]) <= 5.0))
filtered = arr[mask]

# Step 2: voxel downsample (voxel_size=0.1)
voxel_size = 0.1
vd = {}
for p in filtered:
    key = (int(p[0]//voxel_size), int(p[1]//voxel_size), int(p[2]//voxel_size))
    vd.setdefault(key, []).append(tuple(p))
downsampled = [tuple(sum(q[i] for q in v)/len(v) for i in range(3)) for v in vd.values()]

# Step 3: clustering
ds_arr = np.array(downsampled)
tree = KDTree(ds_arr)
visited = set(); clusters = []
for i in range(len(downsampled)):
    if i in visited: continue
    comp = []; q = deque([i]); visited.add(i)
    while q:
        cur = q.popleft(); comp.append(downsampled[cur])
        for nb in tree.query_ball_point(downsampled[cur], r=0.3):
            if nb not in visited: visited.add(nb); q.append(nb)
    clusters.append(comp)

# Step 4: size filter
sized = [c for c in clusters if 3 <= len(c) <= 200]

# Step 5: dimension filter + to dicts
result = []
for i, cl in enumerate(sized):
    xs = [p[0] for p in cl]; ys = [p[1] for p in cl]; zs = [p[2] for p in cl]
    if max(xs)-min(xs) < 1.0 and max(ys)-min(ys) < 1.0 and max(zs)-min(zs) < 0.8:
        n = len(cl)
        result.append({"id": i, "size": n,
                        "centroid": (sum(xs)/n, sum(ys)/n, sum(zs)/n)})

print("PASS pipeline" if len(result) >= 1 else f"FAIL pipeline — {len(result)} detections")

# ── 2. Verify the detected cone is near (2.0, 0.0) ───────────────────────────
if result:
    cx, cy, _ = result[0]["centroid"]
    near_cone = math.dist((cx,cy), (2.0,0.0)) < 0.5
    print("PASS cone_position" if near_cone
          else f"FAIL cone_position — centroid at ({cx:.2f},{cy:.2f})")
else:
    print("FAIL cone_position — no detection")

# ── 3. Hungarian retention — assign 2 detections to 2 tracks ────────────────
tracks =     [(1.0, 0.0), (4.0, 0.0)]
detections = [(1.1, 0.1), (3.9, 0.1)]
cost = np.array([[math.dist(t, d) for d in detections] for t in tracks])
rows, cols = linear_sum_assignment(cost)
pairs = list(zip(rows.tolist(), cols.tolist()))
# Should match track0→det0 and track1→det1
print("PASS hungarian_retention" if cost[rows,cols].sum() < 0.5
      else f"FAIL hungarian_retention — total_cost={cost[rows,cols].sum():.3f}")
