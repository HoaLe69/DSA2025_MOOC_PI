"""
Implement a class SuperStack with the following methods:
- push(x) : add the element x to the top of the stack.
- push_many(k,x) : add k copies of the element x to the top of the stack.
- top() : access the element at the  top of the stack.
- pop() : remove the element at the top of the stack.

The time complexity of each method should be O(1)
"""


class SuperStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((1, x))

    def push_many(self, k, x):
        self.stack.append((k, x))

    def top(self):
        return self.stack[-1][1]

    def pop(self):
        last = self.stack[-1]
        if last[0] == 1:
            self.stack.pop()
        else:
            self.stack[-1] = (last[0] - 1, last[1])


s = SuperStack()

s.push(1)
s.push(2)

print(s.stack[-1])
