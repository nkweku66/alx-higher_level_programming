#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
else:
    last_digit = (number * -1) % 10
    last_digit = (last_digit * -1)

if last_digit > 5:
    return(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_number < 6 and last_number != 0:
    return(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    return(f"Last digit of {number) is {last_digit} and is 0")
