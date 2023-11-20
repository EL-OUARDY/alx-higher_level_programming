# Exceptions — Alx Higher Level Programming 
0x05. Python - Exceptions

## Errors vs. Exceptions
`Errors` are generally more severe issues that cause a program to terminate (ex: *Syntax Errors*), while `exceptions` are raised when a problem occurs within a code block but can be handled without halting the program.

## What are Exceptions and How to Use Them
### Exceptions Defined
Exceptions are unexpected events or conditions that occur during program execution, leading to a disruption in the normal flow. Python provides a way to handle these exceptional conditions using **try-except** blocks.

### Using Exceptions
```python
try:
    # Code that might raise an exception
    result = 10 / 0  # Example: division by zero
except ZeroDivisionError as e:
    # Handling the specific exception
    print("Error:", e)
```

## When to Use Exceptions
### Need for Exceptions
Exceptions are used to handle unexpected situations that might arise during program execution, allowing graceful handling of errors without crashing the program.

## Correctly Handling Exceptions
### Handling Exceptions
```python
try:
    # Code that might raise an exception
    result = int(input("Enter a number: "))
except ValueError:
    # Handling incorrect input
    print("Please enter a valid number.")
else:
    # Executed if no exception occurred
    print("You entered:", result)
finally:
    # Cleanup or final actions
    print("Execution complete.")
```

## Purpose of Catching Exceptions
### Catching Exceptions
Catching exceptions allows programs to handle errors gracefully, providing a way to recover from unexpected situations, log errors, and ensure the program doesn't crash abruptly.

## Raising a Built-in Exception
### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return "Valid Age!"
```

## Implementing Clean-up Actions
### Clean-up After Exceptions
Clean-up actions or `finally` blocks are used to implement code that should be executed regardless of whether an exception occurred or not. It's useful for releasing resources or performing necessary clean-up.


## Contact Me
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com

