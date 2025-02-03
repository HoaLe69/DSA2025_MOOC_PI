"""
You are given a list containing n integers.
How many ways can we choose a sublist contains exactly two distinct integers?

For example, the list [1,2,3,3,2,2,4,2] has 14 such sublists.
"""

numbers = [1, 2, 3, 3, 2, 2, 4, 2]


# a points to the nearest preceding position that contains a different value than the one in the position i.
# b points to the nearest preceding position whose value differs from both of the values at the positions i and a.
# the result of each round computed by a - b formula.


# Best solution : Its time complexity : O(n).
def count_lists(numbers):
    count = 0
    a = b = -1
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] != numbers[i - 1]:
            if numbers[i] != numbers[a]:
                b = a
            a = i - 1
        # default : it will be 0
        count += a - b
    return count


print(count_lists(numbers))
