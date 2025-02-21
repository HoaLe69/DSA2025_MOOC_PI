[search problems](https://tira.mooc.fi/spring-2025/chap09/)

# Search problems.

- Many algorithmic problems can be thought of as search problems.
- A straightforward way of solving a search problem is a brute force search that goes through all solutions one by one.This method always produces the correct answer, but the search may take too much time.

## Iterating solutions.

- A brute force algorithm for a search problem iterates through all possible solutions one by one.
- A brute force algorithm can be implemented to construct all solutions by combining given elements in certain way.
- Here is three common types of cases
  **Sequences**
- The input consists of n elements and we want all sequences of m elements. There are n^m such sequences.
  Ex: [1,2,3] and m = 2 the sequences are [1,1] , [1,2] , [1,3], [2,1], [2,2], [2,3], [3,1],[3,2] and [3,3]

- In python, sequences can be formed using the function `product` in the module `itertools`.

```python
import itertools


for repetition in itertools.product([1,2,3], repeat=2):
  print(repetition)

# output look like this
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)
```

**Permutations**

- The input consists of n elements and we want all permutations or orderings of the elements. The number of permutations is n!.

Ex : [1,2,3] the permutations are [1,2,3] , [1,3,2], [2,1,3], [2,3,1], [3,1,2] , [3,2,1]

- In python, the permutations of a list can be formed using the function `permutations` in the module `itertools` as follows

```python
import itertools

for permutation in itertools.permutations([1,2,3])
  print(permutation)

# Output look like this.
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
```

**Combinations**

- The input consists of n elements and we want all combinations or subsets consisting of m elements.

Ex: [1,2,3,4] and m = 2. The combinations are [1,2] ,[1,3], [1,4], [2,3], [2,4] and [3,4]

- In python, combinations can be formed using the function `combinations` in the module `itertools` as follows:

```python
import itertools

for combination in itertools.combinations([1,2,3,4] , 2):
  print(combination)

# Output look like this
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
```
