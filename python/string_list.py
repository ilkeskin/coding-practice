#!/usr/bin/env python  

str_in = str(raw_input("Enter a string: "))
str_rvs = str_in[::-1]
if str_in == str_rvs:
    print "%s is a palindrome!" % str_in
else:
    print "%s is not a palindrome!" % str_in
