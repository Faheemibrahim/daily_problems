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
import inspect


def group_quadrant_defaultdict(points):
    """
    Rewrite quadrant grouping using defaultdict(list).
    Use defaultdict only.
    key   = quadrant name
    value = list of points
    """

    d = defaultdict(list)

    for point in points:

        x, y, z = point

        if x > 0 and y > 0:
            d["Q1"].append(point)

        elif x < 0 and y > 0:
            d["Q2"].append(point)

        elif x < 0 and y < 0:
            d["Q3"].append(point)

        elif x > 0 and y < 0:
            d["Q4"].append(point)

    return d


def group_distance_defaultdict(points):
    """
    Rewrite distance grouping using defaultdict(list).
    close = dist < 2.0
    medium = 2.0-5.0
    far = >= 5.0
    Use defaultdict only.
    """

    group = defaultdict(list)

    for point in points:

        x, y, z = point

        dist = math.sqrt(x**2 + y**2 + z**2)

        if dist < 2.0:
            group["close"].append(point)

        elif 2.0 <= dist < 5.0:
            group["medium"].append(point)

        else:
            group["far"].append(point)

    return group


def demonstrate_difference():
    """
    Return a dict showing normal dict vs defaultdict behavior.
    """

    regular = {}

    try:
        regular["missing"]

    except KeyError as e:
        regular_error = str(e)

    dd = defaultdict(list)

    defaultdict_result = dd["missing"]

    return {
        "regular_dict_error": regular_error,
        "defaultdict_result": defaultdict_result
    }


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

    print(
        "PASS — is dict-like"
        if hasattr(result, '__getitem__')
        else "FAIL"
    )

    print(
        "PASS — Q1 has 3"
        if len(result.get("Q1", [])) == 3
        else f"FAIL — Q1: {result.get('Q1')}"
    )

    print(
        "PASS — Q2 has 2"
        if len(result.get("Q2", [])) == 2
        else f"FAIL — Q2: {result.get('Q2')}"
    )

    dist_result = group_distance_defaultdict(pts)

    print(
        "PASS — distance groups exist"
        if "close" in dist_result or "far" in dist_result
        else "FAIL — missing distance groups"
    )

    diff = demonstrate_difference()

    print(
        "PASS — demonstrates difference"
        if isinstance(diff, dict)
        else "FAIL — should return dict"
    )

    src = inspect.getsource(group_quadrant_defaultdict)

    forbidden_patterns = [
        "if key not in",
        "if point not in",
        "if x not in",
        "if y not in",
    ]

    print(
        "PASS — no if key not in"
        if not any(pattern in src for pattern in forbidden_patterns)
        else "FAIL — still using forbidden pattern"
    )