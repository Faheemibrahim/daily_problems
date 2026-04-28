# Problem: Given a list of Cluster objects, filter out clusters smaller than 5 points,
#          then find the one whose centroid is closest to the origin.
# Concept: Combining class methods (centroid, size) with list filtering and a min search —
#          exactly the post-clustering object selection step in a detection pipeline.
# You are done when:
#   [ ] You filter using cluster.size()
#   [ ] You compute distance from centroid to origin for each surviving cluster
#   [ ] You return the Cluster object (not just its centroid)
#   [ ] All test cases print PASS
# Hint: min(clusters, key=lambda cl: dist_to_origin(cl.centroid())) after filtering.

import math


class Cluster:
    def __init__(self, points):
        self.points = points

    def size(self):
        return len(self.points)

    def centroid(self):
        n = len(self.points)
        return (sum(p[0] for p in self.points) / n,
                sum(p[1] for p in self.points) / n,
                sum(p[2] for p in self.points) / n)


def nearest_large_cluster(clusters, min_size=5):
    """
    Return the Cluster with size >= min_size whose centroid is nearest to the origin.
    Return None if no clusters meet the size requirement.
    """
    pass


if __name__ == "__main__":
    c1 = Cluster([(1.0, 0.0, 0.0)] * 6)   # size 6, centroid (1,0,0)
    c2 = Cluster([(0.5, 0.0, 0.0)] * 3)   # size 3 — filtered out
    c3 = Cluster([(2.0, 0.0, 0.0)] * 5)   # size 5, centroid (2,0,0)

    result = nearest_large_cluster([c1, c2, c3])
    print("PASS" if result is c1 else f"FAIL — expected c1 (centroid closest to origin among large clusters)")

    result2 = nearest_large_cluster([c2])
    print("PASS none" if result2 is None else f"FAIL none — got {result2}")
