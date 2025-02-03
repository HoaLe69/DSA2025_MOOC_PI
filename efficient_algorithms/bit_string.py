"""
You are given a bit string consisting of the characters 0 and 1.
How many ways can you select two positions in the bit string so that
left position contains the bit 0 and the right position contains the bit 1 ?

Consider the following situation:
bit : 01001011

Here there are 12 such pairs of position
"""

bits = "01001011"


# solution 1 : Its time complexity : O(n^2)
def count_ways(bits):
    count = 0
    n = len(bits)

    for i in range(n):
        for j in range(i + 1, n):
            if bits[i] == "0" and bits[j] == "1":
                count += 1
    return count


print(count_ways(bits))


# solution 1 : Its time complexity : O(n)
def count_ways2(bits):
    count = 0
    n = len(bits)
    zeros = 0
    for i in range(n):
        if bits[i] == "0":
            zeros += 1
        else:
            count += zeros
    return count


print(count_ways2(bits))
