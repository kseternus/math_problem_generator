import time
import random

operators = ['*', '/', '+', '-']
problems = 10
wrong = 0


def introduction():
    input('Welcome to math problem generator!\n'
          'When entering the answer to the division result, enter it accurate to two decimal places\n\n'
          'Press any key to start')


def generate_problem():
    operator = random.choice(operators)

    if operator == '*' or operator == '/':
        left = random.randint(1, 10)
        right = random.randint(1, 10)
        equation = f'{str(left)} {operator} {str(right)}'
        if operator == '/':
            answer = format(eval(equation), '.2f')
        else:
            answer = eval(equation)
    else:
        left = random.randint(1, 100)
        right = random.randint(1, 100)
        equation = f'{str(left)} {operator} {str(right)}'
        answer = eval(equation)
    return equation, answer


def generate_equation():
    global wrong
    start = time.time()
    for i in range(problems):
        equation, answer = generate_problem()
        while True:
            guess = input(f'Problem number {i+1}:\n{equation} = ')
            if guess == str(answer):
                break
            else:
                print('Wrong anwser! Try again.')
                wrong += 1

    end = time.time()
    print(f'You finished in {(end-start):.2f}s. You made {wrong} mistakes!\n'
          f'Your score is {((problems/(problems+wrong))*100):.2f}%')


if __name__ == '__main__':
    introduction()
    generate_equation()
