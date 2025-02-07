[Sorting](https://tira.mooc.fi/spring-2025/chap05/)

# Sorting

- It is a classical algorithmic problem where the goal is to reorder the elements according to their value.
- There is efficient algorithms for sorting in O(nlogn) time.

# Sorting in python.

```Python
numbers = [4,3,2,1]
numbers.sort()
print(numbers) #[1,2,3,4]

# another ways
print(sorted(numbers)) #[1,2,3,4]
```

- There is a difference between the two ways of sorting a list is that the method `sort` modifies the list
  while the function `sorted` creates a new list and leaves the original list unmodified.

- Time complexity of both the method `sort` and `sorted` are O(nlogn).

# Own class.

- In python, objects of a class can be sorted if the class defines sufficient methods for
  comparing objects. For ex, it is enough to define the methods `__eq__` and `__lt__` which are
  called when the objects are compared with operators `==` and `<`.

```python

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __repr__(self):
        return str((self.x, self.y))


locations = []
locations.append(Location(1, 4))
locations.append(Location(4, 5))
locations.append(Location(2, 2))
locations.append(Location(1, 2))

locations.sort()

print(locations)
```

# How is sorting done ?

- A sorting algorithm is given a list of elements and the goal is the reorder them by their value.
  A typical algorithm can compare to each other and move elements to a difference position in the list.
- Simple sorting algorithm compare adjacent elements and swap them when needed. The time complexity is O(n^2).One
  such algorithm is `Insertion sort` that processes the elements from left to right and moves each element to its correct position among the already processed elements.
- There are also efficient algorithms with time complexity O(n log n). One such algorithm is `merge sort` that start by sorting the first half and the second half of the list separately using recursion, and the merges the two halfs
