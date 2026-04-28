# Problem: Given a cost matrix where cost[i][j] is the distance between old cone i
#          and new cone j, find the optimal assignment by trying all permutations.
# Concept: The assignment problem asks: given N old cones and N new cones, which pairing
#          minimises total distance? Brute force tries all N! permutations — correct but
#          O(N!) which is only feasible for tiny N. Hungarian is O(N³).
# You are done when:
#   [ ] You try every permutation of column assignments
#   [ ] You return the assignment list and its total cost
#   [ ] Results match scipy.optimize.linear_sum_assignment for all inputs
#   [ ] All test cases print PASS
# Hint: itertools.permutations(range(n)) gives all orderings of column indices.

import itertools


def brute_force_assignment(cost_matrix):
    """
    Find the minimum-cost assignment by exhaustive search.
    cost_matrix is a list of lists (N x N).
    Return (assignment, total_cost) where assignment[i] = j means old cone i -> new cone j.
    """
    pass


if __name__ == "__main__":
    cost = [
        [4.0, 1.0, 3.0],
        [2.0, 0.5, 5.0],
        [3.0, 2.0, 1.0],
    ]
    assignment, total = brute_force_assignment(cost)
    print(f"Assignment: {assignment}  Total cost: {total:.2f}")

    # Verify: assignment[i]=j means row i paired with col j, no repeats
    print("PASS unique cols" if len(set(assignment)) == 3 else f"FAIL unique — {assignment}")

    # Compare with scipy
    from scipy.optimize import linear_sum_assignment
    import numpy as np
    rows, cols = linear_sum_assignment(np.array(cost))
    scipy_cost = sum(cost[r][c] for r, c in zip(rows, cols))
    print("PASS optimal cost" if abs(total - scipy_cost) < 1e-9 else f"FAIL cost — got {total:.3f} scipy {scipy_cost:.3f}")
