# =============================================================================
# REVISION DAY 02 — Loops
# =============================================================================
# What: 4 loop tasks on a list of (x,y,z) points
# Concept: enumerate, zip, nested loops, building results into collections
# Done when:
#   [ ] enumerate builds list of formatted strings
#   [ ] zip computes paired distances
#   [ ] nested loop finds the single closest pair
#   [ ] loop builds dict of index -> distance
#   [ ] all functions return, none print
# Hint: unpack tuples inside loops with x,y,z = point
# =============================================================================

import math


def label_points(points):
    """Return list of strings like 'point 0: (1.0, 2.0, 3.0)'."""
    lst = []
    for idx, value in enumerate(points):
         store = f"point {idx}: {value}"
         lst.append(store)
    
    return lst


def paired_distances(points_a, points_b):
    """Return list of distances between each paired point using zip."""
    lst = []

    for points in zip(points_a,points_b):

        point_a = points[0]
        point_b = points[1]

        if point_a > point_b:
            distance = (point_a[0] - point_b[0]) + (point_a[1] - point_b[1]) + (point_a[2] - point_b[2])
        else:
            distance = (point_b[0] - point_a[0]) + (point_b[1] - point_a[1]) + (point_b[2] - point_a[2])

        lst.append(distance)

    return lst


def closest_pair(points):
    """Return (p1, p2) the pair of distinct points with smallest distance."""

    prev_dist = math.inf

    for i in range(len(points)):
        for j in range(i+1,len(points)):

            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]

            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2

            distance = (dx*dx + dy*dy + dz*dz) 
  
            if distance < prev_dist:
                prev_dist = distance
                final_p1 = points[i]
                final_p2 = points[j]

    
    return final_p1, final_p2



def index_to_distance(points):
    """Return dict where key=index, value=distance from origin."""
    
    d ={}

    for i,point in enumerate(points): 
        x,y,z = point
        distance  = (x + y + z)

        d[i] = distance
    
    return d 
    

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (1.0, 0.0, 0.0),
        (0.0, 2.0, 0.0),
        (0.0, 0.0, 3.0),
        (1.0, 1.0, 1.0),
    ]

    labels = label_points(pts)
    print("PASS — label_points" if labels[0] == "point 0: (1.0, 0.0, 0.0)"
          else f"FAIL — label_points got {labels[0]}")

    pts_a = [(0.0,0.0,0.0), (1.0,0.0,0.0)]
    pts_b = [(3.0,0.0,0.0), (1.0,0.0,0.0)]
    pd = paired_distances(pts_a, pts_b)
    print("PASS — paired_distances" if math.isclose(pd[0], 3.0) and math.isclose(pd[1], 0.0)
          else f"FAIL — paired_distances got {pd}")

    p1, p2 = closest_pair(pts)
    dist = math.sqrt(sum((a-b)**2 for a,b in zip(p1,p2)))
    min_dist = min(
        math.sqrt(sum((a-b)**2 for a,b in zip(pts[i],pts[j])))
        for i in range(len(pts)) for j in range(len(pts)) if i != j
    )
    print("PASS — closest_pair" if math.isclose(dist, min_dist)
          else f"FAIL — closest_pair dist={dist} expected {min_dist}")

    itd = index_to_distance(pts)
    print("PASS — index_to_distance" if math.isclose(itd[0], 1.0) and math.isclose(itd[1], 2.0)
          else f"FAIL — index_to_distance got {itd}")
