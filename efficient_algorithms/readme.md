[Efficient algorithm](https://tira.mooc.fi/spring-2025/chap03/)

# Outline of an efficient algorithm.

- A typical efficient algorithm might be structured something like this:

```python
# define variables
for ...
    # efficient code
# return answer
```

- An efficient algorithm typical has single for-loop that goes through the input from left to right. The code inside the loop is efficient so that each round in loop takes O(1).
- A loop in an efficient algorithm may contain the following:
  - updates of variable values using other variables or individual elements of the input.
  - arithmetic expressions related to variable updates.
  - if-commands that effect the variable updates.
- But the loop may not contain: - other loops that go through the input. - slow operations that process the input(ex : `count` or the `slice` operation[:]). - slow function calls( ex : `sum`, `min` , `max`).
  **A major challenge** in the design of many algorithms is to figure out how to implement the algorithm so that the loop contains only efficent code.
