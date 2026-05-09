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

    d = {
        "Q1": 0,
        "Q2": 0,
        "Q3": 0,
        "Q4": 0
    }

    for point in points:

        x, y, z = point

        # Quadrant 1
        if x > 0 and y > 0:
            d["Q1"] += 1

        # Quadrant 2
        elif x < 0 and y > 0:
            d["Q2"] += 1

        # Quadrant 3
        elif x < 0 and y < 0:
            d["Q3"] += 1

        # Quadrant 4
        elif x > 0 and y < 0:
            d["Q4"] += 1

    return d



def get_centroid(points):
    """
    Return (mean_x, mean_y, mean_z) as a tuple.
    Do NOT print anything inside this function.
    Raise ValueError if points is empty.
    """

    if not points:
        raise ValueError("points is empty")
    
    
    sum_x,sum_y,sum_z = 0,0,0

    for point in points:
        x,y,z = point
        
        sum_x += x
        sum_y += y
        sum_z += z
       
        mean_x = sum_x/len(points)
        mean_y = sum_y/len(points)
        mean_z = sum_z/len(points)
       
    return (mean_x,mean_y,mean_z)
    


def get_nearest(query, points):
    """
    Return the single nearest point to query.
    Do NOT print anything inside this function.
    """

    prev_dist = math.inf
    store = (points[0][0],points[0][1],points[0][2])

    for point in points:
        distance =  math.sqrt((point[0] - query[0])**2 + (point[1] - query[1])**2 + (point[2] - query[2])**2)
        if distance < prev_dist:
            prev_dist = distance
            store = point
    
    return store


            
    
    

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
