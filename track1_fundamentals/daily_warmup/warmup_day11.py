# Warmup Day 11 — Dicts+Functions + Classes+Lists + Sets+Loops + Numpy
# 5 problems. Target: 5-10 minutes total.

import numpy as np


# ── Problem 1 (Dicts + Functions) ────────────────────────────────────────────
# Concept: voxel count per cell
# Given a list of points, return a dict of voxel_key -> count using voxel_size=1.0.

def voxel_counts(pts, voxel_size=1.0):
    pass

r1 = voxel_counts([(0.1, 0.1, 0.0), (0.9, 0.1, 0.0), (1.5, 0.0, 0.0)])
print("W11-P1 PASS" if r1.get((0, 0, 0), 0) == 2 and r1.get((1, 0, 0), 0) == 1
      else f"W11-P1 FAIL — {r1}")

# ── Problem 2 (Classes + Lists) ──────────────────────────────────────────────
# Concept: filter Cluster list by size
# Return only clusters with size >= min_size.

class Cluster:
    def __init__(self, pts): self.points = pts
    def size(self): return len(self.points)
    def centroid(self):
        n = len(self.points)
        return (sum(p[0] for p in self.points)/n, sum(p[1] for p in self.points)/n,
                sum(p[2] for p in self.points)/n)

def large_clusters(clusters, min_size=3):
    pass

clusters2 = [Cluster([(0.0, 0.0, 0.0)] * 5), Cluster([(1.0, 0.0, 0.0)] * 2)]
r2 = large_clusters(clusters2)
print("W11-P2 PASS" if len(r2) == 1 and r2[0] is clusters2[0] else f"W11-P2 FAIL — {r2}")

# ── Problem 3 (Sets + Loops) ─────────────────────────────────────────────────
# Concept: visited set to skip duplicates in a loop
# Loop through a list; if the element was seen before skip it, else add to seen and result.

def deduplicate_ordered(lst):
    pass

r3 = deduplicate_ordered([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print("W11-P3 PASS" if r3 == [3, 1, 4, 5, 9, 2, 6] else f"W11-P3 FAIL — got {r3}")

# ── Problem 4 (Numpy) ────────────────────────────────────────────────────────
# Concept: convert list to numpy array, check shape
pts4 = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]
arr4 = np.array(pts4)
print("W11-P4 PASS" if arr4.shape == (2, 3) else f"W11-P4 FAIL — shape {arr4.shape}")

# ── Problem 5 (Numpy) ────────────────────────────────────────────────────────
# Concept: column slicing
arr5 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
x_col = arr5[:, 0]
print("W11-P5 PASS" if list(x_col) == [1.0, 4.0, 7.0] else f"W11-P5 FAIL — {x_col}")
