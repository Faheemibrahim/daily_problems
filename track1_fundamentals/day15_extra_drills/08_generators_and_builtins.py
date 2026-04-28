# Problem: Four generator/builtin sub-problems:
#   1. Compute sum of all x values using sum() with a generator expression — no list.
#   2. Use any() to check if any point has z > 1.0.
#   3. Use all() to check if all points are inside a bounding box.
#   4. Rewrite centroid using sum() and generators — no building x_vals/y_vals/z_vals lists.
# Concept: Generator expressions feed sum/any/all lazily — no intermediate list is built,
#          saving memory and often time. This is the idiomatic Python way for aggregation.
# You are done when:
#   [ ] No intermediate list is built anywhere in problems 1-3
#   [ ] centroid uses sum() with generator expressions, not list comprehensions
#   [ ] All test cases print PASS
# Hint: sum(p[0] for p in points) is a generator expression inside sum() — no brackets [].


def sum_x(points):
    """Return the sum of all x values using sum() and a generator expression."""
    pass


def any_z_above(points, threshold=1.0):
    """Return True if any point has z > threshold — use any()."""
    pass


def all_inside_box(points, x_range=5.0, y_range=5.0, z_min=-0.5, z_max=0.3):
    """Return True if all points are inside the bounding box — use all()."""
    pass


def centroid(points):
    """Return (mean_x, mean_y, mean_z) using sum() with generator expressions."""
    pass


if __name__ == "__main__":
    pts = [(1.0, 0.0, 0.1), (2.0, 0.0, 0.2), (3.0, 0.0, -0.1)]

    print("PASS sum_x" if sum_x(pts) == 6.0 else f"FAIL sum_x — {sum_x(pts)}")

    print("PASS any_z False" if not any_z_above(pts) else "FAIL any_z False")
    pts_with_high_z = pts + [(0.0, 0.0, 2.0)]
    print("PASS any_z True" if any_z_above(pts_with_high_z) else "FAIL any_z True")

    print("PASS all_inside True" if all_inside_box(pts) else "FAIL all_inside True")
    pts_outside = pts + [(10.0, 0.0, 0.0)]
    print("PASS all_inside False" if not all_inside_box(pts_outside) else "FAIL all_inside False")

    c = centroid(pts)
    expected = (2.0, 0.0, 0.2/3)
    ok = all(abs(c[i] - expected[i]) < 1e-9 for i in range(3))
    print("PASS centroid" if ok else f"FAIL centroid — {c}")
