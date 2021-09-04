import math
from os import write
import random
import time

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
        if num2 == 0:
            temp = random.randint(1,num1)
            num2 = temp
        print(f'{no} Question : {num1} ÷ {num2} (2 digit)')
        ans = num1 / num2
        ans = round(ans,2)

    if op == '^':
        if num2 >= 5:
            temp = random.randint(2,4)
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
    for x in range(1,50):
        time.sleep(1)
        #print(x)
        if x == 20:
            print(f'you have {x} left')
        if x == 40:
            print(f'you have {x} left')
        if x == 50:
            print('Time out now')

def leveling(point):
   
    if point < 200:
        level = 0
    if point >= 200 and point <= 500:
        level1 = time.gmtime()
        time_level1 = level1[5]
        final_time1 = start_timer - time_level1

        level = 1
        if point >= 200 and point <= 300:
            print(f'Congratulation you has been {level} at {final_time1} second')
    if point > 500 and point <= 1000:
        level2 = time.gmtime()
        time_level2 = level2[5]
        final_time2 = start_timer - time_level2

        level = 2
        if point > 500 and point <= 700:
            print(f'Congratulation you has been {level} at {final_time2} second')

    if point > 1000 and point <= 2000:
        level3 = time.gmtime()
        time_level3 = level3[5]
        final_time3 = start_timer - time_level3

        level = 3
        if point > 1000 and point <= 1300:
            print(f'Congratulation you has been {level} at {final_time3} second')

    if point > 2000 and point <= 3000:
        level4 = time.gmtime()
        time_level4 = level4[5]
        final_time4 = start_timer - time_level4

        level = 4
        if point > 2000 and point <= 2300:
            print(f'Congratulation you has been {level} at {final_time4} second')
    if point > 3000 and point <= 4000:
        level5 = time.gmtime()
        time_level5 = level5[5]
        final_time5 = start_timer - time_level5
        level = 5
        if point > 3000 and point <= 3200:
            print(f'Congratulation you has been {level} at {final_time5} second')
    
    if point == 7000:
        level = 6
        end_time = time.gmtime()
        end_timer = end_time[5]
        final_time = end_timer - start_timer
        print(f'Congratulation you has been finish game at time {level} at {final_time} second')

    return level

#final_time = timer()
"""data = username()
put_data(data)"""

Quotes = (
    "Do not fear failure but rather fear not trying.'― Roy T. Bennett, The Light in the Heart",
    "“Great things happen to those who don't stop believing, trying, learning, and being grateful.”",
    "“A bruise is a lesson... and each lesson makes us better.”",
    "“The one who falls and gets up is stronger than the one who never tried. Do not fear failure but rather fear not trying.”",
    "“To learn something new, you need to try new things and not be afraid to be wrong.”")
    #https://www.goodreads.com/quotes/tag/trying

count = player()
username(count)
level = ranking()


for x in range(1,20): 
    last_number = level
    num1 = num_1(level)
    num2 = num_2(level)
    op = operation(level) #Return ค่าจาก final_level
    final_answer = equation(x,num1,num2,op)
    final_points =  check_ans(final_answer)
    if final_point <= 0:
        final_quotes = random.choice(Quotes)
        print(final_quotes)
        print('Game Over !')
        break

    if final_point == 7000:
        break
LEVEL = leveling(final_points)


