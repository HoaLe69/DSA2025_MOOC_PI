"""
Task : Count the number of balanced parenthesis sequences of length n.

input : n = 6
ouput : 5
explain : ((())), (())(), ()(()), (()()) and ()()().
"""

# time complexity : O(2^n*n)
import itertools


def count_sequeneces(n):
    count = 0
    for sequence in itertools.product("()", repeat=n):
        print(sequence, "\n")
        if valid_sequence(sequence):
            count += 1
    return count


def valid_sequence(sequence):
    depth = 0

    for bracked in sequence:
        if bracked == "(":
            depth += 1
        if bracked == ")":
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


print("count_sequeneces", count_sequeneces(6))
