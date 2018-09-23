#!/usr/bin/env python

user1_in = str(raw_input("[User 1] Choose Rock, Paper or Scissors: "))
while (user1_in != "Rock") and (user1_in != "Paper") and (user1_in != "Scissors"):
    user1_in = str(raw_input("[User 1] Choose Rock, Paper or Scissors: "))
user2_in = raw_input("[User 2] Choose Rock, Paper or Scissors: ")
while (user2_in != "Rock") and (user2_in != "Paper") and (user2_in != "Scissors"):
    user2_in = raw_input("[User 2] Choose Rock, Paper or Scissors: ")

if user1_in == "Rock":
    if user2_in == "Scissors":
        print "User 1 wins!"
    elif user2_in == "Paper":
        print "User 2 wins!"
    else:
        print "Draw!"
elif user1_in == "Paper":
    if user2_in == "Rock":
        print "User 1 wins!"
    elif user2_in == "Scissors":
        print "User 2 wins!"
    else:
        print "Draw!"
else:
    if user2_in == "Paper":
        print "User 1 wins!"
    elif user2_in == "Rock":
        print "User 2 wins!"
    else:
        print "Draw!"
