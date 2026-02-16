# Data Structures: Lists, Tuples — Alx Higher Level Programming

0x03. Python - Data Structures: Lists, Tuples

## Overview

Python offers a plethora of tools and structures, making it versatile for handling various data types and structures. In this project, we'll explore two essential data structures: `Lists` and `Tuples`.

## What are Lists and How to Use Them

`Lists` in Python are ordered collections of elements enclosed in square brackets []. They can contain various data types and are changeable (Mutable), meaning you can add, remove, or modify elements after creation.

Example:

```python
my_list = [1, 'apple', 3.14, True]
print(my_list)  # Output: [1, 'apple', 3.14, True]
```

## Differences and Similarities Between Strings and Lists

Strings and lists are both sequences in Python. Strings are collections of characters and are immutable (cannot be changed after creation), whereas lists are mutable (can be modified). Both are indexed and sliced similarly.

## Common List Methods and How to Use Them

Lists have various useful methods such as `append()`,` remove()`, and `extend()` to add, delete, or modify elements. For instance:

```python
fruits = ['apple', 'banana', 'orange']
fruits.append('grapes')
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grapes']
```

## Using Lists as Stacks and Queues

Lists can be used as `stacks` (Last-In, First-Out) and `queues` (First-In, First-Out) by using methods like **append()**, **pop()**, and **popleft()** from the collections module.

## List Comprehensions

List comprehensions provide a concise way to create lists. They are an elegant and efficient way to create new lists by iterating over an existing list.

Example:

```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## What are Tuples and How to Use Them

`Tuples` are ordered collections enclosed in parentheses (). They are **immutable**, making them a fixed collection of elements.

Example:

```python
my_tuple = (1, 'apple', 3.14, True)
print(my_tuple)  # Output: (1, 'apple', 3.14, True)
```

## When to Use Tuples versus Lists

Use tuples for fixed data that should not be changed, and lists for mutable collections.

## Sequence, Tuple Packing, and Sequence Unpacking

Both **lists** and **tuples** are sequences in Python, allowing ordered indexing and slicing. `Tuple packing` is creating a tuple without parentheses, and `sequence unpacking` assigns elements to multiple variables at once.

Example:

```python
coordinates = 3, 5  # Tuple packing
x, y = coordinates  # Sequence unpacking
print(x, y)  # Output: 3 5
```

## The del Statement and How to Use It

The `del` statement removes elements or slices from a list or entire variables from the namespace.

Example:

```python
my_list = [1, 2, 3, 4, 5]
del my_list[2]
print(my_list)  # Output: [1, 2, 4, 5]
```

## Conclusion

In the realm of Python programming, mastering Lists and Tuples offers you a wide array of tools and techniques. Lists provide flexibility, enabling modifications, while Tuples offer stability with their immutability.

## Contact Me

**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** contact@wadi3.codes
