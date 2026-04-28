# Problem: Demonstrate with a timing test that checking membership in a set is
#          faster than checking in a list, using 100 000 elements.
# Concept: O(1) average case for sets vs O(n) for lists — critical for visited checks
#          in clustering where you may check membership millions of times.
# You are done when:
#   [ ] You create both a list and a set of 100 000 elements
#   [ ] You time many membership checks against each
#   [ ] You print the ratio showing set is significantly faster
#   [ ] The test auto-confirms set is faster
# Hint: import time; t = time.time() before the loop, time.time() - t after.

import time


def timing_test(n=100_000, checks=10_000):
    """
    Return (list_time, set_time) in seconds for `checks` membership tests
    against a collection of size n.
    """
    data = list(range(n))
    data_set = set(data)
    targets = [i * (n // checks) for i in range(checks)]

    start = time.time()
    for t in targets:
        _ = t in data
    list_time = time.time() - start

    start = time.time()
    for t in targets:
        _ = t in data_set
    set_time = time.time() - start

    return list_time, set_time


if __name__ == "__main__":
    list_t, set_t = timing_test()
    ratio = list_t / set_t if set_t > 0 else float("inf")
    print(f"List time: {list_t:.4f}s  |  Set time: {set_t:.6f}s  |  Ratio: {ratio:.1f}x")
    print("PASS set is faster" if set_t < list_t else "FAIL — set was not faster (unexpected)")
