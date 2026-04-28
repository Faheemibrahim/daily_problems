# Problem: Given a list of (x, y, z) points, find the min and max for each axis separately.
# Concept: Iterating over structured data and tracking per-axis extremes without numpy.
# You are done when:
#   [ ] You find min and max x, y, and z independently
#   [ ] You use no built-in min() or max()
#   [ ] You return all six values in a clear structure
#   [ ] All test cases print PASS
# Hint: You can unpack each tuple inside the loop with: x, y, z = point


def axis_min_max(points):
    """
    Return a dict with keys 'x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max'.
    Do not use min() or max().
    """
    
    x_max = points[0][0]
    x_min = points[0][0]

    y_max = points[0][1]
    y_min = points[0][1]

    z_max = points[0][2]
    z_min = points[0][2]

    for key in points:

        if key[0] > x_max:
            x_max = key[0] 
        
        if key[0] < x_min:
            x_min = key[0]
        
        if key[1] > y_max:
            y_max = key[1] 
        
        if key[1] < y_min:
            y_min = key[1]

        if key[2] > z_max:
            z_max = key[2] 
        
        if key[2] < z_min:
            z_min = key[2]
        
    return {
        "x_min": x_min,
        "x_max": x_max,
        "y_min": y_min,
        "y_max": y_max,
        "z_min": z_min,
        "z_max": z_max
    }
            

if __name__ == "__main__":
    pts = [
        (1.0, -2.0, 3.0),
        (4.0, 5.0, -1.0),
        (-2.0, 0.0, 7.0),
        (3.0, 3.0, 0.0),
    ]
    result = axis_min_max(pts)
    expected = {
        "x_min": -2.0, "x_max": 4.0,
        "y_min": -2.0, "y_max": 5.0,
        "z_min": -1.0, "z_max": 7.0,
    }
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
