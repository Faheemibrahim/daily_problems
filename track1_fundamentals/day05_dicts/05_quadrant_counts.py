# Problem: Given a quadrant dict (from problem 04), loop through it and return a dict
#          showing how many points are in each quadrant.
# Concept: Iterating over a dict of lists, computing a derived value (length) per entry.
# You are done when:
#   [ ] You loop using .items()
#   [ ] The result maps each quadrant key to an integer count
#   [ ] All test cases print PASS
# Hint: len(list_of_points) gives the count for each quadrant.


def count_per_quadrant(quadrant_dict):
    """
    Return a dict mapping each quadrant key to the number of points in it.
    """
    
    # print(quadrant_dict)

    d = {}

    # VALUES give you the count and the items give you the quadrant 
    for name,lst in quadrant_dict.items():
        # print(name,lst)

        
        d[name] = len(lst)

    return d



        

if __name__ == "__main__":
    q = {
        "Q1": [(1.0, 1.0, 0.0), (2.0, 3.0, 0.0), (4.0, 2.0, 0.0)],
        "Q2": [(-1.0, 1.0, 0.0), (-1.0, 2.0, 0.0)],
        "Q3": [(-1.0, -1.0, 0.0), (-2.0, -3.0, 0.0)],
        "Q4": [(1.0, -1.0, 0.0), (3.0, -1.0, 0.0)],
        "Q0": [(0.0, 1.0, 0.0)],
    }
    result = count_per_quadrant(q)
    expected = {"Q1": 3, "Q2": 2, "Q3": 2, "Q4": 2, "Q0": 1}
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
