problem = '' 
while problem != 'bye':
    try:
        answer = eval(problem)
        print('Your answer is '+str(answer))
    except:
        if problem != '':
            print("That's not a math problem! Try again.")
    problem = raw_input("What is your problem? Type 'bye' to quit. ")
print("Bye bye!")
