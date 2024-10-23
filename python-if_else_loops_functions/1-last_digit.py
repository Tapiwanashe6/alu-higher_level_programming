#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_number=str(number)
str_last_number=str_number[-1]
number = int(str_last_number)
if number > 5:
    print(f"Last digit of {str_number} is {str_last_number} and is greater than 5")
elif number == 0:
    print(f"Last digit of {str_number} is {str_last_number} and is 0")
else:
    print(f"Last digit of {str_number} is {str_last_number} and is less than 6 and not 0")
