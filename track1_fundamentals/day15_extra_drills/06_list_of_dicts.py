# Problem: Four list-of-dicts sub-problems:
#   1. Convert raw clusters (list of lists of points) into dicts with id/centroid/size/bounding_box.
#   2. Find the cluster dict with the largest size.
#   3. Filter keeping only dicts where size > 5.
#   4. Sort by distance of centroid from origin.
# Concept: List of dicts is the standard way to represent detected objects in robotics.
#          Query, sort, and filter operations are all one-liners once data is in this form.
# You are done when:
#   [ ] Each cluster dict has exactly the keys: id, centroid, size, bounding_box
#   [ ] Largest, filter, and sort all work correctly
#   [ ] All test cases print PASS
# Hint: centroid is (mean_x, mean_y, mean_z); bounding_box is (x_min, x_max, y_min, y_max, z_min, z_max).

import math


def clusters_to_dicts(raw_clusters):
    """
    Convert a list of point lists into a list of cluster dicts.
    Each dict: {'id': i, 'size': n, 'centroid': (mx, my, mz),
                'bounding_box': (xmin, xmax, ymin, ymax, zmin, zmax)}
    """
    pass


def largest_cluster(cluster_dicts):
    """Return the cluster dict with the maximum size."""
    pass


def filter_large(cluster_dicts, min_size=5):
    """Return only cluster dicts where size > min_size."""
    pass


def sort_by_centroid_distance(cluster_dicts):
    """Return cluster dicts sorted by centroid distance from origin ascending."""
    pass


if __name__ == "__main__":
    raw = [
        [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (2.0, 0.0, 0.0)],      # size 3
        [(5.0, 5.0, 0.0)] * 8,                                        # size 8
        [(1.0, 0.0, 0.0), (1.1, 0.0, 0.0), (0.9, 0.0, 0.0)] * 2,   # size 6
    ]
    dicts = clusters_to_dicts(raw)

    print("PASS num dicts" if len(dicts) == 3 else f"FAIL num dicts — {len(dicts)}")
    print("PASS keys" if all("centroid" in d and "bounding_box" in d for d in dicts)
          else "FAIL keys")

    largest = largest_cluster(dicts)
    print("PASS largest" if largest["size"] == 8 else f"FAIL largest — {largest['size']}")

    filtered = filter_large(dicts, min_size=5)
    print("PASS filter" if len(filtered) == 2 else f"FAIL filter — {len(filtered)}")

    sorted_d = sort_by_centroid_distance(filtered)
    d0 = math.sqrt(sum(v**2 for v in sorted_d[0]["centroid"]))
    d1 = math.sqrt(sum(v**2 for v in sorted_d[1]["centroid"]))
    print("PASS sort" if d0 <= d1 else f"FAIL sort — d0={d0:.2f} d1={d1:.2f}")
