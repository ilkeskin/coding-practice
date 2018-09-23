#!/usr/bin/env python3

from random import choice

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
sowpods = []
with open("data/sowpods.txt", "r") as sp:
    sowpods = [w.strip() for w in sp]

def rand_word(wordlist):
    return choice(wordlist)

def main():
    word = rand_word(sowpods)
    correct_guesses = ["_" for l in word]
    counter = 0
    wrong_guesses = set()

    print("Welcome to Hangman!")
    while ("".join(correct_guesses) != word) and (len(wrong_guesses) < 7):
        print("\n", " ".join(correct_guesses), "\n")
        guess = ""
        while not len(guess) == 1:
            guess = input("Guess a letter: ").upper()
        if guess in word:
            char_pos = [pos for pos, char in enumerate(word) if char == guess]
            for pos in char_pos:
                correct_guesses[pos] = guess
        else:
            wrong_guesses.add(guess)
            print("Incorrect!")
            print(HANGMAN[len(wrong_guesses) - 1])
        counter += 1
    if ("".join(correct_guesses) == word):
        print("It took you %d guesses to guess %s!" % (counter, word))
    else:
        print("The word was %s" % word)

if __name__ == "__main__":
    main()
