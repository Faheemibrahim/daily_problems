# Problem: Time the full pipeline on 50000 points. Profile which step takes the most time.
#          Then optimise that step and measure the improvement.
# Concept: Profiling before optimising is non-negotiable — you cannot know where the
#          bottleneck is without measuring it. This is the last lesson of the track.
# You are done when:
#   [ ] Each pipeline step is timed independently
#   [ ] You identify the slowest step from the timing output
#   [ ] You implement one optimisation to that step and show improvement
#   [ ] All test cases print PASS
# Hint: Use time.time() around each step; the clustering step is usually the bottleneck.
#       Common optimisation: increase voxel_size to reduce N before clustering.

import time
import math
import random
import numpy as np
from collections import deque
from scipy.spatial import KDTree


def profile_pipeline(raw_points, z_min=-0.5, z_max=0.3, xy_range=5.0,
                     voxel_size=0.1, epsilon=0.3, min_size=5, max_size=200):
    """
    Run the pipeline and return (result, timing_dict) where timing_dict maps
    step name to seconds taken.
    """
    timings = {}

    # Step 1: numpy bbox filter
    t = time.time()
    arr = np.array(raw_points) if not isinstance(raw_points, np.ndarray) else raw_points
    mask = ((arr[:,2] >= z_min) & (arr[:,2] <= z_max) &
            (np.abs(arr[:,0]) <= xy_range) & (np.abs(arr[:,1]) <= xy_range))
    filtered = arr[mask]
    timings["1_bbox_filter"] = time.time() - t

    # Step 2: voxel downsample
    t = time.time()
    vd = {}
    for p in filtered:
        key = (int(p[0]//voxel_size), int(p[1]//voxel_size), int(p[2]//voxel_size))
        vd.setdefault(key, []).append(tuple(p))
    downsampled = [(sum(q[i] for q in v)/len(v) for i in range(3)) for v in vd.values()]
    downsampled = [tuple(p) for p in downsampled]
    timings["2_voxel"] = time.time() - t

    # Step 3: clustering — your implementation goes here
    t = time.time()
    # TODO: implement clustering
    clusters = []
    timings["3_cluster"] = time.time() - t

    # Step 4 & 5: filter + to dicts
    t = time.time()
    result = []
    timings["4_postprocess"] = time.time() - t

    return result, timings


if __name__ == "__main__":
    random.seed(0)
    N = 50_000

    def make_cone(cx, cy, n):
        return [(cx+random.gauss(0,0.05), cy+random.gauss(0,0.05), random.uniform(0,0.3)) for _ in range(n)]

    raw = (
        [(random.uniform(-5,5), random.uniform(-5,5), random.uniform(-0.5,0.0)) for _ in range(N-300)] +
        make_cone(2.0, 0.5, 100) + make_cone(-2.0, 0.5, 100) + make_cone(0.0, 3.0, 100)
    )

    result, timings = profile_pipeline(raw, voxel_size=0.1)

    print("\n=== Pipeline timing (N=50000) ===")
    total = sum(timings.values())
    for step, t in sorted(timings.items()):
        pct = 100 * t / total if total > 0 else 0
        print(f"  {step}: {t:.4f}s  ({pct:.1f}%)")
    print(f"  TOTAL: {total:.4f}s")

    slowest = max(timings, key=timings.get)
    print(f"\nBottleneck: {slowest}")

    # Optimisation test: larger voxel reduces input to clustering
    _, timings_opt = profile_pipeline(raw, voxel_size=0.3)
    cluster_improvement = timings["3_cluster"] / timings_opt["3_cluster"] if timings_opt["3_cluster"] > 0 else 1.0
    print(f"\nClustering speedup with voxel_size=0.3: {cluster_improvement:.1f}x")
    print("PASS timing ran" if total > 0 else "FAIL timing")
