# Problem: Write a greedy assignment that always picks the closest unmatched pair.
# Concept: Greedy is faster (O(N² log N)) but not always optimal — it can get stuck with
#          a bad early choice. Comparing greedy vs Hungarian shows why optimality matters.
# You are done when:
#   [ ] You iteratively pick the minimum-cost unmatched (row, col) pair
#   [ ] You mark both row and column as used after each pick
#   [ ] You compare total cost with brute force on small examples
#   [ ] All test cases print PASS
# Hint: Flatten cost matrix to (cost, i, j) tuples, sort, then pick greedily.


def greedy_assignment(cost_matrix):
    """
    Find an assignment greedily: always pick the globally cheapest available pair.
    Return (assignment, total_cost) where assignment[i] = j.
    """
    pass


if __name__ == "__main__":
    # Case where greedy is optimal
    cost1 = [
        [1.0, 5.0, 3.0],
        [5.0, 2.0, 5.0],
        [3.0, 5.0, 1.0],
    ]
    asgn, total = greedy_assignment(cost1)
    print(f"Greedy: {asgn}  cost={total:.2f}")
    print("PASS unique" if len(set(asgn)) == 3 else f"FAIL unique — {asgn}")

    # Case where greedy is suboptimal
    cost2 = [
        [1.0, 2.0],
        [2.0, 3.0],
    ]
    # Greedy picks (0->0, cost 1) then (1->1, cost 3) = 4
    # Optimal is (0->1, cost 2) + (1->0, cost 2) = 4 — actually same here
    _, greedy_cost = greedy_assignment(cost2)

    from scipy.optimize import linear_sum_assignment
    import numpy as np
    rows, cols = linear_sum_assignment(np.array(cost2))
    opt_cost = sum(cost2[r][c] for r, c in zip(rows, cols))
    print(f"Greedy cost={greedy_cost:.2f}  Optimal cost={opt_cost:.2f}")
    print("PASS greedy >= optimal" if greedy_cost >= opt_cost - 1e-9 else "FAIL greedy < optimal (bug)")
