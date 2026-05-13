# Problem: Write a mini pipeline function that: filters by bounding box, removes duplicates
#          using a set, groups into voxel cells using a dict, and returns a downsampled
#          point list (one centroid per voxel cell).
# Concept: Composing all four data structures (list, set, dict, tuple) and the function
#          abstraction into a single coherent pipeline — the shape of real LiDAR processing.
# You are done when:
#   [ ] Step 1: bounding box filter removes out-of-bounds points
#   [ ] Step 2: set deduplication removes exact duplicates
#   [ ] Step 3: voxel dict groups remaining points
#   [ ] Step 4: one centroid per voxel is returned as the downsampled output
#   [ ] All test cases print PASS
# Hint: Each step's output becomes the next step's input — chain them in order.


def mini_pipeline(raw_points, z_min=-0.5, z_max=0.3, x_range=5.0, y_range=5.0, voxel_size=0.5):
    """
    Filter -> deduplicate -> voxelise -> downsample.
    Return a list of (x, y, z) centroids, one per voxel cell.
    """
    #filter 
    filtered = [p for p in raw_points if z_min <= p[2] <= z_max and abs(p[0]) <= x_range and abs(p[1]) <= y_range]

    #deduplicate
    visited = set(filtered)

    #voxelise
    vd = {}
    for p in visited:
        key = (int(p[0] // voxel_size), int(p[1] // voxel_size), int(p[2] // voxel_size))
        vd.setdefault(key, []).append(p)
    
    #downsample
    result = []
    for key, points in vd.items():
        n = len(points)
        mean_x = sum(p[0] for p in points) / n
        mean_y = sum(p[1] for p in points) / n
        mean_z = sum(p[2] for p in points) / n
        result.append((mean_x, mean_y, mean_z))
    
    return result


if __name__ == "__main__":
    raw = [
        (0.1, 0.1, 0.0),
        (0.2, 0.1, 0.0),
        (0.1, 0.1, 0.0),  # duplicate of first
        (1.0, 0.0, 0.0),
        (10.0, 0.0, 0.0), # outside x_range
        (0.0, 0.0, 5.0),  # outside z_range
    ]
    result = mini_pipeline(raw)

    # Expect 2 voxel centroids: one for cell (0,0,0) and one for (2,0,0)
    print("PASS num downsampled" if len(result) == 2 else f"FAIL num downsampled — {len(result)}: {result}")
    all_close = all(isinstance(p, tuple) and len(p) == 3 for p in result)
    print("PASS output type" if all_close else f"FAIL output type — {result}")
