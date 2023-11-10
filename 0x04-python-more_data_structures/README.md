# Data Structures: Set, Dictionary — Alx Higher Level Programming
0x04. Python - More Data Structures: Set, Dictionary

## Overview
In this project, we will explore two essential data structures: **Sets** and **Dictionaries** as well as lambda functions, and the map, reduce, and filter functions.

## Sets
`Sets` in Python are unordered collections of unique elements. They are defined using curly braces **{}**. \
Here's a basic example:
```python
my_set = {1, 2, 3, 4, 5}
```
## Common Set Methods
```python
# Adding Elements:
my_set.add(6)
# Removing Elements:
my_set.remove(3)
# Checking Membership:
if 2 in my_set:
    print("2 is in the set.")
```
## Sets vs. Lists
Use sets when you need to store unique elements, and the order doesn't matter. Lists, on the other hand, allow duplicate elements and maintain order.

## Iterating Over a Set
Iterating Over a Set
```python
for element in my_set:
    print(element)
```

## Dictionaries
`Dictionaries` are unordered collections of key-value pairs. They are defined using curly braces **{ }** with key-value pairs separated by colons : \
Example:
```python
my_dict = {'name': 'El_Ouardy', 'age': 25, 'country': 'Morocco'}
```
## When to Use Dictionaries
Use dictionaries when you have data that is best represented by a key-value mapping, and you need to look up values based on keys.

## Keys in a Dictionary
In the dictionary my_dict, 'name', 'age', and 'country' are keys.

## Iterating Over a Dictionary
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
## Lambda Functions
A lambda function is a concise way to create ***Anonymous Functions***. \
Example:
```python
square = lambda x: x**2
```
## Map, Reduce, and Filter Functions
### Map:
Applies a function to all items in an input list and returns an iterator.
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
```
### Filter:
Filters out elements from a list based on a condition.
```python
even_numbers = filter(lambda x: x % 2 == 0, numbers)
```
### Reduce:
Applies a rolling computation to sequential pairs of values in a list. It combines elements of a list using a specified function, resulting in a single accumulated value.
```python
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
```

## Conclusion
Understanding the use cases and functionalities of sets, dictionaries, lambda functions, and the map, reduce, and filter functions enhances the ability to work with data in Python. \
Choose sets for unique, unordered collections, dictionaries for key-value mappings, and lambda functions for concise, one-line functions. The map, reduce, and filter functions provide powerful tools for manipulating data in a functional programming style.

## Contact Me
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
