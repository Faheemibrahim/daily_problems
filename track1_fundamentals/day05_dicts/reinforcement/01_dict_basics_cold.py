# =============================================================================
# PROBLEM 01 — Dict Basics Cold
# =============================================================================
# What: write all 5 basic dict operations from memory in one function
# Concept: create add update delete check loop — muscle memory
# Done when:
#   [ ] all 5 operations work without looking at notes
#   [ ] function returns the final dict
#   [ ] no print inside the function
# Hint: write this in a comment before any code:
#       # key   = cone name (string)
#       # value = (x,y,z) position tuple
# =============================================================================


def build_cone_dict():
    """
    Create a dict of 5 cones.
    Update cone_2 position.
    Delete cone_4.
    Check cone_3 exists before accessing.
    Return the final dict.
    key   = cone name string e.g. 'cone_1'
    value = (x, y, z) tuple
    """
    pass


def loop_and_collect(cone_dict):
    """
    Loop through cone_dict and return a list of strings
    formatted as 'cone_name: (x, y, z)' for each entry.
    """
    pass


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    result = build_cone_dict()

    print("PASS — is dict"     if isinstance(result, dict)          else "FAIL — not a dict")
    print("PASS — cone_4 gone" if "cone_4" not in result            else "FAIL — cone_4 still exists")
    print("PASS — cone_3 exists" if "cone_3" in result              else "FAIL — cone_3 missing")
    print("PASS — has 4 cones" if len(result) == 4                  else f"FAIL — expected 4 got {len(result)}")
    print("PASS — values are tuples" if all(isinstance(v, tuple) for v in result.values())
          else "FAIL — values should be tuples")

    labels = loop_and_collect(result)
    print("PASS — loop_and_collect returns list" if isinstance(labels, list)
          else "FAIL — should return list")
    print("PASS — correct count" if len(labels) == len(result)
          else f"FAIL — expected {len(result)} labels got {len(labels)}")
