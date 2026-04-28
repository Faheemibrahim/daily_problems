# Problem: Apply ransac_plane to a simulated ground plane point cloud with noise and outliers.
#          Verify it correctly identifies the ground plane and separates inliers from outliers.
# Concept: RANSAC ground removal replaces the naive z-threshold filter used in early pipeline
#          versions — it handles tilted ground and is robust to a high fraction of outliers.
# You are done when:
#   [ ] ransac_plane correctly identifies the z≈0 plane among mixed data
#   [ ] You correctly label each point as ground (inlier) or non-ground (outlier)
#   [ ] Precision and recall of ground detection are both > 90%
#   [ ] All test cases print PASS
# Hint: After finding the best plane, filter points with distance < threshold to get ground points.

import random
import math


def plane_from_three_points(p1, p2, p3):
    v1 = tuple(p2[i]-p1[i] for i in range(3))
    v2 = tuple(p3[i]-p1[i] for i in range(3))
    a = v1[1]*v2[2]-v1[2]*v2[1]; b = v1[2]*v2[0]-v1[0]*v2[2]; c = v1[0]*v2[1]-v1[1]*v2[0]
    return (a, b, c, -(a*p1[0]+b*p1[1]+c*p1[2]))


def point_to_plane_distance(pt, plane):
    a,b,c,d = plane; n = math.sqrt(a**2+b**2+c**2)
    return abs(a*pt[0]+b*pt[1]+c*pt[2]+d)/n if n>0 else float("inf")


def ransac_plane(points, iterations=100, threshold=0.05, seed=None):
    """Paste your solution from problem 04 here."""
    pass


def segment_ground(points, plane, threshold=0.05):
    """
    Return (ground_points, nonground_points) by splitting on plane distance.
    """
    pass


if __name__ == "__main__":
    random.seed(1)
    ground_pts = [(random.uniform(-5,5), random.uniform(-5,5), random.gauss(0, 0.02)) for _ in range(100)]
    nonground_pts = [(random.uniform(-5,5), random.uniform(-5,5), random.uniform(0.3, 2.0)) for _ in range(50)]
    all_pts = ground_pts + nonground_pts
    random.shuffle(all_pts)

    plane = ransac_plane(all_pts, iterations=200, threshold=0.08, seed=1)
    ground, nonground = segment_ground(all_pts, plane, threshold=0.08)

    # Points that were truly ground
    true_ground_set = set(map(tuple, ground_pts))
    found_ground_set = set(map(tuple, ground))

    tp = len(true_ground_set & found_ground_set)
    precision = tp / len(found_ground_set) if found_ground_set else 0
    recall = tp / len(true_ground_set) if true_ground_set else 0

    print(f"Precision: {precision:.2f}  Recall: {recall:.2f}")
    print("PASS precision" if precision > 0.9 else f"FAIL precision — {precision:.2f}")
    print("PASS recall" if recall > 0.9 else f"FAIL recall — {recall:.2f}")
