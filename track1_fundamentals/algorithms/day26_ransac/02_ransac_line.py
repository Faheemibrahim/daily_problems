# Problem: Write ransac_line(points, iterations=100, threshold=0.1).
#          Randomly sample 2 points, fit a line, count inliers. Repeat and return the best line.
# Concept: RANSAC (Random Sample Consensus) ignores outliers by design — it finds the model
#          that the most data points agree with, even when 50%+ of data are outliers.
# You are done when:
#   [ ] Each iteration samples exactly 2 random points
#   [ ] Inliers are points within threshold distance of the fitted line
#   [ ] The line with the most inliers is returned as (slope, intercept)
#   [ ] All test cases print PASS
# Hint: Distance from (x,y) to line y=mx+b is |y - (m*x + b)| / sqrt(m²+1).

import random
import math


def ransac_line(points, iterations=100, threshold=0.1, seed=None):
    """
    Fit a line to points using RANSAC. Return (slope, intercept) of the best line.
    """
    pass


if __name__ == "__main__":
    random.seed(42)
    # Mostly on y=2x+1, with 5 outliers
    inlier_pts = [(x*0.5, 2*x*0.5 + 1 + random.gauss(0, 0.02)) for x in range(20)]
    outlier_pts = [(random.uniform(0, 10), random.uniform(-10, 10)) for _ in range(5)]
    pts = inlier_pts + outlier_pts
    random.shuffle(pts)

    m, b = ransac_line(pts, iterations=200, threshold=0.2, seed=42)
    print(f"Fitted line: y = {m:.3f}x + {b:.3f}")
    print("PASS slope near 2" if abs(m - 2.0) < 0.3 else f"FAIL slope — {m:.3f}")
    print("PASS intercept near 1" if abs(b - 1.0) < 0.5 else f"FAIL intercept — {b:.3f}")
