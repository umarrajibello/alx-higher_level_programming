#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (-1 * number) % 10
    last_digit *= -1
else:
    last_digit = number % 10
if last_digit > 5:
    final_str = "and is greater than 5"
elif last_digit == 0:
    final_str = "and is 0"
else:
    final_str = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last_digit, final_str))
