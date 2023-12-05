# Input/Output — Alx Higher Level Programming
0x0B. Python - Input/Output

## Introduction
Python offers robust functionalities for handling Input/Output operations, enabling seamless interaction with files and data serialization formats like JSON.

## Opening a File
To open a file, use the open() function:
```python
file = open('filename.txt', 'r')  # 'r' for reading, 'w' for writing, 'a' for appending
```
## Writing Text in a File
Writing text into a file involves using the file object's write() method:
```python
with open('filename.txt', 'w') as file:
    file.write('Hello, World!')
```
## Reading Full Content of a File
To read the entire content of a file:
```python
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
```
## Reading a File Line by Line
Reading a file line by line:
```python
with open('filename.txt', 'r') as file:
    for line in file:
        print(line)
```
## Moving the Cursor in a File
You can move the cursor within a file using seek():
```python
with open('filename.txt', 'r') as file:
    file.seek(5)  # Moves the cursor to the 5th byte in the file
    content = file.read()
    print(content)
```
## Ensuring File Closure
Python automatically closes files after usage within a with statement. However, for explicit closure, use:
```python
file = open('filename.txt', 'r')
# File operations...
file.close()
```
## Using the with Statement
The ``with`` statement is a context manager ensuring proper resource handling, automatically closing files after usage:
```python
with open('filename.txt', 'r') as file:
    # File operations...
```
## JSON - JavaScript Object Notation
``JSON`` is a lightweight data interchange format, human-readable, and easy for machines to parse and generate.

## Serialization and Deserialization
Serialization refers to converting Python objects into a JSON string. Deserialization is the opposite, turning JSON strings into Python objects.

## Converting Python Data Structure to JSON
Using the json module to convert a Python data structure into JSON:
```python
import json

data = {'name': 'John', 'age': 30}
json_str = json.dumps(data)
```
## Converting JSON String to Python Data Structure
Converting a JSON string into a Python data structure:
```python
json_str = '{"name": "John", "age": 30}'
data = json.loads(json_str)
```

## Conclusion
Python's I/O functionalities empower developers to interact with files efficiently while JSON simplifies data interchange between different platforms or systems. Mastering these basics is pivotal for effective software development and data handling.

## Contact Me
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
