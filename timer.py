from tkinter import *

time = 0

def timer(label):
    global time
    time += 1
    Label.config(text= str(time))
    Label.after(1000, timer, Label)

root = Tk()
root.title('Timer')

label = Label(root,text='0').pack()

timer(label)

root.mainloop()