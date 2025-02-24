# Deque.

- It is a list structure that supports efficient addition and removal of elements both at the beginning and at the end of the list.

- It look like similar Array<list>, but more efficiently when you adding and removing an element at the beginning of the list.
- You can using the index to access the element.
  Here is a following methods:
  `append` : add an element to the end of the list.
  `pop`: remove the element at the end of the list.
  `appendleft` : add an element to the beginning of the list.
  `popleft` : remove the element at the beginning of the list.
- In addition to the familiar methods `append` and `pop`, we now have the methods `appendleft` and `popleft` the operate at the beginning of the list. The time complexity of all four methods is O(1).

# Stack and queue

- _Stack_ is a data structure that supports adding and removing elements at the end of the list.
- _Queue_ is a data structure that supports adding elements to end of list and removing elements from the beginning of the list.

- We can use `deque` to implement both stack and queue.

# Heap

- It is a data structure where the smallest or the largest element can be found and removed efficiently.
- Additions to a heap are unrestricted
  In python, a list ca be used as a heap with the following functions in the module `heapq`.
  `heappush` : add an element to the heap.
  `heappop` : remove and return the smallest element of the heap.
- The time complexity of both functions is O(log n).
- The smallest in the list is always at the beginning of the list and can be accessed in O(1) time.
