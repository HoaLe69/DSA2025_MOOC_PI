"""
You are given a list that contains the numbers 1,2,...,n in some order.
Your task is to collect all the numbers in order from smallest to largest
so that each round you go through the list from left to right. How many rounds
do you needs ?

For example, the list [3,6,1,7,5,2,4,8] requires 4 rounds. The first round collects the numbers
1 and 2. The second round the numbers 3 and 4, the third round the number 5, and the fourth round the numbers
6 , 7 and 8.

1 -> 1,2,3,6,7,5,4,8
2 -> 1,2,3,4,6,7,5,8
3 -> 1,2,3,4,5,6,7,8.
4 -> 1,2,3,4,5,6,7,8.
"""

# A useful observation is that a new round starts whenever the number to be collected
# next is to the left of the most recently collected number.

numbers = [3, 6, 1, 7, 5, 2, 4, 8]


# Solution 1 : O(n^2)
def count_rounds(numbers):
    rounds = 1
    n = len(numbers)
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1
    return rounds


print("rounds", count_rounds(numbers))


# Solution 2 : O(n)
def count_rounds2(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
    rounds = 1

    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds


count_rounds2(numbers)
