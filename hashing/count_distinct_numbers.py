"""
You are given a list of numbers. How many distinct numbers does it contain ?

Ex : [3,1,2,1,5,2,2,3] the desired answer is 4 (1,2,3,5)
"""

numbers = [3, 1, 2, 1, 5, 2, 2, 3]


# Solution 1 : O(n^2)
def count_distinct(numbers):
    seen = []
    for x in numbers:
        if x not in seen:
            seen.append(x)
    return len(seen)


print(count_distinct(numbers))

# Solution 2 : using set


def count_distinct2(numbers):
    seen = set()

    for x in numbers:
        if x not in seen:
            seen.add(x)
    return len(seen)


# Solution 3 : shorten
def count_distinct3(numbers):
    return len(set(numbers))


print(count_distinct3(numbers))
