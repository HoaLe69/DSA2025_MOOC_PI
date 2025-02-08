"""
Implement a class Mode with following methods:
- add(x) : add the number x on the list.
- mode() : return the mode of the list, i.e, the mose frequent number on the list.

The time complexity of each method should be O(1)
"""


class Mode:
    def __init__(self):
        self.count = {}
        self.status = (0, 0)

    def add(self, x):
        if x not in self.count:
            self.count[x] = 0
        self.count[x] += 1
        self.status = max(self.status, (self.count[x], x))

    def mode(self):
        return self.status[1]


mode = Mode()

mode.add(2)
mode.add(2)
mode.add(2)
mode.add(2)
mode.add(1)
print(mode.mode())
