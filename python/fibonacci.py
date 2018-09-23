#!/usr/bin/env python

def fibonacci(amnt):
    i = 1
    if amnt == 0:
        fib = []
    elif amnt == 1:
        fib = [0]
    elif amnt == 2:
        fib = [0,1]
    elif amnt > 2:
            fib = [0,1]
            while i < (amnt - 1):
                fib.append(fib[i] + fib[i-1])
                i += 1
    return fib

amnt = int(raw_input("Enter the amount of Fibonacci numbers to create: "))
print fibonacci(amnt)
