# Problem: Use scipy.spatial.KDTree to perform radius search and verify results match
#          your hand-built KD-tree exactly.
# Concept: scipy.spatial.KDTree is the production-quality reference implementation.
#          Matching it confirms your tree is correct. In real pipelines, you use scipy;
#          building your own first ensures you understand what it does internally.
# You are done when:
#   [ ] You use scipy.spatial.KDTree (not your own tree) for this problem
#   [ ] Results match your radius_search from day21 for all test cases
#   [ ] All test cases print PASS
# Hint: tree = KDTree(np.array(points)); indices = tree.query_ball_point(query, r=radius)

import math
import numpy as np
from scipy.spatial import KDTree


def scipy_radius_search(points, query, radius):
    """
    Use scipy.spatial.KDTree to return all points within radius of query.
    points is a list of (x, y, z) tuples; query is a (x, y, z) tuple.
    """
    pass


if __name__ == "__main__":
    import random
    random.seed(3)
    pts = [(random.uniform(-5,5), random.uniform(-5,5), random.uniform(-5,5)) for _ in range(200)]
    query = (0.0, 0.0, 0.0)
    radius = 1.5

    scipy_result = set(scipy_radius_search(pts, query, radius))
    brute_result = {p for p in pts if math.sqrt(sum(v**2 for v in p)) <= radius}

    print("PASS scipy matches brute" if scipy_result == brute_result
          else f"FAIL — scipy has {len(scipy_result)}, brute has {len(brute_result)}")
