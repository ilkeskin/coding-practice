#!/usr/bin/env python

from random import randint

rnd_lst = [randint(1, 10) for i in range(10)]
print rnd_lst

def unique_loop(lst):
    unq_lst = []
    for el in lst:
        if el not in unq_lst:
            unq_lst.append(el)
    return unq_lst

def create_set(lst):
    return list(set(lst))

print unique_loop(rnd_lst)
print create_set(rnd_lst)
