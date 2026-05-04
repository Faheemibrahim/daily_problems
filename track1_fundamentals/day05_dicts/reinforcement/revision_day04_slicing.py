# =============================================================================
# REVISION DAY 04 — Slicing, Nesting, Sorting
# =============================================================================
# What: 6 slicing and sorting tasks on a list of 12 points
# Concept: slice syntax, reverse, step, restructuring, sorted with key/lambda
# Done when:
#   [ ] first/last/middle slices correct
#   [ ] reverse uses slicing not .reverse()
#   [ ] flat list converted to tuples correctly
#   [ ] both sorts use key argument not manual loops
# Hint: sorted(points, key=lambda p: p[2]) sorts by z value
# =============================================================================

import math


def slice_sections(points):
    """Return dict with keys first4, last4, middle4."""
    
    # create the keys 
    d = {
        "first4": None,
        "last4": None,
        "middle4": None
    }

    chunk = (len(points) // 3) 
    
    # print(points[0:chunk])
    # print(points[chunk:2*chunk])
    # print(points[2*chunk:])

    # dynamic 
    d["first4"] =  points[0:chunk]
    d["middle4"] = points[chunk:2*chunk]
    d["last4"] =  points[2*chunk:]


   
    
    # print(points)
    
    # print(points[0:4])
    # print(points[4:8])
    # print(points[8:12])

    # hard coded 
    # d["first4"] = points[0:4]
    # d["middle4"] = points[4:8]
    # d["last4"] = points[8:12]
    
    return d


    # just the dict 
    #d ={}




    return 


def reverse_list(points):
    """Return reversed list using slicing only."""
    return points[::-1]


def flat_to_tuples(flat):
    """Convert [x1,y1,z1,x2,y2,z2,...] to [(x1,y1,z1),(x2,y2,z2),...]."""
    
    #print(flat[::3])
    lst = []

    for i in range(0,len(flat),3):
        #print(flat[i:i+3])
        lst.append(tuple(flat[i:i+3]))

    return lst


def sort_by_z(points):
    """Return points sorted by z ascending using sorted() with key."""

    return sorted(points, key=lambda p: p[2])
    
    
        


def sort_by_distance(points):
    """Return points sorted by distance from origin using sorted() with lambda."""
    
    return sorted(points, key=lambda p: (p[0]+p[1]+p[2]))


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0,2.0,3.0),(4.0,5.0,6.0),(7.0,8.0,9.0),(10.0,11.0,12.0),
        (2.0,3.0,1.0),(5.0,6.0,4.0),(8.0,9.0,7.0),(11.0,12.0,10.0),
        (3.0,1.0,2.0),(6.0,4.0,5.0),(9.0,7.0,8.0),(12.0,10.0,11.0),
    ]

    s = slice_sections(pts)
    print("PASS — first4"  if s["first4"]  == pts[:4]  else f"FAIL — first4")
    print("PASS — last4"   if s["last4"]   == pts[-4:] else f"FAIL — last4")
    print("PASS — middle4" if s["middle4"] == pts[4:8] else f"FAIL — middle4")

    rev = reverse_list(pts)
    print("PASS — reverse" if rev == pts[::-1] else f"FAIL — reverse got {rev[:2]}")

    flat = [1.0,2.0,3.0, 4.0,5.0,6.0, 7.0,8.0,9.0]
    tuples = flat_to_tuples(flat)
    print("PASS — flat_to_tuples" if tuples == [(1.0,2.0,3.0),(4.0,5.0,6.0),(7.0,8.0,9.0)]
          else f"FAIL — flat_to_tuples got {tuples}")

    small = [(3.0,0.0,5.0),(1.0,0.0,1.0),(2.0,0.0,3.0)]
    sz = sort_by_z(small)
    print("PASS — sort_by_z" if sz[0][2] <= sz[1][2] <= sz[2][2]
          else f"FAIL — sort_by_z got {sz}")

    sd = sort_by_distance(small)
    dists = [math.sqrt(sum(v**2 for v in p)) for p in sd]
    print("PASS — sort_by_distance" if dists == sorted(dists)
          else f"FAIL — sort_by_distance")
