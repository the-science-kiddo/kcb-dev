from random import randint
import sys

limit = int(sys.argv[1])
guess = ''
correct = False
answer = randint(1,limit)
while guess != 'quit' and correct == False:
    if guess != '':
        print('Your guess is '+str(guess))
        if int(guess) > answer:
            print('Your guess is too high. Try again!')
        if int(guess) < answer:
            print('Your guess is too low. Try again!')
        if int(guess) == answer:
            print('Correct! You win!')
            print("I just chose a new number, let's play again!")
            answer = randint(1,limit)
    guess = raw_input("Make a guess between 1 and " + str(limit) + " (type 'quit' to quit): ")
print("Bye bye!")
