from random import randint
import sys

guess = randint(1,100)
low_end = 1
high_end = 100
user_input = raw_input("Think of a number between 1 and 100, then press enter, or type 'quit' to quit. ")
while user_input != 'quit':
    print('My guess is '+str(guess)+". Type 'high' if it's too high. Type 'low' if it's too low. Type 'correct' if I guessed right!")
    response = raw_input(':')
    if response == 'high':
        high_end = guess
    elif response == 'low':
        low_end = guess
    elif response == 'correct':
        print("Yay for me! I'm going to choose again.")
        low_end = 1
        high_end = 100
        user_input = raw_input("Think of a number between 1 and 100, then press enter, or type 'quit' to quit. ")
    elif response == 'quit':
        print('Bye bye!')
        exit()
    else:
        continue
    guess = randint(low_end,high_end)
