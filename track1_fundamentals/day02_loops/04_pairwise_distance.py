# Problem: Write a nested loop that computes the Euclidean distance between every pair of
#          points (i, j) where i < j, and collect each (i, j, distance) triple.
# Concept: Nested loops, avoiding duplicate pairs with index comparison, distance formula.
# You are done when:
#   [ ] You use two nested for loops over indices
#   [ ] You skip pairs where i >= j so each pair appears exactly once
#   [ ] Distance is computed as sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
#   [ ] All test cases print PASS
# Hint: import math and use math.sqrt(); keep the inner loop condition i < j.

import math


def pairwise_distances(points):
    """
    Return a list of (i, j, distance) triples for every unique pair i < j.
    """
 
    store = []

    for i in range(len(points)):
        for j in range(i+1,len(points)):
                
                p1 = points[i]
                p2 = points[j]
              
                distance = math.sqrt(
                    (p1[0] - p2[0])**2 +
                    (p1[1] - p2[1])**2 +
                    (p1[2] - p2[2])**2
                )

                store.append((i,j,distance))

    return store

if __name__ == "__main__":
    pts = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    result = pairwise_distances(pts)
    expected = [
        (0, 1, 1.0),
        (0, 2, 1.0),
        (1, 2, math.sqrt(2)),
    ]
    ok = len(result) == len(expected) and all(
        r[0] == e[0] and r[1] == e[1] and abs(r[2] - e[2]) < 1e-9
        for r, e in zip(result, expected)
    )
    print("PASS" if ok else f"FAIL — got {result}")
