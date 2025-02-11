

# Calculator Project in Python :

from tkinter import *
import random
# Activate the tkinter module and screen setting and adding shape of calculator
bg = ["#FF5733","#8E44AD","#1ABC9C"]
randomly = random.choice(bg)

window = Tk()
window.title("Python Caluculator")
window.config(width=100,height=200,bg=randomly)
# By functions activate the buttons
def cancel_button():
    cerrent_text = user_entry.get()
    if len(cerrent_text) >0:
        user_entry.delete(len(cerrent_text) - 1 ,END)

def result():
  result_num = user_entry.get()
  try:
    user_entry.delete(0,END)
    user_entry.insert(END,eval(result_num))
  except:
      user_entry.delete(0,END)
      user_entry.insert(END,"ERROR")
def clear_button():
    user_entry.delete(0, END)

def plus_button():
    user_entry.insert(END,"+")

def minus_button():
    user_entry.insert(END,"-")
    
def multiply_button():
    user_entry.insert(END,"*")
    
def divide_button():
    user_entry.insert(END,"/")
    
def seven_number():
    user_entry.insert(END,"7")

def four_number():
    user_entry.insert(END,"4")
    
def one_number():
    user_entry.insert(END,"1")
    
def eight_number():
    user_entry.insert(END,"8")
    
def five_number():
    user_entry.insert(END,"5")
    
def two_number():
    user_entry.insert(END,"2")
    
def nine_number():
    user_entry.insert(END,"9")
    
def six_number():
    user_entry.insert(END,"6")

def three_number():
    user_entry.insert(END,"3")

def zero_number():
    user_entry.insert(END,"0")

# Use the Buttons of Numbers and its positions

canvas = Canvas(width=50,height=200,bg=randomly,highlightthickness=0)
canvas.grid(column=0,row=0)

user_color = ['red','green','blue']
ramdomly = random.choice(user_color)
# user input numbers or Answer to the user
user_entry = Entry(window,font=("Arial",24,"bold"),width=18,borderwidth=5,fg=ramdomly)
user_entry.grid(column=0,row=0,columnspan=3,padx=10,pady=10)


cancel = Button(text="❌", font=("Arial", 15, "bold"), width=5, height=1,command=cancel_button)
cancel.grid(column=3, row=0, padx=5, pady=5)

seven = Button(text=7, font=("Arial",15,"bold"),width=5,height=2,command=seven_number,fg="red")
seven.grid(row=1, column=0, padx=5, pady=5)

eight = Button(text=8, font=("Arial", 15, "bold"), width=5, height=2,command=eight_number,fg="green")
eight.grid(row=1, column=1, padx=5, pady=5)

nine = Button(text=9, font=("Arial", 15, "bold"), width=5, height=2,command=nine_number,fg="blue")
nine.grid(row=1, column=2, padx=5, pady=5)

four = Button(text=4, font=("Arial", 15, "bold"), width=5, height=2,command=four_number,fg="red")
four.grid(row=2, column=0, padx=5, pady=5)

five = Button(text=5, font=("Arial", 15, "bold"), width=5, height=2,command=five_number,fg="green")
five.grid(row=2, column=1, padx=5, pady=5)

six = Button(text=6, font=("Arial", 15, "bold"), width=5, height=2,command=six_number,fg="blue")
six.grid(row=2, column=2, padx=5, pady=5)

one = Button(text=1, font=("Arial", 15, "bold"), width=5, height=2,command=one_number,fg="red")
one.grid(row=3, column=0, padx=5, pady=5)

two = Button(text=2, font=("Arial", 15, "bold"), width=5, height=2,command=two_number,fg="green")
two.grid(row=3, column=1, padx=5, pady=5)

three = Button(text=3, font=("Arial", 15, "bold"), width=5, height=2,command=three_number,fg="blue")
three.grid(row=3, column=2, padx=5, pady=5)

zero = Button(text=0, font=("Arial", 15, "bold"), width=5, height=2,command=zero_number,fg="orange")
zero.grid(row=4, column=1, padx=5, pady=5)

equal = Button(text="=",font=("Arial",15,"bold"),width=5,height=2,command=result,fg="gray")
equal.grid(row=4,column=2,padx=5,pady=5)

clear= Button(text="Clear",font=("Arial",15,"bold"),width=5,height=2,command=clear_button,fg="lightgreen")
clear.grid(row=4,column=0,padx=5,pady=5)

# signs Buttons

plus = Button(text="+",font=("Arial",15,"bold"),width=5,height=2,command=plus_button)
plus.grid(row=1,column=3,padx=5,pady=5)

minus = Button(text="-",font=("Arial",15,"bold"),width=5,height=2,command=minus_button)
minus.grid(row=2,column=3,padx=5,pady=5)

multiply = Button(text="x",font=("Arial",15,"bold"),width=5,height=2,command=multiply_button)
multiply.grid(row=3,column=3,padx=5,pady=5)

divide = Button(text="÷",font=("Arial",15,"bold"),width=5,height=2,command=divide_button)
divide.grid(row=4,column=3,padx=5,pady=5)


window.mainloop()