#!/usr/bin/env python

from random import randint

a = [randint(1,100) for x in range(randint(10,15))]
b = [randint(1,100) for x in range(randint(10,15))]

dup = [num for num in b if num in a]
print a
print b
print dup



