# =============================================================================
# REVISION DAY 01 — Lists and Indexing
# =============================================================================
# What: given a list of (x,y,z) points perform 4 operations from scratch
# Concept: list traversal, axis tracking, no built-in min/max
# Done when:
#   [ ] find largest x using a loop and tracking variable
#   [ ] find point closest to origin using a loop
#   [ ] collect points where x>0 and z>0 into a new list
#   [ ] find min and max for each axis
#   [ ] all results returned in a dict, nothing printed inside functions
# Hint: initialise tracking variables from points[0] not from 0
# =============================================================================

import math


def analyse_points(points):
    """
    Returns a dict with keys:
      largest_x_point  -> the point with the largest x value
      closest_to_origin -> the point closest to (0,0,0)
      positive_xz      -> list of points where x>0 and z>0
      axis_stats       -> dict with x_min x_max y_min y_max z_min z_max
    """
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0, -2.0, 3.0),
        (4.0,  5.0, -1.0),
        (-2.0, 0.0,  7.0),
        (3.0,  3.0,  2.0),
        (-1.0, 1.0,  1.0),
        (2.0, -1.0,  0.5),
    ]

    result = analyse_points(pts)

    checks = [
        (result["largest_x_point"] == (4.0, 5.0, -1.0),
         "largest_x_point"),
        (result["closest_to_origin"] == (1.0, -2.0, 3.0) or
         math.isclose(
             math.sqrt(sum(v**2 for v in result["closest_to_origin"])),
             min(math.sqrt(sum(v**2 for v in p)) for p in pts)
         ), "closest_to_origin"),
        (result["positive_xz"] == [(1.0,-2.0,3.0),(3.0,3.0,2.0),(2.0,-1.0,0.5)],
         "positive_xz"),
        (result["axis_stats"]["x_min"] == -2.0, "x_min"),
        (result["axis_stats"]["x_max"] ==  4.0, "x_max"),
        (result["axis_stats"]["z_min"] == -1.0, "z_min"),
        (result["axis_stats"]["z_max"] ==  7.0, "z_max"),
    ]

    for passed, name in checks:
        print(f"{'PASS' if passed else 'FAIL'} — {name}")
