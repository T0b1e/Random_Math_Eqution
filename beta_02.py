import math
from os import write
import random
import time
import numpy as np

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

def player():
    player_count = input('How many player : ')
    try:
        final_player = int(player_count)
        if final_player < 0:
            print('That was in an list')
    except ValueError:
        try:
            final_v = float(player_count)
        except ValueError:
            final_player = str(player_count)

    return final_player

def username(player_count):
    for x in range(0,player_count):
        user_name = input('User name : ')
    return user_name

def num_1(level):#last_num
    if level <= 1:
        number_1 = random.randint(1,10)
    if level == 2:
        number_1 = random.randint(1,20)
    if level == 3:
        number_1 = random.randint(1,30)
    if level == 4:
        number_1 = random.randint(1,40)
    if level == 5:
        number_1 = random.randint(1,50)
    if level == 6:
        number_1 = random.randint(1,60)
    if level == 7:
        number_1 = random.randint(1,70)
    if level == 8:
        number_1 = random.randint(1,80)
    if level == 9:
        number_1 = random.randint(1,90)
    if level >= 10:
        number_1 = random.randint(1,100)
        hard_core = random.randint(0,100)
        if hard_core <= 50:
            temp = number_1 / 100
            number_2  = round(temp,2)
    #print(num_1)
    return number_1

def num_2(level):#
    if level <= 1:
        number_2 = random.randint(1,10)
    if level == 2:
        number_2 = random.randint(1,20)
    if level == 3:
        number_2 = random.randint(1,30)
    if level == 4:
        number_2 = random.randint(1,40)
    if level == 5:
        number_2 = random.randint(1,50)
    if level == 6:
        number_2 = random.randint(1,60)
    if level == 7:
        number_2 = random.randint(1,70)
    if level == 8:
        number_2 = random.randint(1,80)
    if level == 9:
        number_2 = random.randint(1,90)
    if level >= 10:
        number_2 = random.randint(1,100)
        hard_core = random.randint(0,100)
        if hard_core <= 50:
            temp = number_2 / 100
            number_2  = round(temp,2)

    return number_2

def num_3(level,num1,num2):

    number_3 = random.randint(1,100)
    check = num1 * num2
    if check % 2 == 0: #เลขคู่
        if number_3 % 2 != 0:
            number_3 = random.randint(1,100)
    if check % 2 != 0: #เลขคี่
        if number_3 % 2 == 0:
            number_3 = random.randint(1,100)

    return number_3

def operation(level):#
    operator = ['+','-','*','/','^','fac']
    
    if level <= 1:
        random_op = random.randint(0,2)
        final_op = (operator[random_op])
    if level == 2:
        random_op = random.randint(0,3)
        final_op = (operator[random_op])
    if level == 3:
        random_op = random.randint(0,4)
        final_op = (operator[random_op])
    if level == 4:
        random_op = random.randint(0,4)
        final_op = (operator[random_op])
    if level >= 5 and level < 8:
        random_op = random.randint(0,5)
        final_op = (operator[random_op])
    if level >= 8 and level < 9:
        random_op = random.randint(0,3)
        final_op = (operator[random_op])
    if level >= 9:
        random_op = random.randint(0,5)
        final_op = (operator[random_op])
        
    #print(final_op)
    return final_op

point = 0 #Static
def equation(no,num1,num2,op):
    
    if op == '+':
        print(f'{no} Question : {num1} + {num2}')
        ans = num1 + num2
    if op == '-':
        print(f'{no} Question : {num1} - {num2}')
        ans = num1 - num2
    if op == '*':
        print(f'{no} Question : {num1} * {num2}')
        ans = num1 * num2
    if op == '/':
        if num2 > 10:
            temp = random.randint(1,num1)
            num2 = temp
        if num2 == 0:
            temp = random.randint(1,num1)
            num2 = temp
        print(f'{no} Question : {num1} ÷ {num2} (2 digit)')
        ans = num1 / num2
        ans = round(ans,2)

    if op == '^':
        if num2 >= 5:
            temp = random.randint(1,2)
            num2 = temp
        print(f'{no} Question : {num1} ^ {num2}')
        ans = num1 ** num2
        
    if op == 'fac':
        if num1 > 10:
            temp = random.randint(1,10)
            num1 = temp
        print(f'{no} Question : Factorial {num1}')
        ans = math.factorial(num1)
    return ans

def hard_mode(no,num1,num2,num3,op):
    #2x+1 = 2 , 3 + 1x = 2, 2 + 1 = 2x
        x_place = random.randint(0,3)
        if op == '+':
            if x_place == 0:
                print(f'{no} Question : {num1}x + {num2} = {num3}')
                ans = (num3 - num2) / num1
            if x_place == 1:
                print(f'{no} Question : {num1} + {num2}x = {num3}')
                ans = (num3 - num1) / num2
            if x_place == 2:
                print(f'{no} Question : {num1} + {num2} = {num3}x')
                ans = (num1 + num2) / num3
        if op == '-':
            if x_place == 0:
                print(f'{no} Question : {num1}x - {num2} = {num3}')
                ans = (num3 + num2) / num1
            if x_place == 1:
                print(f'{no} Question : {num1} - {num2}x = {num3}')
                ans = (num3 - num1) / num2
            if x_place == 2:
                print(f'{no} Question : {num1} - {num2} = {num3}x')
                ans = (num1 - num2) / num3
        if op == '*':
            if x_place == 0:
                print(f'{no} Question : {num1}x * {num2} = {num3}')
                ans = num3 / (num1 * num2)  
            if x_place == 1:
                print(f'{no} Question : {num1} * {num2}x = {num3}')
                ans = num3 / (num1 * num2)  
            if x_place == 2:
                print(f'{no} Question : {num1} * {num2} = {num3}x')
                ans = (num1 * num2) / num3

        return ans

def Matrix():
    #matrix = [[num]]
    for x in range(3):
        num = random.randint(1,20)
        matrix = [[num,num]]
    print(matrix)
    
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
    print('POINT : ', final_point)

    return final_point

def time_count():
    timer = 0
    for x in range(180):
        timer = timer + 1
        #print(timer)
        time.sleep(1)
    return timer

def leveling(point):
    timer = 0
    if point < 200:
        level = 0
    if point >= 200 and point <= 500:
        level = 1
        if point >= 200 and point <= 300:
            print(f'Congratulation you has been {level}')
    if point > 500 and point <= 1000:
        level = 2
        if point > 500 and point <= 700:
            print(f'Congratulation you has been reach {level}')

    if point > 1000 and point <= 2000:
        level = 3
        if point > 1000 and point <= 1300:
            print(f'Congratulation you has been reach {level}')

    if point > 2000 and point <= 3000:
        level = 4
        if point > 2000 and point <= 2300:
            print(f'Congratulation you has been reach {level}')
    if point > 3000 and point <= 4000:
        level = 5
        if point > 3000 and point <= 3200:
            print(f'Congratulation you has been reach {level}')
    if point > 4000 and point <= 5000:
        level = 6
        if point > 4000 and point <= 4200:
            print(f'Congratulation you has been reach {level}')
    if point > 5000 and point <= 6000:
        level = 6
        if point > 5000 and point <= 5200:
            print(f'Congratulation you has been reach {level}')
    if point > 6000 and point <= 7000:
        level = 7
        if point > 6000 and point <= 6200:
            print(f'Congratulation you has been reach {level}')
    if point > 7000 and point <= 8000:
        level = 8
        if point > 3000 and point <= 3200:
            print(f'Congratulation you has been reach {level}')
    if point > 8000 and point <= 9000:
        level = 9
        if point > 9000 and point <= 10000:
            print(f'Congratulation you has been reach {level}')
    if point > 10000:
        level = 10
        print(f'Congratulation you has been finish game at time {level}')

    print('LEVEL : ',level)
    return level

Quotes = (
    "Do not fear failure but rather fear not trying.'― Roy T. Bennett, The Light in the Heart",
    "“Great things happen to those who don't stop believing, trying, learning, and being grateful.”",
    "“A bruise is a lesson... and each lesson makes us better.”",
    "“The one who falls and gets up is stronger than the one who never tried. Do not fear failure but rather fear not trying.”",
    "“To learn something new, you need to try new things and not be afraid to be wrong.”")
    #https://www.goodreads.com/quotes/tag/trying

count = player()
username(count)
#level = leveling(final_point)

for x in range(1,101): 
    level = leveling(final_point)
    num1 = num_1(level)
    num2 = num_2(level)
    num3 = num_3(level,num1,num2)
    op = operation(level) #Return ค่าจาก final_level
    if level < 10:
        final_answer = equation(x,num1,num2,op)
    if level >= 10:
        hard_mode(level,x,num1,num2,num3,op)
    if level >= 11:
        Matrix(num1,num2)

    final_points =  check_ans(final_answer)
    if final_point <= 0:
        final_quotes = random.choice(Quotes)
        print(final_quotes)
        print('Game Over !')
        break
    if final_point == 7000:
        break
if x == 20:
    print('Final Score ',final_point)


#Matrix()