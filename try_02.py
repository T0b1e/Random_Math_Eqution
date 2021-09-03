import math
from os import write
import random
import time
import json


start_time = time.gmtime()
start_timer = start_time[5]

def leveling_number(level):
    if level == 1:
        last_num = 10
    if level == 2:
        last_num = 20
    if level == 3:
        last_num = 30
    if level == 4:
        last_num = 40
    return last_num
    
"""def username():
    user_name = input('User name : ')

    return user_name

def put_data(data, filename = 'users.json'):
    with open (filename,'w') as f:
        json.dump(data,f,indent=4)
    
    with open ('users.json') as json_file:
        data = json.load(json_file)
        temp = data['name']
        temp.append('user')"""


def num_1(last_num):#last_num
    if last_num == 1:
        num_1 = random.randint(1,10)
    if last_num == 2:
        num_1 = random.randint(1,20)
    if last_num == 3:
        num_1 = random.randint(1,30)
    if last_num == 4:
        num_1 = random.randint(1,40)
    if last_num >= 5 and last_num < 8:
        num_1 = random.randint(1,50)
    if level >= 8:
        num_1 = random.randint(1,100)
    #print(num_1)
    return num_1

def num_2(last_num):#
    if last_num == 1:
        num_2 = random.randint(1,10)
    if last_num == 2:
        num_2 = random.randint(1,20)
    if last_num == 3:
        num_2 = random.randint(1,30)
    if last_num == 4:
        num_2 = random.randint(1,40)
    if last_num >= 5 and last_num < 8:
        num_2 = random.randint(1,50)
    if level >= 8:
        num_2 = random.randint(1,100)
    #print(num_1)
    return num_2

def operation(level):#
    operator = ['+','-','*','/','^','fac']
    
    if level == 1:
        random_op = random.randint(0,2)
        final_op = (operator[random_op])
    if level == 2:
        random_op = random.randint(0,3)
        final_op = (operator[random_op])
    if level == 3:
        random_op = random.randint(0,4)
        final_op = (operator[random_op])
    if level >= 5 and level < 8:
        random_op = random.randint(0,5)
        final_op = (operator[random_op])
    if level >= 8:
        random_op = random.randint(0,5)
        final_op = (operator[random_op])
    #print(final_op)
    return final_op

point = 0 #Static
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
        if num2 == 0:
            temp = random.randint(1,num1)
            num2 = temp
        print(f'Question : {num1} ÷ {num2} (2 digit)')
        ans = num1 / num2
        ans = round(ans,2)

    if op == '^':
        if num2 >= 5:
            temp = random.randint(2,4)
            num2 = temp
        print(f'Question : {num1} ^ {num2}')
        ans = num1 ** num2
        
    if op == 'fac':
        if num1 > 10:
            temp = random.randint(1,10)
            num1 = temp
        print(f'Question : Factorial {num1}')
        ans = math.factorial(num1)
    return ans

final_point = 0
def ranking():
    your_level =input('Ranking(1-10) : ')
    try:
        final_rank = int(your_level)
        if final_rank < 0:
            print('That was in an list')
    
    except ValueError:
        try:
            final_rank = float(your_level)
        except ValueError:
            final_rank = str(your_level)

    return final_rank

def check_ans(ans):

    global final_point
    answer = input('ANSWER : ')
    try:
        final_ans = int(answer)
        if final_ans < 0:
            print('That was not an answer')
        #print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            final_ans = float(answer)
        except ValueError:
            final_ans = str(answer)
            
    
    if final_ans == ans:
        print('You got correct answer')

        final_point = final_point + 200
        
    else:
        print(f'Wong answer, and correct answer is {ans}')

        final_point = final_point - 100
        if final_point <= 0:
            final_point = 0
    print(final_point)

    return final_point

def time_count():
    for x in range(1,50):
        time.sleep(1)
        #print(x)
        if x == 20:
            print(f'you have {x} left')
        if x == 40:
            print(f'you have {x} left')
        if x == 50:
            print('Time out now')

def timer():
    clock = 10
    while clock >= 0:
        #print(clock)
        clock -= 1
        time.sleep(1)

    return clock

def leveling(point):
    Quotes = (
    "Do not fear failure but rather fear not trying.'― Roy T. Bennett, The Light in the Heart",
    "“Great things happen to those who don't stop believing, trying, learning, and being grateful.”",
    "“A bruise is a lesson... and each lesson makes us better.”",
    "“The one who falls and gets up is stronger than the one who never tried. Do not fear failure but rather fear not trying.”",
    "“To learn something new, you need to try new things and not be afraid to be wrong.”")
    #https://www.goodreads.com/quotes/tag/trying

    if point <= 0:
        final_quotes = random.choice(Quotes)
        print(final_quotes)
    if point < 500:
        level = 0
    if point == 500:
        level = 1
        print(f'Congratulation you has been {level}')
    if point > 500 and point <= 1000:
        level = 2
        print(f'Congratulation you has been {level}')
    if point > 1000 and point <= 2000:
        level = 3
        print(f'Congratulation you has been {level}')
    if point > 2000 and point <= 3000:
        level = 4
        print(f'Congratulation you has been {level}')
    if point > 3000 and point <= 4000:
        level = 5
        print(f'Congratulation you has been {level}')
    if point == 7000:
        level = 6
        end_time = time.gmtime()
        end_timer = end_time[5]
        final_time = end_timer - start_timer
        print(f'Congratulation you has been finish game at time {level} at {final_time} second')

    return level

"""def no():
    for number in range(0,5):
        final_level = leveling_number(last_level) 
        final_num1 = num_1(final_level) #Get last number from 
        final_num2 = num_2(final_level) #Get last number from 
        ans = equation(final_num1,final_num2,operation()) #Return answer question
        answer = check_ans(ans) #Return point
        last_level = leveling(answer) #answer = point
        #print(answer)
no()

"""
""" 5 function
Time line 
1.Generate number by check level
2.Generate Operation by check level
3.Get Equation by using number and operation from 1,2
4.Check answer and add point
5.Check level by using point
6.Return level

"""
#final_time = timer()
"""data = username()
put_data(data)"""

level = ranking()

for x in range(1,100): 
    last_number = level
    num1 = num_1(level)
    num2 = num_2(level)
    op = operation(level) #Return ค่าจาก final_level
    final_answer = equation(num1,num2,op)
    final_points =  check_ans(final_answer)
    if final_point <= 0:
        print('Game Over !')
        break

    if final_point == 7000:
        break
    LEVEL = leveling(final_points)
    

