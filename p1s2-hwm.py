problem = raw_input("What is your problem? Type 'bye' to quit. ")
while problem != 'bye':
    answer = eval(problem)
    print('Your answer is '+str(answer))
    problem = raw_input("What is your problem? Type 'bye' to quit. ")
print("Bye bye!")
