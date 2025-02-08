# Own data structures.

- The functionality of a data structure can be represented as a collections of methods.
- By defining a class we can create a customized data structure that has its own set of methods.

# How not to implement a class.

- The following way of implementing a class does not work.

```python
class Stack:
  stack = []

  def push(self, x):
    self.stack.append(x)
  def top(self):
    return self.stack[-1]

  def pop(self):
    self.stack.pop()


a = Stack()
b = Stack()

a.push(1)
b.push(2)

print(a.top()) # 2 --> should be 1
```
