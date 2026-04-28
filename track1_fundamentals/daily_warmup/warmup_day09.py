# Warmup Day 09 — Sets + Functions + Classes (Point3D) + Dicts
# 5 problems. Target: 5-10 minutes total.

import math


# ── Problem 1 (Sets) ─────────────────────────────────────────────────────────
# Concept: set difference chain
# Return elements in A that are in neither B nor C.

def only_in_a(a, b, c):
    pass

r1 = only_in_a([1, 2, 3, 4], [2, 3], [3, 4])
print("W09-P1 PASS" if r1 == {1} else f"W09-P1 FAIL — got {r1}")

# ── Problem 2 (Functions) ────────────────────────────────────────────────────
# Concept: calling centroid
# Given a list of (x, y, z) points, return their centroid using a function you write.

def centroid(pts):
    pass

r2 = centroid([(0.0, 0.0, 0.0), (4.0, 0.0, 0.0)])
print("W09-P2 PASS" if r2 == (2.0, 0.0, 0.0) else f"W09-P2 FAIL — got {r2}")

# ── Problem 3 (Classes) ──────────────────────────────────────────────────────
# Concept: Point3D instantiation and distance_to
# Create two Point3D objects and compute distance between them.

class Point3D:
    def __init__(self, x, y, z):
        pass
    def distance_to(self, other):
        pass
    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

p1 = Point3D(0.0, 0.0, 0.0)
p2 = Point3D(3.0, 4.0, 0.0)
print("W09-P3 PASS" if p1.distance_to(p2) == 5.0 else f"W09-P3 FAIL dist — {p1.distance_to(p2)}")
print("W09-P3 PASS repr" if repr(p2) == "Point3D(x=3.0, y=4.0, z=0.0)" else f"W09-P3 FAIL repr — {repr(p2)}")

# ── Problem 4 (Classes) ──────────────────────────────────────────────────────
# Concept: comparing two Point3D distances to origin
# Create two points and return the one closer to the origin.

def closer_to_origin(p1, p2):
    pass

origin = Point3D(0.0, 0.0, 0.0)
pa = Point3D(1.0, 0.0, 0.0)
pb = Point3D(3.0, 0.0, 0.0)
r4 = closer_to_origin(pa, pb)
print("W09-P4 PASS" if r4 is pa else f"W09-P4 FAIL — got {r4}")

# ── Problem 5 (Dicts) ────────────────────────────────────────────────────────
# Concept: build dict from objects
# Given a list of Point3D objects, return a dict mapping index -> Point3D.

def index_dict(points):
    pass

pts5 = [Point3D(1.0, 0.0, 0.0), Point3D(2.0, 0.0, 0.0)]
r5 = index_dict(pts5)
print("W09-P5 PASS" if r5[0] is pts5[0] and r5[1] is pts5[1] else f"W09-P5 FAIL — {r5}")
