"""
You are given a list of numbers. What is the smallest difference between two element ?
Ex : [4,1,7,3,9] -> the desired answer is 1,

because the smallest difference is between the numbers 3 and 4.
"""

# The smallest difference is always between two adjacent elements.
numbers = [4, 1, 7, 3, 9]


# Time complexity : O(n log n).
def min_diff(numbers):
    sorted_numbers = sorted(numbers)

    n = len(sorted_numbers)
    result = sorted_numbers[1] - sorted_numbers[0]

    for i in range(2, n):
        result = min(result, sorted_numbers[i] - sorted_numbers[i - 1])

    return result


print(min_diff(numbers))
