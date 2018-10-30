import random

guess = ''
correct = False
answer = random.randint(1,100)
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
            answer = random.randint(1,100)
    guess = raw_input("Make a guess between 1 and 100 (type 'quit' to quit): ")
print("Bye bye!")
