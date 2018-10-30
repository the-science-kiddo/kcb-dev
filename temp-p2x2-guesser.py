from random import randint
import sys

golden = 0.38197
guess = randint(1,100)
low_end = 1
high_end = 100
user_input = raw_input("Think of a number between 1 and 100, then press enter, or type 'quit' to quit. ")
while user_input != 'quit':
    print('My guess is '+str(guess)+". Type 'high' if it's too high. Type 'low' if it's too low. Type 'correct' if I guessed right!")
    response = raw_input(':')
    if response == 'high':
        high_end = guess-1
        hilo = 0
    elif response == 'low':
        low_end = guess+1
        hilo = 1
    elif response == 'correct':
        print("Yay for me! I'm going to choose again.")
        low_end = 1
        high_end = 100
        user_input = raw_input("Think of a number between 1 and 100, then press enter, or type 'quit' to quit. ")
        hilo = randint(0,1)
    elif response == 'quit':
        print('Bye bye!')
        exit()
    else:
        continue
    delta = high_end - low_end
    if hilo == 0:
        target = low_end + int(delta * golden)
    else:
        target = high_end - int(delta * golden)
    low_temp = target - int(delta / 8)
    high_temp = target + int(delta / 8)
    guess = randint(low_temp,high_temp)
