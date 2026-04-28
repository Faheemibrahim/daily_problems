# Warmup Day 26 — RANSAC retention
# Topics: fit plane to 3 points, count points within 0.1, recursion retention
# Fill in each block so all PASS lines print.

import math
import random

# ── 1. Fit a plane to exactly 3 points ───────────────────────────────────────
def fit_plane(p1, p2, p3):
    v1 = (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])
    v2 = (p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2])
    a = v1[1]*v2[2] - v1[2]*v2[1]
    b = v1[2]*v2[0] - v1[0]*v2[2]
    c = v1[0]*v2[1] - v1[1]*v2[0]
    d = -(a*p1[0] + b*p1[1] + c*p1[2])
    return (a, b, c, d)

p1, p2, p3 = (0.0,0.0,0.0), (1.0,0.0,0.0), (0.0,1.0,0.0)
plane = fit_plane(p1, p2, p3)
# z=0 plane → normal should be (0,0,±1,0)
a,b,c,d = plane
norm = math.sqrt(a**2+b**2+c**2)
print("PASS fit_plane" if norm > 1e-9 and abs(d/norm) < 1e-9
      else f"FAIL fit_plane — {plane}")

# ── 2. Count points within distance 0.1 of the z=0 plane ─────────────────────
random.seed(7)
ground = [(random.uniform(-5,5), random.uniform(-5,5), random.gauss(0, 0.03)) for _ in range(50)]
above  = [(random.uniform(-5,5), random.uniform(-5,5), random.uniform(0.5, 1.5)) for _ in range(20)]
all_pts = ground + above

a, b, c, d = 0.0, 0.0, 1.0, 0.0  # z=0 plane
norm = math.sqrt(a**2+b**2+c**2)
inliers = [p for p in all_pts if abs(a*p[0]+b*p[1]+c*p[2]+d)/norm <= 0.1]
# Most ground points (±3σ with σ=0.03) should be inliers; none of the above
print("PASS count_inliers" if len(inliers) >= 40 and len(inliers) <= 50
      else f"FAIL count_inliers — {len(inliers)}")

# ── 3. Recursion retention — power function ───────────────────────────────────
def power(base, exp):
    if exp == 0: return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)

print("PASS recursion" if power(2, 10) == 1024 and power(3, 4) == 81
      else f"FAIL recursion")
