#!/usr/bin/env python

num_in = int(raw_input("Enter a number: "))

divisors = range(1,num_in)

print divisors
for div in divisors:
    if num_in % div != 0:
        #print "%f / %f = %f" % (num_in, div, (num_in % div))
        divisors.remove(div)
        print divisors

