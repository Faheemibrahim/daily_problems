# Problem: Given a list of (x, y, z) tuples, sort them by distance from the origin
#          using sorted() with a key argument.
# Concept: sorted() with a key= lambda to sort by a computed value without modifying the list.
# You are done when:
#   [ ] You use sorted() with a key= argument
#   [ ] The key computes Euclidean distance from origin
#   [ ] The original list is not modified
#   [ ] All test cases print PASS
# Hint: key=lambda p: p[0]**2 + p[1]**2 + p[2]**2 avoids sqrt and sorts in the same order.

import math


def sort_by_distance(points):
    """
    Return a new list of points sorted by Euclidean distance from the origin (ascending).
    """

    
    # points.sort(key=lambda p: p[0]**2 + p[1]**2 + p[2]**2)

    # print(points)


    # return points 
    

    lst = sorted(points)

    lst.sort(key=lambda p: p[0]**2 + p[1]**2 + p[2]**2)

    print(lst)
    print(points)


    return lst
    


if __name__ == "__main__":
    pts = [
        (3.0, 0.0, 0.0),
        (0.0, 0.0, 1.0),
        (1.0, 1.0, 1.0),
        (0.0, 0.0, 0.0),
        (2.0, 2.0, 0.0),
    ]
    result = sort_by_distance(pts)
    distances = [math.sqrt(x**2 + y**2 + z**2) for x, y, z in result]
    is_sorted = all(distances[i] <= distances[i + 1] for i in range(len(distances) - 1))
    print("PASS" if is_sorted else f"FAIL — distances are {distances}")

    original_copy = pts[:]
    sort_by_distance(pts)
    print("PASS original unchanged" if pts == original_copy else "FAIL original was modified")
