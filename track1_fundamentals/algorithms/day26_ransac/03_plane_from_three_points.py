# Problem: Given 3 points, return the plane as (a, b, c, d) where ax + by + cz + d = 0.
# Concept: A plane in 3D is defined by its normal vector. The normal is the cross product
#          of two edge vectors from the three points. RANSAC uses this to fit planes.
# You are done when:
#   [ ] You compute two edge vectors: v1 = p2-p1, v2 = p3-p1
#   [ ] You compute the normal as the cross product of v1 and v2
#   [ ] You verify that all three input points satisfy ax+by+cz+d = 0 (within tolerance)
#   [ ] All test cases print PASS
# Hint: normal = (v1.y*v2.z - v1.z*v2.y, v1.z*v2.x - v1.x*v2.z, v1.x*v2.y - v1.y*v2.x)
#       d = -(a*p1.x + b*p1.y + c*p1.z)


def plane_from_three_points(p1, p2, p3):
    """
    Return (a, b, c, d) of the plane ax+by+cz+d=0 passing through p1, p2, p3.
    """
    pass


def point_to_plane_distance(point, plane):
    """Return the signed distance from point to plane (a,b,c,d)."""
    a, b, c, d = plane
    x, y, z = point
    norm = (a**2 + b**2 + c**2) ** 0.5
    return (a*x + b*y + c*z + d) / norm


if __name__ == "__main__":
    # Ground plane z = 0 -> normal is (0, 0, 1) -> plane is 0x+0y+1z+0=0
    p1, p2, p3 = (0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)
    plane = plane_from_three_points(p1, p2, p3)

    for pt in [p1, p2, p3]:
        d = abs(point_to_plane_distance(pt, plane))
        print(f"PASS p{[p1,p2,p3].index(pt)+1} on plane" if d < 1e-9 else f"FAIL distance={d}")

    # Point above plane should have nonzero distance
    above = (0.0, 0.0, 1.0)
    d_above = abs(point_to_plane_distance(above, plane))
    print("PASS above plane" if abs(d_above - 1.0) < 1e-9 else f"FAIL above — {d_above}")
