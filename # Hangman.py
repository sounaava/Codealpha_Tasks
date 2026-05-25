# Hangman

import random

words = ["dog", "monkey", "hippopotamus", "cat", "book", "rocket", "cricket", "football"]

letters = []
word = words[random.randrange(len(words))]

print("Welcome to Hangman!")

life = 5

while life > 0:

    guess = input("Enter your guess: ")

    if word.__contains__(guess):
        print("Wow! You guessed it right")

        letters.append(guess)

        if len(letters) == len(word):
            print("Congratulations!! You have guessed your word",word)
            break

        else:
            lettersleft = len(word) - len(letters)
            print("You have", lettersleft, "letters left")

    else:
        life -= 1

        if life == 0:
            print("Game Over! Your word was", word)
            break

        else:
            print("Oops! You have", life, "lives left, TRY AGAIN!!")