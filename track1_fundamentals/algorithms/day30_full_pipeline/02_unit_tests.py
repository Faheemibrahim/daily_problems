# Problem: Write unit tests for each step of the pipeline using automatic PASS/FAIL checks.
# Concept: Each step should be testable in isolation. Testing step-by-step lets you pinpoint
#          exactly which step broke when the full pipeline fails.
# You are done when:
#   [ ] Each step (filter, voxel, cluster, size_filter, dim_filter, to_dicts) has its own test
#   [ ] Tests use small, hand-crafted inputs with known expected outputs
#   [ ] All 6 step tests print PASS
# Hint: Import the helpers from 01_full_pipeline or copy-paste each step function here.

import math
import numpy as np
from scipy.spatial import KDTree
from collections import deque


# ── Step 1: bounding box filter ───────────────────────────────────────────────
def test_bbox_filter():
    """Filter should remove points outside z∈[-0.5,0.3] and |x|,|y| > xy_range."""
    arr = np.array([
        [0.0, 0.0, 0.0],    # inside
        [6.0, 0.0, 0.0],    # x too far
        [0.0, 0.0, 0.5],    # z too high
        [0.0, 0.0, -0.6],   # z too low
        [4.9, 4.9, 0.1],    # inside
    ])
    # Your filter implementation:
    mask = (
        (arr[:, 2] >= -0.5) & (arr[:, 2] <= 0.3) &
        (np.abs(arr[:, 0]) <= 5.0) & (np.abs(arr[:, 1]) <= 5.0)
    )
    result = arr[mask]
    print("PASS step1 filter" if result.shape[0] == 2 else f"FAIL step1 — {result.shape[0]} rows")


# ── Step 2: voxel downsampling ────────────────────────────────────────────────
def test_voxel_downsample():
    """Two close points should merge into one centroid."""
    pts = [(0.05, 0.0, 0.0), (0.08, 0.0, 0.0), (1.0, 0.0, 0.0)]
    voxel_size = 0.1
    vd = {}
    for p in pts:
        key = (int(p[0]//voxel_size), int(p[1]//voxel_size), int(p[2]//voxel_size))
        vd.setdefault(key, []).append(p)
    centroids = [(sum(p[i] for p in v)/len(v) for i in range(3)) for v in vd.values()]
    print("PASS step2 voxel" if len(vd) == 2 else f"FAIL step2 — {len(vd)} cells")


# ── Step 3: clustering ────────────────────────────────────────────────────────
def test_clustering():
    """Three separate groups should produce 3 clusters."""
    groups = [[(i*0.05, 0.0, 0.0) for i in range(10)],
              [(5.0 + i*0.05, 0.0, 0.0) for i in range(8)],
              [(10.0 + i*0.05, 0.0, 0.0) for i in range(6)]]
    pts = [p for g in groups for p in g]
    arr = np.array(pts)
    tree = KDTree(arr)
    visited = set(); clusters = []
    for i in range(len(pts)):
        if i in visited: continue
        comp = []; q = deque([i]); visited.add(i)
        while q:
            cur = q.popleft(); comp.append(pts[cur])
            for nb in tree.query_ball_point(pts[cur], r=0.2):
                if nb not in visited: visited.add(nb); q.append(nb)
        clusters.append(comp)
    print("PASS step3 cluster" if len(clusters) == 3 else f"FAIL step3 — {len(clusters)}")


# ── Step 4: size filter ───────────────────────────────────────────────────────
def test_size_filter():
    clusters = [list(range(3)), list(range(10)), list(range(50)), list(range(300))]
    filtered = [c for c in clusters if 5 <= len(c) <= 200]
    print("PASS step4 size" if len(filtered) == 2 else f"FAIL step4 — {len(filtered)}")


# ── Step 5: dimension filter ──────────────────────────────────────────────────
def test_dim_filter():
    clusters = [
        [(0.0,0.0,0.0),(0.3,0.3,0.4)],   # fits
        [(0.0,0.0,0.0),(1.5,0.0,0.0)],   # too wide x
    ]
    filtered = [c for c in clusters
                if (max(p[0] for p in c)-min(p[0] for p in c) < 1.0 and
                    max(p[1] for p in c)-min(p[1] for p in c) < 1.0 and
                    max(p[2] for p in c)-min(p[2] for p in c) < 0.8)]
    print("PASS step5 dims" if len(filtered) == 1 else f"FAIL step5 — {len(filtered)}")


# ── Step 6: to dicts ──────────────────────────────────────────────────────────
def test_to_dicts():
    clusters = [[(1.0,0.0,0.0),(1.2,0.0,0.0)], [(5.0,0.0,0.0)]]
    dicts = []
    for i, cl in enumerate(clusters):
        n = len(cl)
        cx = sum(p[0] for p in cl)/n; cy = sum(p[1] for p in cl)/n; cz = sum(p[2] for p in cl)/n
        dicts.append({"id": i, "size": n, "centroid": (cx,cy,cz),
                      "bounding_box": (min(p[0] for p in cl), max(p[0] for p in cl),
                                       min(p[1] for p in cl), max(p[1] for p in cl),
                                       min(p[2] for p in cl), max(p[2] for p in cl))})
    print("PASS step6 dicts" if len(dicts) == 2 and "centroid" in dicts[0] else f"FAIL step6")


if __name__ == "__main__":
    test_bbox_filter()
    test_voxel_downsample()
    test_clustering()
    test_size_filter()
    test_dim_filter()
    test_to_dicts()
