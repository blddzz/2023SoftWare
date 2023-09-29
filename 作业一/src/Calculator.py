import tkinter as tk
from tkinter import ttk
from Calculation import *
import os

list=[]
#计算
def evaluate_expression():
    try:
        list.clear()
        deal=Calculation()
        expression = result_num.get()
        result = deal.evaluate(expression)
        result_num.set(result)
        list.append(str(result))
    except Exception as e:
        result_num.set("Error")
#添加
def add_to_expression(char):
    list.append(char)
    result_num.set(result_num.get()+char)


#清除    
def clear():
    list.clear()
    result_num.set('')

# 退格
def back():
    result1=result_num.get()
    result1=result1[:-len(list.pop())]
    result_num.set(result1)
    

tcl_file_path = os.path.join(os.path.dirname(__file__), "azure.tcl")
data_folder_path = os.path.join(os.path.dirname(__file__), "theme")
root = tk.Tk()
root.title("Calculator")
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)
result_num=tk.StringVar()
result_num.set('')
tk.Label(big_frame,
         textvariable=result_num,height=2,width=40,justify=tk.LEFT,anchor=tk.SE,font=(20)
         ).grid(row=1,column=1,columnspan=6)


# 创建按钮
buttons = [
    ("sin", 2, 1, "sin("),("^", 2, 2, "^"),("AC",2,3, None), ("AC", 2, 4, None), ("Ba", 2, 5, None),("ck", 2, 6, None),
    ("cos", 3, 1, "cos("),("√", 3, 2, "√"), ("(", 3, 3, "("), (")", 3, 4, ")"), ("mod", 3, 5, "%"), ("÷", 3, 6, "÷"),
    ("tan", 4, 1, "tan("),("!", 4, 2, "!"), ("7", 4, 3, "7"), ("8", 4, 4, "8"), ("9", 4, 5, "9"), ("x", 4, 6, "x"),
    ("asin", 5, 1, "asin("),("ln", 5, 2, "ln("), ("4", 5, 3, "4"), ("5", 5, 4, "5"),("6", 5, 5, "6"), ("-", 5, 6, "-"),
    ("acos", 6, 1, "acos("),("lg", 6, 2, "lg("), ("1", 6, 3, "1"), ("2", 6, 4, "2"),("3", 6, 5, "3"), ("+", 6, 6, "+"),
    ("atan", 7, 1, "atan("),("π", 7, 2, "π"), ("e", 7, 3, "e"), ("0", 7, 4, "0"), (".", 7, 5, "."), ("=", 7, 6, None)
]

for (text, row, col, char) in buttons:
    if(char==None):
        continue
    button = ttk.Button(big_frame,text=text, width=4, command=lambda c=char: add_to_expression(c))
    button.grid(row=row, column=col, padx=3, pady=2, sticky="nsew")


# 创建退格按钮
back_button = ttk.Button(big_frame, text="Back",command=back)
back_button.grid(row=2, column=5 ,columnspan=2, padx=3, pady=2, sticky="nsew")


# 创建清除按钮
clear_button = ttk.Button(big_frame, text="AC",command=clear)
clear_button.grid(row=2, column=3 ,columnspan=2, padx=3, pady=2, sticky="nsew")

#创建等号按钮
equals_button = ttk.Button(big_frame, text="=",width=4,command=evaluate_expression)
equals_button.grid(row=7, column=6 , padx=3, pady=2, sticky="nsew")

root.tk.call("source", tcl_file_path)
root.tk.call("set_theme", "light")
root.mainloop()
