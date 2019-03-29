# Nph2tx
# Nolan Harris

print("Pick a number between 1 and 100 and I will guess it.")
guesses = int(input("How many guesses should I get?: "))
win = 0
count = 0
low = 0
high = 100

while count < guesses and win != 1:
    guess  = (high+low)//2
    answer = input('Is your number higher, lower, or the same as ' + str(guess) + '?')
    answer=answer.lower()

    if answer == 'same':
        print ('I won!')
        win = 1
    elif answer == 'lower':
        high = guess
    elif answer == 'higher':
        low = guess
    if (high - low) == 1:
        print("Stop. How can it be both higher than" + str(low) + 'and' + str(high) + '?')
        win = 1
    else:
        count = count + 1
x = str(input('I lost! What was your number?: '))
print('Well played!')

