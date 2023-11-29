# Test-driven development — Alx Low Level Programming
0x07. Python - Test-driven development

## Why Tests are Important
Tests are the safety nets of your code. They ensure that your code works as intended and remains stable even when making changes. They catch bugs early, enhance code quality, and give you the confidence to refactor without fear of breaking things.

## Writing Docstrings for Tests
### doctest - Testing Interactive Python Examples
Example:
```python
def add(a, b):
    """
    Adds two numbers together.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```
Using docstrings with doctest allows testing code examples embedded in documentation. It validates if the actual output matches the expected output in these examples.

### Testing Through Documentation
Docstrings can serve as a testing ground. By embedding examples in the docstrings, you create living documentation that doubles as test cases, ensuring your code stays true to its documented behavior.

## Unit Tests in Python
### Unittest Module
Python's unittest module is a powerful tool for writing and running unit tests.

Example:

```python
import unittest

def multiply(a, b):
    return a * b

class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)
```
Here, we create a test case using `unittest.TestCase`. Each method starting with `test_` is a test case.

## Running Tests
### **For doctest:**
####  **Using Command Line:**
```bash
python -m doctest -v your_file.py
```
The `-m` flag executes the doctest module as a script.
`-v` stands for verbose output.

### **For unittest:**
#### **Using Command Line:**
```bash
python -m unittest discover
```
Searches for test cases in files starting with **test_** in the current directory and subdirectories.
Or specify a particular test file or class:
```bash
python -m unittest your_test_file.py
```
OR
```bash
python -m unittest YourTestClass.
```

#### **Inside Python Code:**
```python
import unittest

if __name__ == '__main__':
    unittest.main()
```
Run all test cases present in the file where this code is written.

## Conclusion
Test-driven development isn't just about finding bugs; it's about preventing them. By writing tests before writing code, you define the behavior and validate it as you develop. It's a systematic way to build robust, maintainable, and reliable software. Remember, tests are your code's best friends!

## Contact Me
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
