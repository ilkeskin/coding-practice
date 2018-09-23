#!/usr/bin/env python

from random import randint

rnd_num = randint(1000, 9999)

def sep_digits(num):
    digits = []
    div = 1000 # assume number is 4-digits max
    while div > 0:
        digit = num // div
        digits.append(digit)
        num -= div * digit
        div = div / 10
    return digits

def cmp_digits(vec1, vec2):
    result = {
        "cows": 0,
        "bulls": 0
        }
    
    for i in range(0, len(vec1)):
        if vec1[i] == vec2[i]:
            result["cows"] += 1
        else:
            result["bulls"] += 1
    return result

def main():
    print "Welcome to the Cows and Bulls game!"
    guesses = 0
    while True:
        #print rnd_num
        
        # handle user input
        usr_in = ""
        while not ((len(usr_in) == 4) and usr_in.isdigit()):
            usr_in = raw_input("Enter a 4-digit number: ")
        
        # compare user input with random number digit by digit
        guess = cmp_digits(sep_digits(int(usr_in)), sep_digits(rnd_num))
        
        # handle output
        if guess["cows"] == 4:
            print "You guessed the number!"
            break
        else:
            print "%d cow(s), %d bull(s)" % (guess["cows"], guess["bulls"])
        guesses += 1
    print "It took you %d guesses to guess the right number" % guesses

if __name__ == "__main__":
    main()
