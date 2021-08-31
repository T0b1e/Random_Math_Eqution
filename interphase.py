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
        Label(widget_1,text = f'Question : {num1} + {num2}',fg='black',font=5).pack()
        print(f'Question : {num1} + {num2}')
        ans = num1 + num2
    if op == '-':
        print(f'Question : {num1} - {num2}')
        Label(widget_1,text = f'Question : {num1} - {num2}',fg='black',font=5).pack()
        ans = num1 - num2
    if op == '*':
        print(f'Question : {num1} * {num2}')
        Label(widget_1,text = f'Question : {num1} x {num2}',fg='black',font=5).pack()
        ans = num1 * num2
    if op == '/':
        print(f'Question : {num1} ÷ {num2}')
        Label(widget_1,text = f'Question : {num1} ÷ {num2}',fg='black',font=5).pack()
        ans = num1 / num2

    return ans

"""def check_ans(ans):
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

    return point"""

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

"""def no():
    for number in range(0,5):
        ans = equation(num_1(),num_2(),operation())
        answer = check_ans(ans)
        #print(answer)
no()"""

equation(num_1(),num_2(),operation())
#Label(widget_1,text= equation(num_1(),num_2(),operation()) ,fg='black',font=10).pack()

recieve_ans = Entry(widget_1,width= 40).pack()

widget_1.mainloop() #Run program loop