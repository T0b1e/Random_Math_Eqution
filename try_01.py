import math
import random
import time

for sum in range(5):
    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    
operator = ['+','-','*','/']

if num_2 > num_1:
    num_3 = random.randint(num_1,10)
    num_2 = num_3

random_op = random.randint(0,len(operator))
final_op = (operator[random_op])

if final_op == '+':
    ans = num_1 + num_2
    print(f'Fisrt Equation is {num_1} + {num_2} = ')
    #print(ans)
if final_op == '-':
    ans = num_1 - num_2
    print(f'Fisrt Equation is {num_1} - {num_2} = ')
    #print(ans)
if final_op == '*':
    ans = num_1 * num_2
    print(f'Fisrt Equation is {num_1} * {num_2} = ')
    #print(ans)
if final_op == '/':
    ans = num_1 / num_2
    print(f'Fisrt Equation is {num_1} / {num_2} = ')
    #print(ans)

answer = input('What is your answer : ')

"""for x in range(1,50):
    #print(x)
    time.sleep(1)
    if x == 20:
        print(f'you have {x} left')
    if x == 40:
        print(f'you have {x} left')
"""
try:
    final_ans = int(answer)
    #print("Input is an integer number. Number = ", val)
except ValueError:
    final_ans = str(answer)
    print('This is not an number')

if final_ans == ans:
    print(f'Correct answer')
else:
    print(f'Not an answer, your correct ansewr is {ans}')