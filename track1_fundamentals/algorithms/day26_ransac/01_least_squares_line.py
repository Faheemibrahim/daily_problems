# Problem: Write a function that fits a line to 2D points using least squares.
#          Return slope and intercept.
# Concept: Least squares minimises the sum of squared residuals — the optimal fit given
#          all data points. RANSAC builds on this but ignores outliers first.
# You are done when:
#   [ ] You compute slope m = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)
#   [ ] You compute intercept b = (Σy - m*Σx) / n
#   [ ] Works on perfectly collinear points (residuals near 0)
#   [ ] All test cases print PASS
# Hint: m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)


def fit_line_least_squares(points_2d):
    """
    Fit a line y = mx + b to a list of (x, y) points using least squares.
    Return (slope, intercept).
    """
    pass


if __name__ == "__main__":
    # Perfect line y = 2x + 1
    pts = [(0.0, 1.0), (1.0, 3.0), (2.0, 5.0), (3.0, 7.0), (4.0, 9.0)]
    m, b = fit_line_least_squares(pts)
    print("PASS slope" if abs(m - 2.0) < 1e-9 else f"FAIL slope — {m}")
    print("PASS intercept" if abs(b - 1.0) < 1e-9 else f"FAIL intercept — {b}")

    # Horizontal line
    pts2 = [(0.0, 5.0), (1.0, 5.0), (2.0, 5.0)]
    m2, b2 = fit_line_least_squares(pts2)
    print("PASS horizontal slope" if abs(m2) < 1e-9 else f"FAIL horizontal — m={m2}")
