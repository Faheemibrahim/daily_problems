# Warmup Day 15 — Extra Drills retention
# Topics: lambda sort, defaultdict, list-of-dicts filter, zip pairing, error handling
# Fill in each block so all PASS lines print.

# ── 1. Lambda sort ────────────────────────────────────────────────────────────
points = [(3, 1, 0.5), (1, 4, 0.1), (2, 2, 0.9)]
# Sort by z (index 2) ascending using sorted() with a lambda key:
sorted_pts = sorted(points, key=lambda p: p[2])
print("PASS lambda_sort" if sorted_pts[0][2] == 0.1 and sorted_pts[-1][2] == 0.9
      else f"FAIL lambda_sort — {sorted_pts}")

# ── 2. defaultdict grouping ───────────────────────────────────────────────────
from collections import defaultdict
readings = [("lidar", 1.0), ("camera", 2.0), ("lidar", 3.0), ("camera", 4.0)]
groups = defaultdict(list)
for sensor, val in readings:
    groups[sensor].append(val)
print("PASS defaultdict" if len(groups["lidar"]) == 2 and len(groups["camera"]) == 2
      else f"FAIL defaultdict — {dict(groups)}")

# ── 3. List-of-dicts filter ───────────────────────────────────────────────────
cones = [{"id": 0, "dist": 1.2}, {"id": 1, "dist": 3.5}, {"id": 2, "dist": 0.8}]
# Keep only cones with dist < 2.0:
close = [c for c in cones if c["dist"] < 2.0]
print("PASS dict_filter" if len(close) == 2 else f"FAIL dict_filter — {close}")

# ── 4. zip pairing ────────────────────────────────────────────────────────────
ids = [10, 11, 12]
positions = [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
paired = {cid: pos for cid, pos in zip(ids, positions)}
print("PASS zip_pair" if paired[11] == (3.0, 4.0) else f"FAIL zip_pair — {paired}")

# ── 5. Error handling ─────────────────────────────────────────────────────────
def safe_divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

caught = False
try:
    safe_divide(5, 0)
except ValueError:
    caught = True
print("PASS error_handling" if caught else "FAIL error_handling")
