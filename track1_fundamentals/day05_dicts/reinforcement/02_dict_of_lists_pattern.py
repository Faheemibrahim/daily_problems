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
    d ={
        "Q1": [],
        "Q2": [],
        "Q3": [],
        "Q4": [],
    }

    for point in points:

        x,y,z = point 

        if x>0 and y>0:
            d["Q1"].append(point)

        if x<0 and y>0:
            d["Q2"].append(point)

        if x<0 and y<0:
            d["Q3"].append(point)
        
        if x>0 and y<0:
            d["Q4"].append(point)

    lst = []

    for key,value in d:
        store = f"{key}: {value}"
        lst.append(store)
    
    #print(lst)

    return d

    # key   =
    # value =
    # structure = { 'Q1': [(x,y,z), ...], 'Q2': [...], ... }
    


def count_per_quadrant(groups):
    """
    Return the groups dict.
    """

    lst = []

    for key,item in groups.items():
        print(key,len(item)) 
        groups[key] = len(item)        
    
    return groups
    

def biggest_quadrant(counts):
    """Return the name of the quadrant with the most points."""


    prev_value = next(iter(counts.values())) # how do you assing the first key ? 

    for key , value in counts.items():
        print(key, value)
        if value > prev_value:
            final_key = key
            prev_value = value
    

    return final_key

    # # return final_key
    # print("big_leagues")
    # print(next(iter(counts.items())))
    # print(counts)
    

    
            

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
