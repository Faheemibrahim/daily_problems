# =============================================================================
# PROBLEM 07 — Defaultdict Upgrade
# =============================================================================
# What: rewrite grouping problems using defaultdict — no if key not in checks
# Concept: defaultdict(list) removes boilerplate, same result cleaner code
# Done when:
#   [ ] zero 'if key not in' checks anywhere
#   [ ] results identical to regular dict versions
#   [ ] understand WHY defaultdict removes the check
# Hint: from collections import defaultdict
#       groups = defaultdict(list)
#       groups[key].append(item)  <- no if check needed
# =============================================================================

from collections import defaultdict
import math


def group_quadrant_defaultdict(points):
    """
    Rewrite quadrant grouping using defaultdict(list).
    No if key not in check allowed.
    key   = quadrant name
    value = list of points
    """
    pass


def group_distance_defaultdict(points):
    """
    Rewrite distance grouping using defaultdict(list).
    close = dist < 2.0, medium = 2.0-5.0, far = >= 5.0
    No if key not in check allowed.
    """
    pass


def demonstrate_difference():
    """
    Return a dict showing the difference between dict and defaultdict
    when accessing a missing key.
    keys: 'regular_dict_error', 'defaultdict_result'
    """
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0,  2.0, 0.0), (-1.0, 2.0, 0.0),
        (1.0, -2.0, 0.0), (-1.0,-2.0, 0.0),
        (3.0,  4.0, 0.0), (-3.0,-4.0, 0.0),
        (2.0, -1.0, 0.0), (-2.0, 1.0, 0.0),
        (5.0,  1.0, 0.0),
    ]

    result = group_quadrant_defaultdict(pts)
    print("PASS — is dict-like"  if hasattr(result, '__getitem__') else "FAIL")
    print("PASS — Q1 has 3"      if len(result.get("Q1",[])) == 3
          else f"FAIL — Q1: {result.get('Q1')}")
    print("PASS — Q2 has 2"      if len(result.get("Q2",[])) == 2
          else f"FAIL — Q2: {result.get('Q2')}")

    dist_result = group_distance_defaultdict(pts)
    print("PASS — distance groups exist" if "close" in dist_result or "far" in dist_result
          else "FAIL — missing distance groups")

    diff = demonstrate_difference()
    print("PASS — demonstrates difference" if isinstance(diff, dict)
          else "FAIL — should return dict")

    import inspect
    src = inspect.getsource(group_quadrant_defaultdict)
    print("PASS — no if key not in" if "if" not in src or "not in" not in src
          else "FAIL — still using if key not in check")
