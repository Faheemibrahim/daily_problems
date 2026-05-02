# =============================================================================
# REVISION DAY 04 — Slicing, Nesting, Sorting
# =============================================================================
# What: 6 slicing and sorting tasks on a list of 12 points
# Concept: slice syntax, reverse, step, restructuring, sorted with key/lambda
# Done when:
#   [ ] first/last/middle slices correct
#   [ ] reverse uses slicing not .reverse()
#   [ ] flat list converted to tuples correctly
#   [ ] both sorts use key argument not manual loops
# Hint: sorted(points, key=lambda p: p[2]) sorts by z value
# =============================================================================

import math


def slice_sections(points):
    """Return dict with keys first4, last4, middle4."""
    pass


def reverse_list(points):
    """Return reversed list using slicing only."""
    pass


def flat_to_tuples(flat):
    """Convert [x1,y1,z1,x2,y2,z2,...] to [(x1,y1,z1),(x2,y2,z2),...]."""
    pass


def sort_by_z(points):
    """Return points sorted by z ascending using sorted() with key."""
    pass


def sort_by_distance(points):
    """Return points sorted by distance from origin using sorted() with lambda."""
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0,2.0,3.0),(4.0,5.0,6.0),(7.0,8.0,9.0),(10.0,11.0,12.0),
        (2.0,3.0,1.0),(5.0,6.0,4.0),(8.0,9.0,7.0),(11.0,12.0,10.0),
        (3.0,1.0,2.0),(6.0,4.0,5.0),(9.0,7.0,8.0),(12.0,10.0,11.0),
    ]

    s = slice_sections(pts)
    print("PASS — first4"  if s["first4"]  == pts[:4]  else f"FAIL — first4")
    print("PASS — last4"   if s["last4"]   == pts[-4:] else f"FAIL — last4")
    print("PASS — middle4" if s["middle4"] == pts[4:8] else f"FAIL — middle4")

    rev = reverse_list(pts)
    print("PASS — reverse" if rev == pts[::-1] else f"FAIL — reverse got {rev[:2]}")

    flat = [1.0,2.0,3.0, 4.0,5.0,6.0, 7.0,8.0,9.0]
    tuples = flat_to_tuples(flat)
    print("PASS — flat_to_tuples" if tuples == [(1.0,2.0,3.0),(4.0,5.0,6.0),(7.0,8.0,9.0)]
          else f"FAIL — flat_to_tuples got {tuples}")

    small = [(3.0,0.0,5.0),(1.0,0.0,1.0),(2.0,0.0,3.0)]
    sz = sort_by_z(small)
    print("PASS — sort_by_z" if sz[0][2] <= sz[1][2] <= sz[2][2]
          else f"FAIL — sort_by_z got {sz}")

    sd = sort_by_distance(small)
    dists = [math.sqrt(sum(v**2 for v in p)) for p in sd]
    print("PASS — sort_by_distance" if dists == sorted(dists)
          else f"FAIL — sort_by_distance")
