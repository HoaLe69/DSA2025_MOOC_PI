# Introdution.
- The aim of the course Data Structures and Algorithms is to advance your programming skills.
- The course uses the Python language but the techniques taught on the course are applicable to other programming languages too.
- The course involes a lot of programming but some theoretical ideas and concepts are covered too.

# What is an algorithm ?
- An algorithm is a method for solving some computational problem
-  An algorithm implemented in some programming language can be executed on a computer.

# What is a data stucture ? 
- A data stucture is a way of storing data within program.
- The choice of data structures is an important part of designing an algoritgm.
- The data structures have a big effect on the efficiency of the algorithm.

# Implementing an algorithm.
- Any algorithm can be implemented with a few basic programming constructs. In Python, these basic constructs are:
    - variables
    - operators (+, = etc.)
    - conditionals (if)
    - loops (for, while)
    - lists
    - functions
    - classes
# Efficiency of algorithms.
[Efficiency of algorithms](https://tira.mooc.fi/spring-2025/chap01/)
- The same task can be solved by different algorithms, and there can be big differences in their efficiencies. 
- Often the goal is to find an efficient algorithm that solves the task quickly.
# Measuring efficiency.
- The efficiency of an algorithm can be studied with a test program that runs the algorithm for a given input and measures the execution time.
- It is often a good idea to write the test program so that it generates a random input of a given size.

# Analysis of algorithms.
## Time complexity of loop.
- The time complexity is often determined by the loops in the code.
**Single loop**
- If the algorithm contains a single loop that goes through all elements of the input, its time complexity is O(n).
**Nested loops**
- If an algorighm contains a loop inside a loop, each of which goes through all elements of the input, its time complexity O(n^2).
**Sequential code segments**
- If the algorithm consits of multiple code segments in sequence, the whole time complexity is the maximum of the segment time complexities.

