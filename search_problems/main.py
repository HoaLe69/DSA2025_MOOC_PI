# Sequences
import itertools

for repetition in itertools.product([1, 2, 3], repeat=2):
    print(repetition)

# permutations

for permutation in itertools.permutations([1, 2, 3]):
    print(permutation)

# Combinations

for combination in itertools.combinations([1, 2, 3, 4], 2):
    print(combination)
