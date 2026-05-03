# =============================================================================
# REVISION DAY 01 — Lists and Indexing
# =============================================================================
# What: given a list of (x,y,z) points perform 4 operations from scratch
# Concept: list traversal, axis tracking, no built-in min/max
# Done when:
#   [ ] find largest x using a loop and tracking variable
#   [ ] find point closest to origin using a loop
#   [ ] collect points where x>0 and z>0 into a new list
#   [ ] find min and max for each axis
#   [ ] all results returned in a dict, nothing printed inside functions
# Hint: initialise tracking variables from points[0] not from 0
# =============================================================================

import math


def analyse_points(points):
    """
    Returns a dict with keys:
      largest_x_point  -> the point with the largest x value
      closest_to_origin -> the point closest to (0,0,0)
      positive_xz      -> list of points where x>0 and z>0
      axis_stats       -> dict with x_min x_max y_min y_max z_min z_max
    """


    results = {
        "largest_x_point": None,
        "closest_to_origin": None,
        "positive_xz": [],
        "axis_stats": {}
    }

    # --------- 1 (largest x point)
    prev = points[0][0]
    final = points[0]

    for point in points:
        if point[0] > prev:
            prev = point[0]
            final = point

    results["largest_x_point"] = final 

    
    # ---------- 2 (distance from origin)

    indx = points[0]
    prev_distance = (points[0][0])**2 + (points[0][1])**2 + (points[0][2])**2 

    for x,y,z in points:
        distance = x*x + y*y + z*z
        
        if distance < prev_distance:
            indx = (x,y,z)
            prev_distance = distance

    results["closest_to_origin"] = indx

    # ---------- 3 (store points based on q)    

    lst = [(x,y,z) for x,y,z in points if x > 0 and z > 0] 
    #print(lst)
    results["positive_xz"] = lst
    
    # ---------- 4 (min-max each axis) 
    

    min_x = points[0][0]
    max_x = points[0][0]

    min_y = points[0][1]
    max_y = points[0][1]

    min_z = points[0][2]
    max_z = points[0][2]



    for x, y, z in points:
        if x > max_x:
            max_x = x

        if x < min_x:
            min_x = x
    
        if y > max_y:
            max_y = y

        if y < min_y:
            min_y = y
        
        if z > max_z:
            max_z = z

        if z < min_z:
            min_z = z

    results["axis_stats"] = { 
        "x_min": min_x,
        "x_max": max_x,
        "y_min": min_y,
        "y_max": max_y,
        "z_min": min_z,
        "z_max": max_z
    }

    return results 
                





# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0, -2.0, 3.0),
        (4.0,  5.0, -1.0),
        (-2.0, 0.0,  7.0),
        (3.0,  3.0,  2.0),
        (-1.0, 1.0,  1.0),
        (2.0, -1.0,  0.5),
    ]

    result = analyse_points(pts)

    checks = [
        (result["largest_x_point"] == (4.0, 5.0, -1.0),
         "largest_x_point"),
        (result["closest_to_origin"] == (1.0, -2.0, 3.0) or
         math.isclose(
             math.sqrt(sum(v**2 for v in result["closest_to_origin"])),
             min(math.sqrt(sum(v**2 for v in p)) for p in pts)
         ), "closest_to_origin"),
        (result["positive_xz"] == [(1.0,-2.0,3.0),(3.0,3.0,2.0),(2.0,-1.0,0.5)],
         "positive_xz"),
        (result["axis_stats"]["x_min"] == -2.0, "x_min"),
        (result["axis_stats"]["x_max"] ==  4.0, "x_max"),
        (result["axis_stats"]["z_min"] == -1.0, "z_min"),
        (result["axis_stats"]["z_max"] ==  7.0, "z_max"),
    ]

    for passed, name in checks:
        print(f"{'PASS' if passed else 'FAIL'} — {name}")
