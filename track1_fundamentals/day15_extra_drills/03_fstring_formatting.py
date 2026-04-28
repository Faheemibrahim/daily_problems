# Problem: Given a list of cluster dicts with keys 'id', 'centroid', and 'size',
#          format a neat table with aligned columns. Each row looks like:
#          Cluster 00 | size:  12 | centroid: x= 1.23 y= 4.56 z= 0.12
# Concept: f-string format specifiers for decimal precision ({:.2f}) and field width
#          ({:>6}) produce readable, aligned output — critical for debugging spatial data.
# You are done when:
#   [ ] IDs are zero-padded to 2 digits
#   [ ] Size field is right-aligned in a fixed-width column
#   [ ] Centroid values are shown with 2 decimal places
#   [ ] All columns line up regardless of value magnitude
#   [ ] All test cases print PASS
# Hint: f"{value:.2f}" for 2 decimal places; f"{value:>6}" for right-align in width 6.


def format_cluster_table(clusters):
    """
    Return a list of formatted strings, one per cluster.
    Format: "Cluster {id:02d} | size: {size:3d} | centroid: x={x:6.2f} y={y:6.2f} z={z:6.2f}"
    """
    pass


if __name__ == "__main__":
    clusters = [
        {"id": 1,  "size": 12, "centroid": (1.234, 4.567, 0.123)},
        {"id": 2,  "size": 5,  "centroid": (-0.1, 10.0, -0.500)},
        {"id": 10, "size": 100, "centroid": (0.0, 0.0, 0.0)},
    ]
    result = format_cluster_table(clusters)

    expected = [
        "Cluster 01 | size:  12 | centroid: x=  1.23 y=  4.57 z=  0.12",
        "Cluster 02 | size:   5 | centroid: x= -0.10 y= 10.00 z= -0.50",
        "Cluster 10 | size: 100 | centroid: x=  0.00 y=  0.00 z=  0.00",
    ]
    for i, (r, e) in enumerate(zip(result, expected)):
        print(f"PASS row {i}" if r == e else f"FAIL row {i}\n  got:      '{r}'\n  expected: '{e}'")
