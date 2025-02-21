"""
You are given alist of n integers.
Your task is to find how long is the longest increasing subsequences.
How many numbers can we collect from the list going from left to right
so that each number is larger than the previous numbers (which mean it allowed to skip numbers)

Ex : [4,1,5,6,3,4,3,8] ---> desired answer is [1,3,4,8] and its length is 4
"""

numbers = [7, 7, 7, 7, 7, 7, 7]


def longest_length_subsequecens(numbers):
    subs = []
    n = len(numbers)
    subs.append([numbers[0]])
    ans = [1] * n
    for i in range(1, n):
        curr_len = 0
        for sub in subs:
            if numbers[i] - sub[len(sub) - 1] > 0:
                subs.append(sub + [numbers[i]])
            curr_len = max(len(sub), curr_len)
        subs.append([numbers[i]])

        ans[i] = max(curr_len, ans[i])
    return ans[n - 1]


def longest_length_subsequecens2(numbers):
    n = len(numbers)
    ans = [1] * n
    for i in range(n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                ans[i] = max(ans[i], ans[j] + 1)
    return ans[n - 1]


print(longest_length_subsequecens2(numbers))
