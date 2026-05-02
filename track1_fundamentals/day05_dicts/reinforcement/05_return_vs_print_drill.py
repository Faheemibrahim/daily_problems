# =============================================================================
# PROBLEM 05 — Return vs Print Drill
# =============================================================================
# What: write 3 functions that RETURN only, then print in main block only
# Concept: functions return, main block prints — never mix them
# Done when:
#   [ ] zero print() statements inside any function
#   [ ] all results stored in variables in main block
#   [ ] all printing done only in main block
# Hint: if you see print() inside a function body — move it out
# =============================================================================

import math


def get_quadrant_counts(points):
    """
    Return dict of quadrant -> count.
    Do NOT print anything inside this function.
    """
    pass


def get_centroid(points):
    """
    Return (mean_x, mean_y, mean_z) as a tuple.
    Do NOT print anything inside this function.
    Raise ValueError if points is empty.
    """
    pass


def get_nearest(query, points):
    """
    Return the single nearest point to query.
    Do NOT print anything inside this function.
    """
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0,  2.0, 0.0),
        (-1.0, 2.0, 0.0),
        (1.0, -2.0, 0.0),
        (-1.0,-2.0, 0.0),
        (3.0,  0.0, 0.0),
    ]

    counts   = get_quadrant_counts(pts)
    centroid = get_centroid(pts)
    nearest  = get_nearest((0.0, 0.0, 0.0), pts)

    print("PASS — counts is dict"    if isinstance(counts, dict)    else "FAIL — counts not dict")
    print("PASS — centroid is tuple" if isinstance(centroid, tuple) else "FAIL — centroid not tuple")
    print("PASS — nearest is tuple"  if isinstance(nearest, tuple)  else "FAIL — nearest not tuple")
    print("PASS — nearest correct"   if nearest == (1.0, 2.0, 0.0) or
          math.sqrt(sum(v**2 for v in nearest)) ==
          min(math.sqrt(sum(v**2 for v in p)) for p in pts)
          else f"FAIL — nearest got {nearest}")

    try:
        get_centroid([])
        print("FAIL — should raise ValueError on empty list")
    except ValueError:
        print("PASS — raises ValueError on empty list")

    print()
    print("Results (printed only here in main):")
    print(f"  quadrant counts: {counts}")
    print(f"  centroid:        {centroid}")
    print(f"  nearest to origin: {nearest}")
