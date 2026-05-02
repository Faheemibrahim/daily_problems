# =============================================================================
# PROBLEM 04 — Dict as O(1) Lookup Table
# =============================================================================
# What: store 1000 points in a dict by grid key, then query it fast
# Concept: dict enables O(1) lookup vs O(n) brute force
# Done when:
#   [ ] dict stores points by rounded (x,y) key
#   [ ] query retrieves points from same cell instantly
#   [ ] timing shows dict faster than brute force
# Hint: key = (round(x, 1), round(y, 1))
# =============================================================================

import math
import time
import random


def build_lookup(points, grid_size=0.5):
    """
    Store points in a dict for fast spatial lookup.
    key   = (vx, vy) where vx = floor(x / grid_size)
    value = list of points in that cell
    Return the lookup dict.
    """
    # key   =
    # value =
    pass


def lookup_query(lookup_dict, query_point, grid_size=0.5):
    """
    Return all points in the same grid cell as query_point.
    This should be O(1) — one dict lookup.
    """
    pass


def brute_force_query(points, query_point, grid_size=0.5):
    """
    Return all points in same grid cell as query_point.
    This is O(n) — checks every point.
    """
    pass


def compare_timing(points, query_point, grid_size=0.5):
    """
    Time both approaches for 1000 queries.
    Return dict with keys 'brute_force_seconds' and 'lookup_seconds'.
    """
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    random.seed(42)
    pts = [(random.uniform(-10,10), random.uniform(-10,10), random.uniform(-5,5))
           for _ in range(1000)]

    lookup = build_lookup(pts)
    print("PASS — builds dict"     if isinstance(lookup, dict)    else "FAIL — not dict")
    print("PASS — has cells"       if len(lookup) > 0             else "FAIL — empty dict")
    print("PASS — values are lists" if all(isinstance(v,list) for v in lookup.values())
          else "FAIL — values should be lists")

    query = pts[0]
    lq = lookup_query(lookup, query)
    bf = brute_force_query(pts, query)

    print("PASS — same results" if sorted(lq) == sorted(bf)
          else f"FAIL — lookup {len(lq)} vs brute {len(bf)}")

    timing = compare_timing(pts, query)
    print("PASS — lookup faster" if timing["lookup_seconds"] < timing["brute_force_seconds"]
          else f"FAIL — lookup {timing['lookup_seconds']:.4f}s brute {timing['brute_force_seconds']:.4f}s")
    print(f"INFO — brute: {timing['brute_force_seconds']:.4f}s  lookup: {timing['lookup_seconds']:.6f}s")
