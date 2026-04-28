# Problem: Write sum_tree(node) that sums all values in a binary tree using recursion.
# Concept: Tree recursion — the result for a node is: node.value + sum_tree(left) + sum_tree(right).
#          Base case: None node contributes 0. This exact pattern applies to KD-tree operations.
# You are done when:
#   [ ] Returns 0 for an empty tree (None root)
#   [ ] Returns the single value for a leaf node
#   [ ] Correctly sums multi-level trees
#   [ ] All test cases print PASS
# Hint: if node is None: return 0; return node.value + sum_tree(node.left) + sum_tree(node.right)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right


def sum_tree(node):
    """Return the sum of all values in the binary tree rooted at node."""
    pass


if __name__ == "__main__":
    print("PASS empty" if sum_tree(None) == 0 else "FAIL empty")

    leaf = TreeNode(5)
    print("PASS leaf" if sum_tree(leaf) == 5 else f"FAIL leaf — {sum_tree(leaf)}")

    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("PASS tree" if sum_tree(tree) == 15 else f"FAIL tree — {sum_tree(tree)}")
