# Everything is object — Alx Low Level Programming
0x09. Python - Everything is object

## Introduction
Python is an object-oriented programming language that emphasizes the concept of objects and classes. Understanding the fundamentals of OOP is crucial for effective programming.

## What is an Object?
An object in Python is a tangible entity that encapsulates data (attributes) and behavior (methods). It's an instance of a class and can interact with other objects.

## Class vs. Object or Instance
A class is a blueprint or template that defines the structure and behavior of objects. An object, also known as an instance, is a specific realization of that class.

## Mutable vs. Immutable Objects
- Mutable: Objects that can be changed after creation, like lists or dictionaries.
- Immutable: Objects that cannot be changed after creation, like strings or tuples.
## Reference, Assignment, and Alias
- **Reference**: A variable refers to an object in memory.
- **Assignment**: Linking a variable name to an object.
- **Alias**: Two or more variables referring to the same object.
## Identical Variables and Object Linkage
**Identical Variables:** Use the `is` operator to check if two variables point to the same object. \
**Linked to the Same Object:** Compare variable identifiers using the id() function.
## Display Variable Identifier (Memory Address)
To display the memory address of a variable in CPython:
```python
variable = "example"
print(id(variable))
```

## Mutable and Immutable Types
- Built-in Mutable Types: Lists, dictionaries, sets.
- Built-in Immutable Types: Strings, tuples, frozensets.

## Variable Passing to Functions
Python passes variables to functions by object reference. Changes made to mutable objects within functions reflect outside the function scope.

## Conclusion
Understanding the concepts of objects, classes, mutability, references, and variable handling in Python is essential for efficient and effective programming. Embrace OOP principles to build robust and scalable applications.
## Contact Me
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
