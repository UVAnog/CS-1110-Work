import random

start = int(input("Pick a number: "))


if start <= -1:
    '''set low and high here'''
    start = random.randrange(1, 101)
else:
    guesses = int(input("How many guesses should you have?: "))
    count = 0
    win = 0

while count < guesses and win != -1:
    guess = int(input("guess a number: "))

    if guess < start:
        print ("Number is higher than that.")
        count += 1
    elif guess > start:
        print ("Number is lower than that.")
        count += 1
    if guess == start:
        print ("you win!")

if count == guesses:
        print ("you are out of guesses!")










