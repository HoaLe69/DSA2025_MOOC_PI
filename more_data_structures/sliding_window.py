"""
You are given a list of n numbers and a parameter k.
For each sliding window a sublist $k$ consecutive elements , from the left to right.
Find the smallest element in the sublist.
"""

import heapq


# the time complexity of this algorithm is O(n log n).
def find_minima(items, k):
    n = len(items)
    heap = []
    result = []

    for i in range(n):
        heapq.heappush(heap, (items[i], i))
        if heap[0][1] <= i - k:
            heapq.heappop(heap)
        if i >= k - 1:
            result.append(heap[0][0])
    return result


items = [1, 2, 3, 5, 4, 4, 1, 2]
k = 3

print(find_minima(items, k))
