#!/usr/bin/env python

from random import randint
num = randint(1,9)
user_in = ""
cntr = 1
while user_in != "0":
    user_in = raw_input("Guess a number between 1 and 9 or type \'0\' to exit: ")
    if (int(user_in) > num) and (int(user_in) != 0):
        print "Guess a little lower!"
        cntr+=1
    elif (int(user_in) < num) and (int(user_in) != 0):
        print "Guess a little higher!"
        cntr+=1
    elif (int(user_in) == num) and (int(user_in) != 0):
        print "You guessed the number within %d attempts!" % (cntr)
        break

