# Deque
import collections
import heapq

items = collections.deque()

items.append(1)
items.append(2)
items.append(3)
items.append(4)
items.append(5)

items.appendleft(10)
items.appendleft(11)

print("before removed", items)
items.popleft()
items.pop()

print("after removed", items)

print(items)

print("last element", items[-1])

# stack and queue


class Stack:
    def __init__(self):
        self.stack = collections.deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __repr__(self) -> str:
        return str(self.stack)


class Queue:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        self.queue.append(x)

    def top(self):
        return self.queue[0]

    def pop(self):
        self.queue.popleft()


stack = Stack()
queue = Queue()

# stack.push(10)
# stack.push(20)
#
# queue.push(10)
# queue.push(20)
#
# top_queue = queue.top()
# top = stack.top()
#
# print("top", top)
#
# print("top_queue", top_queue)
#
# print(stack)
#### HEAD

heap_list = []
heapq.heappush(heap_list, 4)
heapq.heappush(heap_list, 3)
heapq.heappush(heap_list, 2)
heapq.heappush(heap_list, 1)

print(heap_list[0])
heapq.heappop(heap_list)

print(heap_list[1])
