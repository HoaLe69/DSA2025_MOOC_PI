[List](https://tira.mooc.fi/spring-2025/chap02/)
# List in memory.
- The memory of a computer consists of a sequence of memory locations capable of storing data.
- Each memory locations has an address that can be used for access.
- The list occupies more memory than is needed for its current elements. The reason for the extra memory is to prepare for possible addition of new elements to the list. Thus the list has two sizes.

# List operations.
1. Indexing
2. List Size
3. Searching
4. Adding an element
5. Removing an element
- knowing the time complexities of the list operations is important for algorithm design, because they determine which operations can be used as components of an efficient algorithm. Most list operations have one of the following time complexities:
    1. O(1) : the operations is always efficient independent of the size of the list.
    2. O(n) : the efficiency depends on the size of the list and the operations be slow for large lists.

# References and copying.
## Side effects of functions.
- When a function is given a data structure as a parameter, only reference is copied.
- The the function can cause side effects, if it changes the content of the data structure.
## Slicing and concatenation.
