#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = -1 if number < 0 else 1  # get number sign
number *= sign  # abs value of number
last_digit = (number % 10) * sign

print(f"Last digit of {number * sign} is {last_digit} ", end="")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
