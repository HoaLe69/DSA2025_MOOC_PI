# normal way
def count_even(numbers):
    result = 0
    for x in numbers:
        if x %  2 == 0:
            result += 1;
    return result
# shorten way
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)
# each True is counted as the number 1 and each False as the number 0.

print(count_even([1, 2, 3])) # 1
print(count_even([2, 2, 2, 2, 2])) # 5
print(count_even([5, 4, 1, 7, 9, 6])) # 2

print(count_even2([1, 2, 3])) # 1
print(count_even2([2, 2, 2, 2, 2])) # 5
print(count_even2([5, 4, 1, 7, 9, 6])) # 2

# efficiency of the algorithms
# find the largest difference between any two numbers.
# For example
#  when the list is [3, 2, 6, 5, 8, 5],
#  the desired answer is 6, because the largest difference is between the numbers 2 and 8.
def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result , abs(x - y))
    return result

def max_diff2(numbers):
    results = sorted(numbers)
    return results[-1] - results[0]

def max_diff3(numbers):
    return max(numbers) - min(numbers)

print("max_diff" ,max_diff([1, 2, 3])) # 2
print("max_diff" ,max_diff([3, 2, 6, 5, 8, 5])) # 6
print("max_diff2" , max_diff2([3, 2, 6, 5, 8, 5]))
print("max_diff3", max_diff3([3, 2, 6, 5, 8, 5]))
