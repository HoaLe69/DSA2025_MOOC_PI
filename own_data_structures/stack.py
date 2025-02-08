"""
Implement a class Stack that implements the stack data structure.
The class should have the following methods.

- push(x) : add the element x to the top of the stack.
- top() : access the element at the top of the stack.
- pop() : remove the element at the top of the stack.

The time complexity of each methods should be O(1)
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def top(self):
        if len(self.stack) == 0:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("pop from empty stack")
        self.stack.pop()

    def __repr__(self) -> str:
        return str(self.stack)

    def __len__(self):
        return len(self.stack)


s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.top())

s.pop()

print(s.top())

print(s.stack)
