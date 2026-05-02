# Problem: Group a list of 10 (x, y, z) points into a dict by quadrant
#          Q1 (x>0, y>0), Q2 (x<0, y>0), Q3 (x<0, y<0), Q4 (x>0, y<0).
#          Points on axes (x=0 or y=0) go into "Q0".
# Concept: Building a dict of lists — a grouping pattern central to spatial algorithms.
# You are done when:
#   [ ] Every point is assigned to exactly one quadrant key
#   [ ] Points on an axis are handled (no crash, go to Q0)
#   [ ] All test cases print PASS
# Hint: Use an if-elif chain to determine the key, then dict.setdefault(key, []).append(point).


def group_by_quadrant(points):
    """
    Return a dict with keys 'Q1', 'Q2', 'Q3', 'Q4', 'Q0' mapping to lists of points.
    Only include keys that have at least one point.
    """

    d = {

    }
    
    for x,y,z in points:
        #print(x,y,z)
        
        #q1
        if x > 0 and y > 0:
            key = "Q1"
            if key in d:   # already created so append 
                d[key].append((x,y,z))
            else:
                d[key] = [] 
                d[key].append((x,y,z))
        
        #q2
        elif x < 0 and y > 0:
            key = "Q2"
            if key in d:   # already created so append 
                d[key].append((x,y,z))
            else:
                d[key] = [] 
                d[key].append((x,y,z))

        #q3
        elif  x < 0 and y < 0:
            key = "Q3"
            if key in d:   # already created so append 
                d[key].append((x,y,z))
            else:
                d[key] = [] 
                d[key].append((x,y,z))

        #q4
        elif x > 0 and y < 0: 
            key = "Q4"
            if key in d:   # already created so append 
                d[key].append((x,y,z))
            else:
                d[key] = [] 
                d[key].append((x,y,z))
        
        else:
            key = "Q0"
            if key in d:   # already created so append 
                d[key].append((x,y,z))
            else:
                d[key] = [] 
                d[key].append((x,y,z))


    print(d.items())
    
    return d 


if __name__ == "__main__":
    pts = [
        (1.0, 1.0, 0.0),   # Q1
        (-1.0, 1.0, 0.0),  # Q2
        (-1.0, -1.0, 0.0), # Q3
        (1.0, -1.0, 0.0),  # Q4
        (2.0, 3.0, 0.0),   # Q1
        (0.0, 1.0, 0.0),   # Q0
        (-2.0, -3.0, 0.0), # Q3
        (4.0, 2.0, 0.0),   # Q1
        (-1.0, 2.0, 0.0),  # Q2
        (3.0, -1.0, 0.0),  # Q4
    ]
    result = group_by_quadrant(pts)

    print("PASS Q1 count" if len(result.get("Q1", [])) == 3 else f"FAIL Q1 — {result.get('Q1')}")
    print("PASS Q2 count" if len(result.get("Q2", [])) == 2 else f"FAIL Q2 — {result.get('Q2')}")
    print("PASS Q3 count" if len(result.get("Q3", [])) == 2 else f"FAIL Q3 — {result.get('Q3')}")
    print("PASS Q4 count" if len(result.get("Q4", [])) == 2 else f"FAIL Q4 — {result.get('Q4')}")
    print("PASS Q0 count" if len(result.get("Q0", [])) == 1 else f"FAIL Q0 — {result.get('Q0')}")
