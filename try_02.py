import math
import random
import time

def num_1():
    num_1 = random.randint(1,10)
    #print(num_1)
    return num_1

def num_2():
    num_2 = random.randint(1,10)
    #print(num_2)
    return num_2

def operation():
    operator = ['+','-','*','/']
    random_op = random.randint(0,len(operator))
    final_op = (operator[random_op])
    #print(final_op)
    return final_op

def equation(num1,num2,op):
    if op == '+':
        print(f'Question : {num1} + {num2}')
        ans = num1 + num2
    if op == '-':
        print(f'Question : {num1} - {num2}')
        ans = num1 - num2
    if op == '*':
        print(f'Question : {num1} * {num2}')
        ans = num1 * num2
    if op == '/':
        print(f'Question : {num1} ÷ {num2}')
        ans = num1 / num2

    return ans

def check_ans(ans):
    point = 1
    answer = input('ANSWER : ')
    try:
        final_ans = float(answer)
        final_ans = int(answer)
        #print("Input is an integer number. Number = ", val)
    except ValueError:
        final_ans = str(answer)
        print('This is not an number')

    if final_ans == ans:
        print('You got correct answer')
        point = point + 1
    else:
        print(f'Wong answer, and correct answer is {final_ans}')

    return point

def time_count():
    for x in range(1,50):
        time.sleep(1)
        if x == 20:
            print(f'you have {x} left')
        if x == 40:
            print(f'you have {x} left')

"""ans = equation(num_1(),num_2(),operation())
check_ans(ans)
time_count()"""

def no():
    for number in range(0,5):
        ans = equation(num_1(),num_2(),operation())
        answer = check_ans(ans)
        #print(answer)
no()