"""
You have an unlimited number coins with values given as a list.
Each value is a positive integer and the smallest value is 1. The goal is to choose a set of coins
summing up to x.

1. Find the optimal solution : How many coins at least is needed to achieve the sum x ?
2. Construct an optimal solution: Give an example of a minimal set of coins summing up x ?
3. Count solutions : How many different ways there are to achieve the sum x ?

Ex : [1,2,5] and x = 13
1. The smallest number of coins needed is 4.
2. A minimal solution is to choose the coins [1,2,5,5]
3. There are 634 ways to choose the coins (including[1,2,5,5] , [2,2,2,2,5] and [1,1,1,5,5])
"""

import math


def min_coins(x, coins):
    result = {}

    result[0] = 0
    for s in range(1, x + 1):
        result[s] = s
        for c in coins:
            if s - c >= 0:
                result[s] = min(result[s], result[s - c] + 1)
    return result


def min_coins2(x, coins):
    f = [math.inf] * (x + 1)
    f[0] = 0

    for coin in coins:
        for j in range(coin, x + 1):
            f[j] = min(f[j], f[j - coin] + 1)

    print(f)


# Get a set of coins corresponding to the minimal solution.


def min_coins3(x, coins):
    result = {}

    result[0] = []

    for s in range(1, x + 1):
        result[s] = [1] * s
        for c in coins:
            if s - c >= 0:
                new_result = result[s - c] + [c]
                if len(new_result) < len(result[s]):
                    result[s] = new_result
    print(result)
    return sorted(result[x])


# Counting the number of all solutions.
def min_coins4(x, coins):
    result = {}

    result[0] = 1

    for s in range(1, x + 1):
        result[s] = 0

        for coin in coins:
            if s - coin >= 0:
                result[s] += result[s - coin]
    return result[x]


print(min_coins2(13, [1, 2, 5]))  # 4
print(min_coins3(13, [1, 2, 5]))  # 4
# print(min_coins(13, [1, 4, 5]))  # 3
print(min_coins2(3, [2]))
print("Num of solution", min_coins4(13, [1, 2, 5]))
