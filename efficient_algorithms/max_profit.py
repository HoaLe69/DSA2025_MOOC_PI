import random

"""
Stock trading

Task : You are given the price of a stock for n days.
Your task is figure out the highest profit you could 
have made if you had bought the stock on one day and sold 
it on another day.

Consider the following situation:
prices = [3,7,5,1,4,6,2,3]

output : 5 , achieved by buying on day 3 and seling on day 5
"""


# solution 1 : O(n^2)
def best_profit(prices):
    result = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            result = max(prices[j] - prices[i], result)
    return result


prices = [3, 7, 5, 1, 4, 6, 2, 3]

print("Max profit", best_profit(prices))


# solution 2 : O(n^2)
def best_profit2(prices):
    result = 0
    n = len(prices)
    for i in range(n):
        min_price = min(prices[0 : i + 1])
        result = max(result, prices[i] - min_price)
    return result


print("Max profit 2 -------->", best_profit2(prices))


# solution 3 : O(n)
def best_profit3(prices):
    result = 0
    n = len(prices)
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        result = max(result, prices[i] - min_price)

    return result


print("Max profit 3 -------->", best_profit3(prices))

while True:
    n = 1000
    prices = [random.randint(1, 10) for _ in range(n)]

    result_brute = best_profit(prices)
    result_fast = best_profit3(prices)

    print(prices, result_brute, result_fast)

    if result_brute != result_fast:
        print("Error")
        break
