# Problem: Given a list of 10 points, slice out the first 3, the last 3, and every other point.
# Concept: Python slice notation [start:stop:step] applied to lists of structured data.
# You are done when:
#   [ ] You extract the first 3 elements correctly
#   [ ] You extract the last 3 elements correctly using negative indexing
#   [ ] You extract every other element using a step of 2
#   [ ] All test cases print PASS
# Hint: list[::2] gives every other element starting from index 0.


def slice_points(points):
    """
    Return a tuple of three lists:
      (first_3, last_3, every_other)
    """
    
    first_3 = points[0:3]
    print(first_3)
    last_3 = points[(len(points)-3):len(points)]
    print(last_3)
    
    every_other = points[0:len(points):2]
    print(every_other)


    return first_3, last_3, every_other
    
        

if __name__ == "__main__":
    pts = [(float(i), 0.0, 0.0) for i in range(10)]
    first_3, last_3, every_other = slice_points(pts)

    ok1 = first_3 == [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (2.0, 0.0, 0.0)]
    ok2 = last_3 == [(7.0, 0.0, 0.0), (8.0, 0.0, 0.0), (9.0, 0.0, 0.0)]
    ok3 = every_other == [(0.0, 0.0, 0.0), (2.0, 0.0, 0.0), (4.0, 0.0, 0.0),
                          (6.0, 0.0, 0.0), (8.0, 0.0, 0.0)]

    print("PASS first_3" if ok1 else f"FAIL first_3 — got {first_3}")
    print("PASS last_3" if ok2 else f"FAIL last_3 — got {last_3}")
    print("PASS every_other" if ok3 else f"FAIL every_other — got {every_other}")
