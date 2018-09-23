#!/usr/bin/env python

from random import randint

a = [randint(1, 100) for i in range(25)]

"""for i in range(50):
    a.append(randint(0, 100))"""

"""for num in a:
    print num"""

"""a_less5 = [num for num in a if num < 5]
print a
print a_less5"""

init = [randint(1, 20) for i in range(25)]
print init
x = int(raw_input("Enter a number: "))
new = [num for num in init if num < x]
print new


