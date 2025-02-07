# Hashing

- It is a technique that is frequently used in implementing efficient algorithms.
- In Python, the data structures `set` and `dict` are based on hashing.

## Set

1. `add` : adds an element to the set.
2. `in` : finds if a given element is in the set.
3. `remove` : removes an element from the set.

Time Complexity : O(1).

```Python
numbers = set() # numbers = set([1,2,3])
numbers.add(4)

print(numbers()) #{1, 2,3, 4}

# in
print(3 in numbers) # True
numbers.remove(4)
print(numbers) #{1,2,3}
```

## List vs. Set.

- There are significant differences in their efficiency and other properties.

**Efficiency**

- Adding an element to a list is efficient, but finding an element and removing it can be slow.
  Adding(`append`/`add`) : List O(1) vs. Set O(1)
  Finding : List O(n) vs. Set O(1)
  Removing : List O(n) vs. Set O(1)
  **Indexing**
- In list, elements can be accessed using an index.

```Python
numbers  = [1,2,3]
print(numbers[1]) #2
```

- A set does not support indexing.

** Repeated elements**

- In a list, an element can occur multiple times.
- A set contains an element at most one.

## Dictionary.

- It based on hashing and stores key-value pairs.
- Accessing and removing data using a key takes O(1) time.

## Using a dictionary.

- Has an element occur.
- Counting occurrences.
- Position of occurrence.
