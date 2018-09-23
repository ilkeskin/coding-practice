#!/usr/bin/env python

def has_divisors(x):
    divisors = [i for i in range(1,x+1) if (x % i == 0)]
    if len(divisors) > 0:
        return True
    else:
        return False

def get_divisors(x):
    return [i for i in range(1,x+1) if (x % i == 0)]

def is_prime(x):
    if get_divisors(x) == [1, x]:
        return True
    else:
        return False

num = 1 
while num != 0:
    num = int(raw_input("Enter a number to check whether it is a prime number: "))   
    print get_divisors(num)
    print is_prime(num)
