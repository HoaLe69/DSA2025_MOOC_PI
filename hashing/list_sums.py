"""
You are given a list containing n integers. Your task is to count,
How many sublists of the list have x as the sum of its elements.

Index   	0	1	2	3	4	5	6	7
Number      2	3	5	–3	4	4	6	2
Prefix sum	2	5	10	7	11	15	21	23

Fomula  to compute the sum of the random sublists: end - start - 1
Ex : sum of [2,4] , prefix_sum[4] - prefix_sum[2-1]  =  11 - 5 = 6
"""

numbers = [2, 3, 5, -3, 4, 4, 6, 2]
x = 5


# Solution1: On=(n^2)
def count_sublists(numbers, x):
    count = 0
    n = len(numbers)

    for i in range(n):
        sum = numbers[i]
        if numbers[i] == x:
            count += 1
        for j in range(i + 1, n):
            sum += numbers[j]
            if sum == x:
                count += 1
    return count


print("count_sublists1", count_sublists(numbers, x))


# Solution 2: O(n)
def count_sublists2(numbers, x):
    prefix_sum = 0
    n = len(numbers)
    count = {0: 1}
    result = 0

    for i in range(n):
        prefix_sum += numbers[i]

        if prefix_sum - x in count:
            result += count[prefix_sum - x]

        if prefix_sum not in count:
            count[prefix_sum] = 0
        count[prefix_sum] += 1

        print(count)

    return result


print("count_sublists2", count_sublists2(numbers, x))
