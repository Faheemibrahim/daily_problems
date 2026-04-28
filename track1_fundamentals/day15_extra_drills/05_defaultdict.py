# Problem: Three defaultdict sub-problems:
#   1. Rewrite quadrant grouping from day05 using defaultdict(list).
#   2. Rewrite voxel grid from day06 using defaultdict(list).
#   3. Demonstrate the difference when accessing a missing key in dict vs defaultdict.
# Concept: collections.defaultdict auto-creates missing keys — eliminating
#          the if-key-not-in-dict boilerplate from every grouping operation.
# You are done when:
#   [ ] No manual key-existence checks (no setdefault, no `if key not in d`)
#   [ ] defaultdict handles missing keys automatically in all three problems
#   [ ] Problem 3 shows dict raises KeyError while defaultdict returns the default
#   [ ] All test cases print PASS
# Hint: collections.defaultdict(list) creates a new empty list for any missing key
#       on first access — d[missing_key] returns [] without error.

from collections import defaultdict


def group_by_quadrant(points):
    """
    Group (x, y, z) points by quadrant Q1/Q2/Q3/Q4/Q0.
    Use defaultdict(list) — no manual key checks.
    """
    pass


def build_voxel_dict(points, voxel_size=0.5):
    """
    Build voxel grid using defaultdict(list) — no manual key checks.
    """
    pass


def demonstrate_defaultdict():
    """
    Return a tuple (dict_result, defaultdict_result) showing what happens
    when accessing key 'missing' in a plain dict vs a defaultdict(list).
    dict_result should be the string 'KeyError'.
    defaultdict_result should be an empty list [].
    """
    pass


if __name__ == "__main__":
    pts = [(1.0, 1.0, 0.0), (-1.0, 1.0, 0.0), (-1.0, -1.0, 0.0), (1.0, -1.0, 0.0)]
    q = group_by_quadrant(pts)
    print("PASS quadrant" if len(q["Q1"]) == 1 and len(q["Q2"]) == 1 else f"FAIL quadrant — {dict(q)}")

    vpts = [(0.1, 0.0, 0.0), (0.2, 0.0, 0.0), (0.9, 0.0, 0.0)]
    vd = build_voxel_dict(vpts)
    print("PASS voxel" if len(vd[(0,0,0)]) == 2 and len(vd[(1,0,0)]) == 1 else f"FAIL voxel — {dict(vd)}")

    d_res, dd_res = demonstrate_defaultdict()
    print("PASS dict KeyError" if d_res == "KeyError" else f"FAIL dict KeyError — {d_res}")
    print("PASS defaultdict empty list" if dd_res == [] else f"FAIL defaultdict — {dd_res}")
