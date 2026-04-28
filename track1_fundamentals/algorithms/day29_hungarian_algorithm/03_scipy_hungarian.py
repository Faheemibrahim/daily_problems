# Problem: Use scipy.optimize.linear_sum_assignment to solve the assignment problem.
#          Verify it gives lower or equal cost than your greedy version.
# Concept: scipy's implementation is the Jonker-Volgenant algorithm (O(N³)).
#          For N=5 cones, both are instant; for N=100 cones in a dense field, greedy fails
#          to find the true minimum cost pairing.
# You are done when:
#   [ ] You call scipy.optimize.linear_sum_assignment on a numpy cost matrix
#   [ ] You extract the assignment as a list (row i -> col assignment[i])
#   [ ] Total cost from scipy <= total cost from greedy on all test inputs
#   [ ] All test cases print PASS
# Hint: rows, cols = linear_sum_assignment(cost_array); zip(rows, cols) gives pairs.

import numpy as np
from scipy.optimize import linear_sum_assignment


def scipy_optimal_assignment(cost_matrix):
    """
    Use scipy to find the minimum cost assignment.
    cost_matrix: list of lists or numpy array (N x N).
    Return (assignment_list, total_cost) where assignment_list[i] = j.
    """
    pass


if __name__ == "__main__":
    import random
    random.seed(11)

    # Test 1: known optimal
    cost = [[4.0, 1.0, 3.0], [2.0, 0.5, 5.0], [3.0, 2.0, 1.0]]
    asgn, total = scipy_optimal_assignment(cost)
    print(f"Optimal: {asgn}  cost={total:.2f}")
    print("PASS unique" if len(set(asgn)) == 3 else f"FAIL unique — {asgn}")

    # Test 2: greedy >= optimal on random 5x5
    cost5 = [[random.uniform(0, 10) for _ in range(5)] for _ in range(5)]

    def greedy_cost(cm):
        n = len(cm); flat = sorted((cm[i][j], i, j) for i in range(n) for j in range(n))
        used_r, used_c = set(), set(); total = 0.0
        for c, i, j in flat:
            if i not in used_r and j not in used_c:
                total += c; used_r.add(i); used_c.add(j)
        return total

    _, opt_cost = scipy_optimal_assignment(cost5)
    g_cost = greedy_cost(cost5)
    print(f"Greedy={g_cost:.3f}  Optimal={opt_cost:.3f}")
    print("PASS optimal <= greedy" if opt_cost <= g_cost + 1e-9 else f"FAIL — optimal {opt_cost:.3f} > greedy {g_cost:.3f}")
