# Problem: Given a list of cluster dicts with keys 'size' and 'centroid', sort by size
#          descending, using distance of centroid from origin as a tiebreaker.
# Concept: A tuple as a sort key enables multi-level sorting — the first element is the
#          primary key, the second is the tiebreaker. Essential when one criterion is not
#          enough to produce a stable, deterministic ordering.
# You are done when:
#   [ ] Clusters are ordered by size largest-first
#   [ ] When two clusters have equal size, the one with centroid closer to origin comes first
#   [ ] A single sorted() call with one lambda handles both criteria
#   [ ] All test cases print PASS
# Hint: key=lambda c: (-c['size'], distance_to_origin(c['centroid']))

import math


def sort_clusters(clusters):
    """
    Return clusters sorted by size descending, centroid distance from origin ascending as tiebreaker.
    """
    pass


if __name__ == "__main__":
    clusters = [
        {"id": "A", "size": 5, "centroid": (3.0, 0.0, 0.0)},
        {"id": "B", "size": 8, "centroid": (1.0, 0.0, 0.0)},
        {"id": "C", "size": 5, "centroid": (1.0, 0.0, 0.0)},  # same size as A, closer
        {"id": "D", "size": 3, "centroid": (0.5, 0.0, 0.0)},
    ]
    result = sort_clusters(clusters)
    ids = [c["id"] for c in result]

    # B first (largest), then C before A (same size, C closer), then D
    print("PASS order" if ids == ["B", "C", "A", "D"] else f"FAIL order — got {ids}")
