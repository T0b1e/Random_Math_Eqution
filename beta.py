import random
import math

def set_value1():
    level = 1
    if level == 1:
        number_1 = 10

def set_value2():
    level = 1
    if level == 1:
        number_2 = 10

def get_firstnum(number_1):
    random_num1 = random.randint(1,int(number_1))
    #print(random_num1,random_num2)
    return random_num1

def get_secondnum(number_1,number_2,random_num1):
    random_num2 = random.randint(1,int(number_2))
    if random_num2 < random_num1:
        random_num3 = random.randint(random_num1,number_1)
        random_num2 = random_num3
    #print(random_num1,random_num2)
    return random_num2

def get_op():
    operator = ['+','-','*','/']
    random_op = random.randint(0,len(operator))
    #print(operator[random_op])
    return operator[random_op]
    
get_op()

get_firstnum(set_value1())
get_secondnum(set_value1(),set_value2(),get_firstnum())


#TOILET