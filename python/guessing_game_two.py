#!/usr/bin/env python3

from random import randint

def main():
    counter = 1
    num = -1
    p_nums = [x for x in range(101)]
    
    while not ((num >= 0) and (num <= 100)):
        num = int(input("Enter any number between 0 and 100: "))
    
    while True:
        hint = ""
        g = p_nums[len(p_nums)//2]
        print("My guess is: ", g)
        while not (hint == "l" or hint == "h" or hint == "c"):
            hint = input("Is my guess high (h), low (l) or correct (c)? ")
        if hint == "l":
            p_nums = p_nums[(len(p_nums)//2):]
            counter += 1
        elif hint == "h":
            p_nums = p_nums[:(len(p_nums)//2)]
            counter += 1
        elif hint == "c":
            print("It took me %d iterations to guess your number %d" % (counter, num))
            break
        print(p_nums)

if __name__ == "__main__":
    main()
