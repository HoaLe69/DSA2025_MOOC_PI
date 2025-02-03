"""
Your are given a list containing n integers. Your task is to count
how many ways one can split the list into two parts so that both parts
have the same total sum of elements.

Consider the following example list:
number = [1, -1,1, -1,1,-1,1,-1]

Output : 3
We can split the list between positions 1 and 2, 3 and 4, 5 and 6.
"""

# from efficient_algorithms.bit_string import count_ways2

numbers = [1, -1, 1, -1, 1, -1, 1, -1]


# Solutions 1 : Its time complexity : O(n^2)
def count_splits(numbers):
    count = 0
    n = len(numbers)
    left_sum = 0
    for i in range(n - 1):
        left_sum += numbers[i]
        right_sum = sum(numbers[i + 1 :])
        if left_sum == right_sum:
            count += 1
    return count


print(count_splits(numbers))


def count_splits2(numbers):
    count = 0
    n = len(numbers)
    left_sum = 0
    total_sum = sum(numbers)
    for i in range(n - 1):
        left_sum += numbers[i]
        right_sum = total_sum - left_sum

        if left_sum == right_sum:
            count += 1
    return count


print(count_splits2(numbers))
