# Warmup Day 10 — Functions + Classes (PointCloud & Cluster) + Dicts + Sets
# 5 problems. Target: 5-10 minutes total.

import math


# ── Shared helpers ────────────────────────────────────────────────────────────
class BoundingBox:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.z_min, self.z_max = z_min, z_max
    def contains(self, p):
        return (self.x_min <= p[0] <= self.x_max and
                self.y_min <= p[1] <= self.y_max and
                self.z_min <= p[2] <= self.z_max)

# ── Problem 1 (Functions) ────────────────────────────────────────────────────
# Concept: calling filter_points with default args
# Write filter_points and call it — keep points where |x| <= 5 and z in [-0.5, 0.3].

def filter_points(pts, z_min=-0.5, z_max=0.3, x_range=5.0, y_range=5.0):
    pass

r1 = filter_points([(0.0, 0.0, 0.0), (6.0, 0.0, 0.0), (0.0, 0.0, 1.0)])
print("W10-P1 PASS" if r1 == [(0.0, 0.0, 0.0)] else f"W10-P1 FAIL — got {r1}")

# ── Problem 2 (Classes) ──────────────────────────────────────────────────────
# Concept: PointCloud add and size
class PointCloud:
    def __init__(self): self.points = []
    def add(self, p): pass
    def size(self): pass
    def centroid(self):
        n = len(self.points)
        return (sum(p[0] for p in self.points)/n, sum(p[1] for p in self.points)/n,
                sum(p[2] for p in self.points)/n)

pc = PointCloud()
for p in [(1.0, 0.0, 0.0), (3.0, 0.0, 0.0)]:
    pc.add(p)
print("W10-P2 PASS size" if pc.size() == 2 else f"W10-P2 FAIL size — {pc.size()}")
print("W10-P2 PASS centroid" if pc.centroid() == (2.0, 0.0, 0.0) else f"W10-P2 FAIL centroid — {pc.centroid()}")

# ── Problem 3 (Classes) ──────────────────────────────────────────────────────
# Concept: Cluster centroid
class Cluster:
    def __init__(self, points): self.points = points
    def size(self): return len(self.points)
    def centroid(self): pass

cl = Cluster([(0.0, 0.0, 0.0), (2.0, 0.0, 0.0), (1.0, 3.0, 0.0)])
c3 = cl.centroid()
print("W10-P3 PASS" if c3 == (1.0, 1.0, 0.0) else f"W10-P3 FAIL — got {c3}")

# ── Problem 4 (Dicts) ────────────────────────────────────────────────────────
# Concept: build dict keyed by index from a list of Cluster objects
def clusters_by_index(clusters):
    pass

clusters4 = [Cluster([(0.0, 0.0, 0.0)]), Cluster([(1.0, 0.0, 0.0)])]
r4 = clusters_by_index(clusters4)
print("W10-P4 PASS" if r4[0] is clusters4[0] and r4[1] is clusters4[1] else f"W10-P4 FAIL — {r4}")

# ── Problem 5 (Sets) ─────────────────────────────────────────────────────────
# Concept: track unique points in a PointCloud using a set
def unique_points(pc):
    pass

pc5 = PointCloud()
for p in [(1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (1.0, 0.0, 0.0)]:
    pc5.add(p)
r5 = unique_points(pc5)
print("W10-P5 PASS" if r5 == {(1.0, 0.0, 0.0), (2.0, 0.0, 0.0)} else f"W10-P5 FAIL — got {r5}")
