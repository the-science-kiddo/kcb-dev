problem = ''
while problem != 'bye':
    problem = raw_input("What is your problem? Type 'bye' to quit. ")
    answer = eval(problem)
    print('Your answer is '+str(answer))
print("Bye bye!")
