# Import & Modules — Alx Higher Level Programming
0x02. Python - import & modules

## Overview
Python uses imports to access code from other files, making code reusable and organized. \
**Modules**  are files containing Python code. These files can include functions, classes, and variables that can be imported and used in other Python files.

## Importing Functions from Another File
Use `import` or `from` to access functions from other files.
```python
# Import the entire module
import module_name

# Import a specific function
from module_name import function_name
```

## Using Imported Functions/Packages
Access functions from imported modules using dot notation.
```python
# Using imported functions
module_name.function_name()
```

## Creating a Module
A Python script becomes a module when it's imported into other scripts.
```python
# Creating a module (example.py)
def some_function():
    return "Hello from example module"
```

## Using the Built-in Function dir()
`dir()` lists all functions and attributes within a module.
```python
# Check available functions in a module
print(dir(module_name))
```

## Preventing Code Execution on Import
Use `if __name__ == "__main__":` to avoid code execution on import.
```python
# Execute code only when file is run directly
if __name__ == "__main__":
    # Your code here
```

## Using Command Line Arguments (argparse)
Access command line arguments using the sys module:
```python
import sys
argument = sys.argv[1]
```
The `argparse` module allows handling command-line arguments easily.
```python
import argparse

parser = argparse.ArgumentParser(description='Description of the program')
parser.add_argument('argument', type=int, help='Description of the argument')
args = parser.parse_args()
print(args.argument)
```

## Conclusion
Knowing how to use Python's import and module system is essential for organizing and reusing code. By importing functions, you can use code from other files, and creating modules helps group related code together.
