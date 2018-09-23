#!/usr/bin/env python

str_in = str(raw_input("Enter a multi-word string: "))

def rev_str(inp):
    words = inp.split()
    return " ".join(words[::-1])

print str_in
print rev_str(str_in)
