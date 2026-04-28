# Problem: Given a list of raw points, use a set to avoid processing duplicate points,
#          then group survivors into a PointCloud and return its centroid.
# Concept: Combining set deduplication with a class — deduplication before construction
#          keeps the PointCloud clean without needing post-processing.
# You are done when:
#   [ ] You use a set to eliminate duplicates
#   [ ] You add only unique points to the PointCloud
#   [ ] You return the centroid of the resulting PointCloud
#   [ ] All test cases print PASS
# Hint: A seen set of tuples lets you check and add in one pass before calling pc.add().


class PointCloud:
    def __init__(self):
        self.points = []

    def add(self, point):
        self.points.append(point)

    def size(self):
        return len(self.points)

    def centroid(self):
        n = len(self.points)
        return (sum(p[0] for p in self.points) / n,
                sum(p[1] for p in self.points) / n,
                sum(p[2] for p in self.points) / n)


def deduplicate_and_centroid(raw_points):
    """
    Remove duplicate points using a set, build a PointCloud, and return its centroid.
    """
    pass


if __name__ == "__main__":
    raw = [
        (1.0, 0.0, 0.0),
        (2.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),  # duplicate
        (3.0, 0.0, 0.0),
    ]
    result = deduplicate_and_centroid(raw)
    expected = (2.0, 0.0, 0.0)
    ok = all(abs(result[i] - expected[i]) < 1e-9 for i in range(3))
    print("PASS" if ok else f"FAIL — got {result}, expected {expected}")
