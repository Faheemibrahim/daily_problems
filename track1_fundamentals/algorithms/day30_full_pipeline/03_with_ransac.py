# Problem: Add RANSAC ground removal as step 1.5 (between bbox filter and voxel downsample).
# Concept: RANSAC plane fitting removes the ground more robustly than a fixed z threshold.
#          It handles sloped ground, speed bumps, and ramps that a z-cutoff would misclassify.
# You are done when:
#   [ ] Step 1.5 runs ransac_plane on the filtered points
#   [ ] Ground points (within threshold of best plane) are removed
#   [ ] Non-ground points proceed to voxel + clustering
#   [ ] Detection accuracy is maintained with RANSAC enabled
#   [ ] All test cases print PASS
# Hint: Run ransac_plane, then keep only points with distance > ransac_threshold from the plane.

import math
import random
import numpy as np
from collections import deque
from scipy.spatial import KDTree


def ransac_plane(points, iterations=50, threshold=0.08, seed=None):
    """Find the dominant plane in a set of 3D points."""
    if seed is not None: random.seed(seed)
    best_plane, best_count = None, 0
    pts = list(points)
    for _ in range(iterations):
        if len(pts) < 3: break
        sample = random.sample(pts, 3)
        p1, p2, p3 = sample
        v1 = tuple(p2[i]-p1[i] for i in range(3))
        v2 = tuple(p3[i]-p1[i] for i in range(3))
        a = v1[1]*v2[2]-v1[2]*v2[1]; b = v1[2]*v2[0]-v1[0]*v2[2]; c = v1[0]*v2[1]-v1[1]*v2[0]
        d = -(a*p1[0]+b*p1[1]+c*p1[2])
        norm = math.sqrt(a**2+b**2+c**2)
        if norm < 1e-9: continue
        count = sum(1 for p in pts if abs(a*p[0]+b*p[1]+c*p[2]+d)/norm <= threshold)
        if count > best_count: best_count = count; best_plane = (a,b,c,d)
    return best_plane


def detect_cones_with_ransac(raw_points,
                              z_min=-0.5, z_max=0.3, xy_range=5.0,
                              voxel_size=0.1,
                              epsilon=0.3, min_cluster_size=5, max_cluster_size=200,
                              max_x_span=1.0, max_y_span=1.0, max_z_span=0.8,
                              ransac_iterations=50, ransac_threshold=0.08):
    """
    Full pipeline with RANSAC ground removal as step 1.5.
    Copy your pipeline from problem 01 and insert the RANSAC step after bbox filter.
    """
    pass


if __name__ == "__main__":
    random.seed(0)

    def make_cone(cx, cy, n=25):
        return [(cx + random.gauss(0, 0.05), cy + random.gauss(0, 0.05),
                 random.uniform(0.0, 0.3)) for _ in range(n)]

    ground = [(random.uniform(-5,5), random.uniform(-5,5), random.gauss(0, 0.02)) for _ in range(200)]
    cones = make_cone(2.0, 0.5) + make_cone(-2.0, 0.5) + make_cone(0.0, 3.0)
    raw = ground + cones

    result = detect_cones_with_ransac(raw)
    print(f"Detected {len(result)} cone(s)")
    print("PASS 3 cones" if len(result) == 3 else f"FAIL — {len(result)}")
