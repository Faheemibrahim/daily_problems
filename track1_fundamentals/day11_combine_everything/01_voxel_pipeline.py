# Problem: Write a function that takes raw points, runs them through filter_points,
#          groups them into a voxel dict, then returns the centroid of each voxel cell.
# Concept: Composing day06 and day08 work into a mini pipeline — filter then discretise
#          then aggregate. This is the structure of a real LiDAR downsampling step.
# You are done when:
#   [ ] You call filter_points to remove out-of-bounds points first
#   [ ] You build a voxel dict from the filtered points
#   [ ] You compute and return the centroid per voxel cell
#   [ ] All test cases print PASS
# Hint: Chain the functions: filtered = filter_points(raw), voxels = build_voxel_dict(filtered),
#       then compute centroids with the same logic from day06 problem 04.

import math


def filter_points(points, z_min=-0.5, z_max=0.3, x_range=5.0, y_range=5.0):
    return [p for p in points
            if z_min <= p[2] <= z_max and abs(p[0]) <= x_range and abs(p[1]) <= y_range]


def build_voxel_dict(points, voxel_size=0.5):
    vd = {}
    for p in points:
        key = (int(p[0] // voxel_size), int(p[1] // voxel_size), int(p[2] // voxel_size))
        vd.setdefault(key, []).append(p)
    return vd


def voxel_pipeline(raw_points, voxel_size=0.5):
    """
    Filter raw_points, group into voxels, and return a dict of
    voxel_key -> centroid (mean_x, mean_y, mean_z).
    """
    pass


if __name__ == "__main__":
    raw = [
        (0.1, 0.1, 0.0),
        (0.2, 0.1, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 0.0, 5.0),  # filtered out (z too high)
        (10.0, 0.0, 0.0), # filtered out (x out of range)
    ]
    result = voxel_pipeline(raw)

    print("PASS num cells" if len(result) == 2 else f"FAIL num cells — {len(result)}: {result}")
    key = (0, 0, 0)
    if key in result:
        c = result[key]
        expected = (0.15, 0.1, 0.0)
        ok = all(abs(c[i] - expected[i]) < 1e-9 for i in range(3))
        print("PASS centroid (0,0,0)" if ok else f"FAIL centroid (0,0,0) — {c}")
    else:
        print(f"FAIL missing key (0,0,0) — keys: {list(result.keys())}")
