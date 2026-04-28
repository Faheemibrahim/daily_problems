# Problem: Given a list of clusters, return a list of dicts each containing
#          id, centroid, size, bounding_box — sorted by distance of centroid from origin.
# Concept: Converting raw clusters into structured dicts is the final step before
#          publishing to the rest of the autonomy stack. Downstream nodes read dicts,
#          not raw point lists.
# You are done when:
#   [ ] Each dict has keys: id, centroid, size, bounding_box
#   [ ] bounding_box is (x_min, x_max, y_min, y_max, z_min, z_max)
#   [ ] The list is sorted by centroid distance from origin ascending
#   [ ] All test cases print PASS
# Hint: centroid = (mean_x, mean_y, mean_z); sort with key=lambda d: dist(d['centroid'])

import math


def clusters_to_dicts(clusters):
    """
    Convert a list of point-lists into a sorted list of cluster dicts.
    Each dict: {'id': int, 'centroid': tuple, 'size': int,
                'bounding_box': (xmin, xmax, ymin, ymax, zmin, zmax)}
    Sorted by centroid distance from origin ascending.
    """
    pass


if __name__ == "__main__":
    c1 = [(5.0, 0.0, 0.0), (5.1, 0.0, 0.0), (4.9, 0.0, 0.0)]  # far
    c2 = [(1.0, 0.0, 0.0), (1.1, 0.0, 0.0)]                     # close

    result = clusters_to_dicts([c1, c2])
    print("PASS len" if len(result) == 2 else f"FAIL len — {len(result)}")
    print("PASS keys" if all("centroid" in d and "bounding_box" in d and "size" in d for d in result)
          else "FAIL keys")
    # closer cluster should be first
    d0 = math.sqrt(sum(v**2 for v in result[0]["centroid"]))
    d1 = math.sqrt(sum(v**2 for v in result[1]["centroid"]))
    print("PASS sorted" if d0 <= d1 else f"FAIL sorted — d0={d0:.2f} d1={d1:.2f}")
    print("PASS size c2 first" if result[0]["size"] == 2 else f"FAIL first size — {result[0]['size']}")
