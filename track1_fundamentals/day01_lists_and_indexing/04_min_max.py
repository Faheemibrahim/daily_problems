# Problem: Given a list of numbers, find the minimum and maximum without using min() or max().
# Concept: Manual iteration over a flat list to track two running extremes simultaneously.
# You are done when:
#   [ ] You loop through the list exactly once
#   [ ] You track both the minimum and maximum in the same pass
#   [ ] You do not call min(), max(), or sorted()
#   [ ] All test cases print PASS
# Hint: Initialize both trackers to the first element before the loop begins.


def find_min_max(numbers):
    """
    Return (minimum, maximum) from a list of numbers.
    Do not use min() or max().
    """
    x = numbers[0]
    y = numbers[0]

    min = None
    max = None

    for i in numbers:
        if i > x:
            x = i

        elif i < y:
            y = i
            

    return y, x



if __name__ == "__main__":
    nums = [4, 7, 2, 9, 1, 5, 8, 3, 6]
    result = find_min_max(nums)
    expected = (1, 9)
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    nums2 = [42.0]
    result2 = find_min_max(nums2)
    expected2 = (42.0, 42.0)
    print("PASS" if result2 == expected2 else f"FAIL — got {result2}, expected {expected2}")

    nums3 = [-3, -1, -7, -2]
    result3 = find_min_max(nums3)
    expected3 = (-7, -1)
    print("PASS" if result3 == expected3 else f"FAIL — got {result3}, expected {expected3}")
