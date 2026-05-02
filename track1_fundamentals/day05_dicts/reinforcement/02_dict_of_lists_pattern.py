# =============================================================================
# PROBLEM 02 — Dict of Lists Pattern
# =============================================================================
# What: group points into quadrants using the dict of lists pattern
# Concept: if key not in dict create list, then append — core pattern
# Done when:
#   [ ] write grouping pattern without any reference
#   [ ] count per quadrant correct
#   [ ] find biggest quadrant
#   [ ] return all three results, no print inside functions
# Hint: ALWAYS write before coding:
#       # key   = quadrant name string 'Q1' 'Q2' 'Q3' 'Q4'
#       # value = list of (x,y,z) points in that quadrant
# =============================================================================


def group_by_quadrant(points):
    """
    Group points by quadrant based on sign of x and y.
    Q1 = x>0 and y>0
    Q2 = x<0 and y>0
    Q3 = x<0 and y<0
    Q4 = x>0 and y<0
    key   = quadrant name string
    value = list of points
    Return the groups dict.
    """
    # key   =
    # value =
    # structure = { 'Q1': [(x,y,z), ...], 'Q2': [...], ... }
    pass


def count_per_quadrant(groups):
    """
    Given the groups dict return a new dict where
    key   = quadrant name
    value = count of points in that quadrant
    """
    # key   =
    # value =
    pass


def biggest_quadrant(counts):
    """Return the name of the quadrant with the most points."""
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0,  2.0, 0.0),
        (-1.0, 2.0, 0.0),
        (1.0, -2.0, 0.0),
        (-1.0,-2.0, 0.0),
        (3.0,  4.0, 0.0),
        (-3.0,-4.0, 0.0),
        (2.0, -1.0, 0.0),
        (-2.0, 1.0, 0.0),
        (5.0,  1.0, 0.0),
    ]

    groups = group_by_quadrant(pts)
    print("PASS — returns dict"   if isinstance(groups, dict)          else "FAIL — not a dict")
    print("PASS — Q1 has 3"       if len(groups.get("Q1", [])) == 3    else f"FAIL — Q1: {groups.get('Q1')}")
    print("PASS — Q2 has 2"       if len(groups.get("Q2", [])) == 2    else f"FAIL — Q2: {groups.get('Q2')}")
    print("PASS — values are lists" if all(isinstance(v, list) for v in groups.values())
          else "FAIL — values should be lists")

    counts = count_per_quadrant(groups)
    print("PASS — counts dict"    if isinstance(counts, dict)           else "FAIL — counts not dict")
    print("PASS — Q1 count 3"     if counts.get("Q1") == 3             else f"FAIL — Q1 count {counts.get('Q1')}")

    biggest = biggest_quadrant(counts)
    print("PASS — biggest is Q1"  if biggest == "Q1"                   else f"FAIL — biggest is {biggest}")
