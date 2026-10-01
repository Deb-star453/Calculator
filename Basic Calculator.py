# Making root window
import tkinter as tk
root=tk.Tk()
root.title("Basic Calculator")
root.geometry("400x400")
# Making user defined functions for the buttons
def multiply(): 
# Get the numbers from entry boxes
    number1=float(num1.get())
    number2=float(num2.get())
# Perform the operation
    answer=number1*number2
# Print answer
    result.config(text="Result: "+str(answer))
def add():
    number1=float(num1.get())
    number2=float(num2.get())
    answer=number1+number2
    result.config(text="Result: "+str(answer))
def subtract():
    number1=float(num1.get())
    number2=float(num2.get())
    answer=number1-number2
    result.config(text="Result: "+str(answer))
def divide():
    number1=float(num1.get())
    number2=float(num2.get())
    answer=number1/number2
    result.config(text="Result: "+str(answer))
# Make a heading
heading=tk.Label(root,text="Basic Calculator",font=("Georgia",20,"bold"))
heading.place(x=93,y=90)
# Make entries for the user to input 2 numbers
num1=tk.Entry(root,font=("Georgia",10))
num1.pack(pady=15)
num2=tk.Entry(root,font=("Georgia",10))
num2.pack(pady=5)
# Create a label for result
result = tk.Label(root, text="Result: ", font=("Georgia", 12, "bold"))
result.place(x=150, y=300)
# Make and function all the buttons
mutiplybutton=tk.Button(root,text="multiply",font=("Georgia",14),command=multiply)
mutiplybutton.place(x=190,y=150)
addbutton=tk.Button(root,text="add",font=("Georgia",14),command=add)
addbutton.place(x=125,y=150)
subtractbutton=tk.Button(root,text="subtract",font=("Georgia",14),command=subtract)
subtractbutton.place(x=98, y=210)
dividebutton=tk.Button(root,text="divide",font=("Georgia",14),command=divide)
dividebutton.place(x=198,y=210)
root.mainloop()