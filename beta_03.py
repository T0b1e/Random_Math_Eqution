import random
import pandas as pd
import numpy as np

X = 0
NO = 10

equption = []

# [number1,[equption],number2]

number = []
#New version Clean all old code
def generate_number(level):
    global number_1 
    global number_2 

    for X in range(0,NO):

        number.append([])
        if level == 0:
            number_1 = random.randint(0,0)
            number_2 = random.randint(0,0)
        if level == 1:
            number_1 = random.randint(0,10)
            number_2 = random.randint(0,10)
        if level == 2:
            number_1 = random.randint(0,20)
            number_2 = random.randint(0,20)
        if level == 3:
            number_1 = random.randint(0,30)
            number_2 = random.randint(0,30)
        if level == 4:
            number_1 = random.randint(0,40)
            number_2 = random.randint(0,40)
        if level == 5:
            number_1 = random.randint(0,50)
            number_2 = random.randint(0,50)
        if level >= 6:
            number_1 = random.randint(0,0)
            number_2 = random.randint(0,0)

        for Y in range(1):
            number[X].append(number_1)
            number[X].append(number_2)

    #print(number)
    return number

operator = []
operator_list = ['+','-','*','/','^','!']

def generate_operator(level):
    
    for X in range(0,NO):
        operator.append([])

        if level == 0:
            operate = operator_list[random.randint(0,0)]
        if level == 1:
            operate = operator_list[random.randint(0,1)]
        if level == 2:
            operate = operator_list[random.randint(0,2)]
        if level == 3:
            operate = operator_list[random.randint(0,3)]     
        if level == 4:
            operate = operator_list[random.randint(0,4)]
        if level == 5:
            operate = operator_list[random.randint(0,4)]
        if level >= 6:
            operate = operator_list[random.randint(0,5)]

        operator[X].append(operate)
    #print(operator)
    return operator



list = generate_number(5)


'''number = generate_number(5)
operator = generate_operator(5)

def equption(number,operator):
    print(number,operator)

equption(number,operator)'''

'''list = [[1,2],[3,4],[5,6]]
print(list[1][1])'''

'''list = [1,[2],3]
print(list[1][0])'''