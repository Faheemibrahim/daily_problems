# Problem: Given a list of 20 index numbers with duplicates, use a set to track visited
#          indices: add to it and check membership as you would in a search algorithm.
# Concept: Sets as O(1) membership trackers — the visited pattern from BFS/clustering.
# You are done when:
#   [ ] You add indices to the set as you "visit" them
#   [ ] You check membership with `in` before processing
#   [ ] The set contains only unique indices at the end
#   [ ] All test cases print PASS
# Hint: set.add(x) never creates duplicates; `x in my_set` is O(1).


def simulate_visited(indices):
    """
    Process each index in order. Skip it if already visited.
    Return (visited_set, processing_order) where processing_order is the
    list of indices in the order they were first seen.
    """
    pass


if __name__ == "__main__":
    indices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
    visited, order = simulate_visited(indices)

    print("PASS unique count" if len(visited) == 9 else f"FAIL unique count — got {len(visited)}")
    print("PASS order first" if order[0] == 3 else f"FAIL order first — got {order[0]}")
    print("PASS no dupes in order" if len(order) == len(set(order)) else "FAIL dupes in order")
