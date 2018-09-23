#!/usr/bin/env python

happy_primes = []

with    open("data/primenumbers.txt", 'r') as primes,\
        open("data/happynumbers.txt", 'r') as happies:
    primes = [int(x) for x in primes]
    happies = [int(x) for x in happies]
    happy_primes = [x for x in primes if x in happies]
print happy_primes
