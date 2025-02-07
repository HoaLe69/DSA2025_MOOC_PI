"""
You are given a list of numbers, and your task is to compute the mode,
which is the most frequent number on the list.
If the mode is not unique, you can choose any of the possible choices
for the most frequent number.

Ex : [1,2,3,2,2,3,2,2] -> The desired answer is 2.

"""

numbers = [1, 2, 3, 2, 2, 3, 2, 2]


# Case 1 : O(n)
def find_mode(numbers):
    count = {}
    mode = numbers[0]
    for x in numbers:
        if x not in count:
            count[x] = 1
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode


# Case 2: O(n)
def find_mode2(numbers):
    count = {}
    mode = (0, 0)

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1
        mode = max(mode, (count[x], x))
    return mode[1]


print(find_mode2(numbers))
