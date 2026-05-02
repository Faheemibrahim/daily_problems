# =============================================================================
# PROBLEM 06 — Combine All Dict Patterns
# =============================================================================
# What: full mini pipeline combining filter group compute return
# Concept: every dict pattern used together in one pipeline
# Done when:
#   [ ] define every data structure in comments first
#   [ ] no print inside any function
#   [ ] filter works correctly
#   [ ] per-quadrant stats correct
#   [ ] biggest quadrant identified correctly
#   [ ] all test cases pass cold
# Hint: write the full structure in comments before any code
#       # key   = quadrant name
#       # value = { 'count': int, 'centroid': tuple, 'closest': tuple }
# =============================================================================

import math


def filter_points(points, x_range=5.0, y_range=5.0):
    """Return only points where -x_range < x < x_range and same for y."""
    pass


def full_pipeline(raw_points):
    """
    Step 1: filter points to x and y within -5.0 to 5.0
    Step 2: group by quadrant Q1 Q2 Q3 Q4
    Step 3: for each quadrant compute count centroid closest_to_origin
    Step 4: return results dict and name of biggest quadrant as tuple

    Return: (results_dict, biggest_quadrant_name)

    results_dict structure:
    # key   = quadrant name string
    # value = {
    #   'count':    int,
    #   'centroid': (mean_x, mean_y, mean_z),
    #   'closest':  (x, y, z)  <- point in this quadrant closest to origin
    # }
    """
    # key   =
    # value = { 'count': , 'centroid': , 'closest': }
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import random
    random.seed(7)

    raw = [(random.uniform(-8,8), random.uniform(-8,8), random.uniform(-2,2))
           for _ in range(30)]

    results, biggest = full_pipeline(raw)

    print("PASS — returns tuple"  if isinstance((results, biggest), tuple) else "FAIL")
    print("PASS — results is dict" if isinstance(results, dict)   else "FAIL — not dict")
    print("PASS — biggest is str"  if isinstance(biggest, str)    else "FAIL — biggest not str")
    print("PASS — biggest valid"   if biggest in ("Q1","Q2","Q3","Q4")
          else f"FAIL — biggest={biggest}")

    total = sum(v["count"] for v in results.values())
    filtered = [p for p in raw if -5.0 < p[0] < 5.0 and -5.0 < p[1] < 5.0]
    print("PASS — counts sum to filtered" if total == len(filtered)
          else f"FAIL — total={total} filtered={len(filtered)}")

    for q, data in results.items():
        if data["count"] > 0:
            print(f"PASS — {q} has centroid" if isinstance(data["centroid"], tuple)
                  else f"FAIL — {q} centroid wrong type")
            print(f"PASS — {q} has closest"  if isinstance(data["closest"], tuple)
                  else f"FAIL — {q} closest wrong type")
