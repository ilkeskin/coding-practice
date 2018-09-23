#!/usr/bin/env python

from random import randint

nums = {randint(1, 20) for i in range(5)}
nums = list(nums)
nums.sort()
print nums

x = int(raw_input("Enter a number to see if it is in the list: "))

in_list = x in nums
print "using in: %s" % in_list

in_list = False
for num in nums:
    if x == num:
        in_list = True
print "using for loop: %s" % in_list

# TODO: add implementation of binary search
