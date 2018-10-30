print('Welcome to the Homework Machine!\nSolving your problems since 2018.\n')
problem = '' 
while problem != 'bye':
    try:
        answer = eval(problem)
        print('Your answer is '+str(answer))
        if '/' in problem:
            new_problem = problem.replace('/','%')
            remainder = eval(new_problem)
            print('\tremainder '+str(remainder))
    except:
        if problem != '':
            print("That's not a math problem! Try again.")
    problem = raw_input("What is your problem? Type 'bye' to quit. ")
print("Bye bye!")
