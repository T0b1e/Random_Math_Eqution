from tkinter import *
import tkinter.messagebox
import math
import random
import time

widget_1 = Tk() #Widget
widget_1.title('Graphic user interface')
widget_1.geometry("500x500")#+0+0

menus = Menu()
widget_1.config(menu=menus)

def about(): #Clcik setting > about
    tkinter.messagebox.showinfo('Information','Narongkorn')

def exit_program():#Close program
    confirm = tkinter.messagebox.askquestion('Confirm','Confirm to close program')
    if confirm == 'yes':
        widget_1.destroy()

menu_list = Menu()
menu_list.add_command(label='File')
menu_list.add_command(label='New File')
menu_list.add_command(label='Open File')
menu_list.add_command(label='Save File')
menu_list.add_command(label='About',command=about)
menu_list.add_command(label='Exit',command=exit_program)

#Add menu
menus.add_cascade(label='Setting',menu = menu_list)

Label(widget_1,text= 'Game Generate Random Equation Speed run' ,fg='black',font=10).pack()

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
    

def num_1(last_num):#last_num

    num_1 = random.randint(1,last_num)
    #print(num_1)
    return num_1

def num_2(last_num):#

    num_2 = random.randint(1,last_num)
    #print(num_2)
    return num_2

def operation(level):#
    operator = ['+','-','*','/','^','fac']
    
    if level == 1:
        random_op = random.randint(0,2)
        final_op = (operator[random_op])
    if level == 2:
        random_op = random.randint(0,3)
        final_op = (operator[random_op])
    if level >= 5:
        random_op = random.randint(0,4)
        final_op = (operator[random_op])
    if level >= 8:
        random_op = random.randint(0,5)
        final_op = (operator[random_op])
    #print(final_op)
    return final_op

point = 0 #Static
def equation(num1,num2,op):
    
    if op == '+':
        Label(text=f'Question : {num1} + {num2}').pack()
        ans = num1 + num2
    if op == '-':
        Label(text=f'Question : {num1} - {num2}').pack()
        ans = num1 - num2
    if op == '*':
        Label(text=f'Question : {num1} * {num2}').pack()
        ans = num1 * num2
    if op == '/':
        if num2 == 0:
            temp = random.randint(1,num1)
            num2 = temp
        Label(text=f'Question : {num1} ÷ {num2}').pack()
        ans = num1 / num2
    if op == '^':
        if num2 >= 5:
            temp = random.randint(2,4)
            num2 = temp
        Label(text=f'Question : {num1} ^ {num2}').pack()
        ans = num1 ** num2
    if op == 'fac':
        if num1 > 10:
            temp = random.randint(1,10)
            num1 = temp
        print(f'Question : Factorial {num1}')
        ans = math.factorial(num1)

    return ans

final_point = 0

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
            print('This is not an number')
    
    if final_ans == ans:
        print('You got correct answer')

        final_point = final_point + 200
        
    else:
        print(f'Wong answer, and correct answer is {ans}')

        final_point = final_point - 100
        
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
        level = 1
    if point == 500:
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

for x in range(1,100): 
    last_number = 10
    num1 = num_1(last_number)
    num2 = num_2(last_number)
    op = operation(5) #Return ค่าจาก final_level
    final_answer = equation(num1,num2,op)
    final_points =  check_ans(final_answer)
    if final_point <= 0:
        print('Game Over !')
        break
    if final_point == 7000:
        break
    """if final_time == 0:
        break"""
    LEVEL = leveling(final_points)
    

def button():
    final_ans = enter_answer.get()
    print(final_ans)
    return None

enter_answer = Entry(widget_1,width=20,).pack()

Button(widget_1,text='enter',command=button).pack()

widget_1.mainloop() #Run program loop