# =============================================================================
# REVISION DAY 03 — List Comprehensions
# =============================================================================
# What: rewrite 5 operations as single-line list comprehensions
#       plus one dict comprehension
# Concept: list comprehension syntax, filtering, transforming, dict comprehension
# Done when:
#   [ ] every solution is a single line
#   [ ] no for loops — only comprehensions
#   [ ] dict comprehension produces correct key/value pairs
# Hint: dict comprehension looks like {k: v for k, v in something}
# =============================================================================

import math


def extract_x(points):
    """Return list of all x values. One line."""
    return [point[0] for point in points]


def negative_z(points):
    """Return points where z < 0. One line."""
    return [point for point in points if point[2] < 0]


def distances_from_origin(points):
    """Return list of distances from origin for every point. One line."""
    
    return [math.sqrt((x**2) + (y**2) + (z**2)) for x,y,z in points]


def within_radius(points, radius):
    """Return points within given radius from origin. One line."""
    return [(x,y,z) for x,y,z in points if ((x**2) + (y**2) + (z**2)) < radius]

def shift_points(points, dx, dy, dz):
    """Return new list with every point shifted by dx dy dz. One line."""
    return [(x+dx,y+dy,z+dz) for x,y,z in points]

def index_distance_dict(points):
    """Return dict: key=index, value=distance from origin. One line."""
    return {key: math.sqrt((x**2) + (y**2) + (z**2))  for key, (x,y,z) in enumerate(points)}


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import math
    pts = [
        (1.0,  2.0,  3.0),
        (4.0,  5.0, -1.0),
        (-2.0, 0.0,  7.0),
        (0.0, -3.0, -2.0),
    ]

    print("PASS — extract_x" if extract_x(pts) == [1.0, 4.0, -2.0, 0.0]
          else f"FAIL — extract_x got {extract_x(pts)}")

    print("PASS — negative_z" if negative_z(pts) == [(4.0,5.0,-1.0),(0.0,-3.0,-2.0)]
          else f"FAIL — negative_z got {negative_z(pts)}")

    dists = distances_from_origin(pts)
    expected_d0 = math.sqrt(1+4+9)
    print("PASS — distances_from_origin" if math.isclose(dists[0], expected_d0)
          else f"FAIL — distances_from_origin got {dists[0]} expected {expected_d0}")

    wr = within_radius(pts, 4.0)
    print("PASS — within_radius" if (1.0,2.0,3.0) not in wr and len(wr) >= 0
          else f"FAIL — within_radius")

    shifted = shift_points(pts, 1.0, 0.5, 0.0)
    print("PASS — shift_points" if shifted[0] == (2.0, 2.5, 3.0)
          else f"FAIL — shift_points got {shifted[0]}")

    idd = index_distance_dict(pts)
    print("PASS — index_distance_dict" if isinstance(idd, dict) and 0 in idd
          and math.isclose(idd[0], math.sqrt(14))
          else f"FAIL — index_distance_dict got {idd}")
