# Seaching
numbers = [4,3,7,3,2]

print(3 in numbers) #True
print(8 in numbers) #False

print(numbers.index(3)) #1 return the index of the first occurrence of the element
print(numbers.count(3)) #2 return the number of occurrences of the element

"""
Adding an element

- append : adds an element to the end of the list. O(1)
- insert : adds an element to a given position on the list O(n)
"""

numbers.append(5)
print("after appended ", numbers) 

numbers.insert(1, 6)
print('after inserted ' , numbers)

"""
Removing an element

- pop method without parameter : removes the last element. O(1)
- pop with parameter : removes the element at the specified index. O(n)
"""

numbers.pop()
print("removed without parameter ", numbers)

numbers.pop(1)
print("removed with parameter ", numbers)

"""
References and copying
"""

a = [1,2,3,4]
#b = a #O(1) references
b = a.copy() #O(n)
a.append(5)

print(a)
print(b)

def double(numbers):
    result = numbers
    for i in range(len(result)):
        result[i] *=2
    return result

print("side effects of functions")
print(double(numbers)) #numbers = [8,6,14,6,4]
print(numbers)#numbers = [8,6,14,6,4]

"""
Slicing and concatenation
"""
print("Slicing and concatenation")
print(numbers[1 : 2]) # O(n)

first = [1,2,3]
second = [4,5,6]
print(first + second) # O(n) it copies the elements from the original list to the new list.
