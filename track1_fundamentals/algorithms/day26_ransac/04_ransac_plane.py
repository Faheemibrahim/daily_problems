# Problem: Write ransac_plane(points, iterations=100, threshold=0.05).
#          Randomly sample 3 points, fit a plane, count inliers. Repeat and return the best plane.
# Concept: 3D RANSAC plane fitting is the same loop as 2D line fitting but with 3 sample points
#          and point-to-plane distance. This is used for ground plane removal in LiDAR pipelines.
# You are done when:
#   [ ] Each iteration samples 3 random points and fits a plane
#   [ ] Inliers are points within threshold distance of the fitted plane
#   [ ] Returns (a, b, c, d) coefficients of the best plane
#   [ ] All test cases print PASS
# Hint: Use plane_from_three_points and point_to_plane_distance from problem 03.

import random
import math


def plane_from_three_points(p1, p2, p3):
    v1 = tuple(p2[i] - p1[i] for i in range(3))
    v2 = tuple(p3[i] - p1[i] for i in range(3))
    a = v1[1]*v2[2] - v1[2]*v2[1]
    b = v1[2]*v2[0] - v1[0]*v2[2]
    c = v1[0]*v2[1] - v1[1]*v2[0]
    d = -(a*p1[0] + b*p1[1] + c*p1[2])
    return (a, b, c, d)


def point_to_plane_distance(point, plane):
    a, b, c, d = plane
    norm = math.sqrt(a**2 + b**2 + c**2)
    return abs(a*point[0] + b*point[1] + c*point[2] + d) / norm if norm > 0 else float("inf")


def ransac_plane(points, iterations=100, threshold=0.05, seed=None):
    """
    Fit a plane to points using RANSAC. Return (a, b, c, d) of the best plane.
    """
    pass


if __name__ == "__main__":
    random.seed(0)
    # Ground plane z ≈ 0 with noise, plus some outliers
    ground = [(random.uniform(-5, 5), random.uniform(-5, 5), random.gauss(0, 0.02)) for _ in range(80)]
    outliers = [(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0.5, 2.0)) for _ in range(20)]
    pts = ground + outliers
    random.shuffle(pts)

    plane = ransac_plane(pts, iterations=200, threshold=0.1, seed=0)
    a, b, c, d = plane
    norm = math.sqrt(a**2 + b**2 + c**2)
    # Normal should be close to (0, 0, 1) or (0, 0, -1)
    nz = abs(c / norm) if norm > 0 else 0
    print(f"Plane normal z-component: {nz:.3f} (expected ≈ 1.0)")
    print("PASS ground plane found" if nz > 0.9 else f"FAIL — z-component={nz:.3f}")
