# Problem: Write flatten(nested_list) recursively to handle any depth.
#          e.g. [1, [2, [3, [4]]]] becomes [1, 2, 3, 4]
# Concept: Recursive tree traversal — each element is either a leaf (add to result)
#          or a subtree (recurse into it). The same pattern appears in JSON parsing,
#          AST traversal, and file system walking.
# You are done when:
#   [ ] Handles arbitrary nesting depth
#   [ ] Non-list elements are included as-is
#   [ ] An empty nested list produces an empty result
#   [ ] All test cases print PASS
# Hint: for item in lst: if isinstance(item, list): result += flatten(item) else: result.append(item)


def flatten(nested_list):
    """Return a flat list with all elements from any nesting depth."""
    pass


if __name__ == "__main__":
    print("PASS 1 level" if flatten([1, 2, 3]) == [1, 2, 3] else f"FAIL 1 level — {flatten([1,2,3])}")
    print("PASS 2 levels" if flatten([1, [2, 3], 4]) == [1, 2, 3, 4] else f"FAIL 2 — {flatten([1,[2,3],4])}")
    print("PASS deep" if flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4] else f"FAIL deep")
    print("PASS mixed" if flatten([[1, 2], [3, [4, 5]]]) == [1, 2, 3, 4, 5] else "FAIL mixed")
    print("PASS empty" if flatten([]) == [] else "FAIL empty")
