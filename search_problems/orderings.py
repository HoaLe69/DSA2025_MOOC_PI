"""
You are given a positive integer n.
Task: Count how many ways the elements 1,2,...n can be ordered so that no pair of adjacent
elements are consecutive numbers.

input : n = 4
output : 2
explain : [2,4,1,3] and [3,1,4,2]
"""
# using permutaions
# time complexity : O(n!n)

import itertools


def count_orders(n):
    items = range(1, n + 1)
    count = 0

    for order in itertools.permutations(items):
        print(order)
        if valid_order(order):
            count += 1

    return count


def valid_order(order):
    for i in range(len(order) - 1):
        if abs(order[i] - order[i + 1]) == 1:
            return False
    return True


print("count_orders", count_orders(4))
