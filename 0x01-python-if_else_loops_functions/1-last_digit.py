#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10

if number < 0:
   lastdigit = -lastdigit
the_string = "Last digit of {} is {} and is ".format(number, lastdigit), end=""
if lastdigit > 5:
    print(f"{the_string} greater than 5")
elif lastdigit == 0:
    print(f"{the_string}" 0)
else:
    print(f"{the_string} less than 6 and not 0")
