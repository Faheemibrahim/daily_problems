# Warmup Day 27 — Euclidean Clustering retention
# Topics: euclidean clustering 20 points, filter ≥3, RANSAC retention
# Fill in each block so all PASS lines print.

import math
import random
from collections import deque
from scipy.spatial import KDTree
import numpy as np

random.seed(0)

# ── 1. Euclidean clustering on 20 points (2 groups of 10) ────────────────────
group_a = [(random.gauss(0.0, 0.05), random.gauss(0.0, 0.05), 0.0) for _ in range(10)]
group_b = [(random.gauss(5.0, 0.05), random.gauss(0.0, 0.05), 0.0) for _ in range(10)]
pts = group_a + group_b

arr = np.array(pts)
tree = KDTree(arr)
visited = set()
clusters = []
for i in range(len(pts)):
    if i in visited: continue
    comp = []; q = deque([i]); visited.add(i)
    while q:
        cur = q.popleft(); comp.append(pts[cur])
        for nb in tree.query_ball_point(pts[cur], r=0.5):
            if nb not in visited: visited.add(nb); q.append(nb)
    clusters.append(comp)

print("PASS clustering" if len(clusters) == 2 else f"FAIL clustering — {len(clusters)} clusters")

# ── 2. Filter clusters with fewer than 3 points ───────────────────────────────
mixed = [list(range(10)), list(range(2)), list(range(5)), list(range(1)), list(range(8))]
large = [c for c in mixed if len(c) >= 3]
print("PASS filter_clusters" if len(large) == 3 else f"FAIL filter_clusters — {len(large)}")

# ── 3. RANSAC retention — ground removal leaves cone points ───────────────────
def ransac_plane(points, iterations=30, threshold=0.08, seed=0):
    random.seed(seed)
    pts = list(points)
    best_plane, best_count = None, 0
    for _ in range(iterations):
        if len(pts) < 3: break
        p1,p2,p3 = random.sample(pts, 3)
        v1 = tuple(p2[i]-p1[i] for i in range(3))
        v2 = tuple(p3[i]-p1[i] for i in range(3))
        a = v1[1]*v2[2]-v1[2]*v2[1]; b = v1[2]*v2[0]-v1[0]*v2[2]; c = v1[0]*v2[1]-v1[1]*v2[0]
        d = -(a*p1[0]+b*p1[1]+c*p1[2])
        norm = math.sqrt(a**2+b**2+c**2)
        if norm < 1e-9: continue
        count = sum(1 for p in pts if abs(a*p[0]+b*p[1]+c*p[2]+d)/norm <= threshold)
        if count > best_count: best_count = count; best_plane = (a,b,c,d)
    return best_plane

ground = [(random.uniform(-5,5), random.uniform(-5,5), random.gauss(0,0.02)) for _ in range(80)]
cone   = [(random.gauss(2.0,0.05), random.gauss(0.0,0.05), random.uniform(0.05,0.3)) for _ in range(20)]
all_pts = ground + cone

plane = ransac_plane(all_pts)
a,b,c,d = plane
norm = math.sqrt(a**2+b**2+c**2)
non_ground = [p for p in all_pts if abs(a*p[0]+b*p[1]+c*p[2]+d)/norm > 0.08]
# most of the 20 cone points should survive; most ground removed
print("PASS ransac_retention" if len(non_ground) >= 15
      else f"FAIL ransac_retention — {len(non_ground)} non-ground points")
