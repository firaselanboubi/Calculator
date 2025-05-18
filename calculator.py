import tkinter as tk

wind = tk.Tk()

wind.title("calculator")
wind.config(bg="white")
wind.geometry("400x500")
wind.resizable(False, False)

title = tk.Label(wind, text="calculator", font=("Arial", 20),bg="white", fg="black")
title.place(x=0, y=0, width=400, height=50)

box = tk.Entry(wind,bd=2, font=("Arial" ,20))
box.place(x=50, y=60, width=300, height=30)

def button_click(button_number):
    current_numbre = box.get()
    box.delete(0, tk.END)
    box.insert(0, str(current_numbre) + str(button_number))

def button_clear():
    box.delete(0, tk.END)

def button_add():
    firt_numbre_str = box.get()
    global firt_numbre
    global operation
    firt_numbre = float(firt_numbre_str)
    operation = "+"
    box.delete(0, tk.END)

def button_subtract():
    firt_numbre_str = box.get()
    global firt_numbre
    global operation
    firt_numbre = float(firt_numbre_str)
    operation = "-"
    box.delete(0, tk.END)

def button_multiply():
    firt_numbre_str = box.get()
    global firt_numbre
    global operation
    firt_numbre = float(firt_numbre_str)
    operation = "x"
    box.delete(0, tk.END)

def button_devide():
    firt_numbre_str = box.get()
    global firt_numbre
    global operation
    firt_numbre = float(firt_numbre_str)
    operation = "/"
    box.delete(0, tk.END)

def button_equal():
    second_number = float(box.get())
    box.delete(0, tk.END)

    if operation == "+":
        box.insert(0, firt_numbre + second_number)
    elif operation == "-":
        box.insert(0, firt_numbre - second_number)
    elif operation == "x":
        box.insert(0, firt_numbre * second_number)
    elif operation == "/":
        box.insert(0, firt_numbre / second_number)



button_add = tk.Button(wind, text="+", bd=1, bg="white", font=("Arial", 20), fg="black", command=button_add)
button_subtract = tk.Button(wind, text="-", bd=1, bg="white", font=("Arial", 20), fg="black", command=button_subtract)
button_multiply = tk.Button(wind, text="x", bd=1, bg="white", font=("Arial", 20), fg="black", command=button_multiply)
button_devide = tk.Button(wind, text="/", bd=1, bg="white", font=("Arial", 20), fg="black", command=button_devide)
button_equal = tk.Button(wind, text="=", bd=1, bg="white", font=("Arial", 20), fg="black", command=button_equal)
button_clear = tk.Button(wind, text="C", bd=1, bg="white", font=("Arial", 20), fg="black", command=button_clear)

button_1 = tk.Button(wind, text="1",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(1))
button_2 = tk.Button(wind, text="2",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(2))
button_3 = tk.Button(wind, text="3",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(3))
button_4 = tk.Button(wind, text="4",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(4))
button_5 = tk.Button(wind, text="5",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(5))
button_6 = tk.Button(wind, text="6",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(6))
button_7 = tk.Button(wind, text="7",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(7))
button_8 = tk.Button(wind, text="8",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(8))
button_9 = tk.Button(wind, text="9",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(9))
button_0 = tk.Button(wind, text="0",font=("Arial", 20), bd=1, bg="white", fg="black", command=lambda: button_click(0))
button_1.place(x=0, y=100, width=100, height=100)
button_2.place(x=100, y=100, width=100, height=100)
button_3.place(x=200, y=100, width=100, height=100)
button_4.place(x=0, y=200, width=100, height=100)
button_5.place(x=100, y=200, width=100, height=100)
button_6.place(x=200, y=200, width=100, height=100)
button_7.place(x=0, y=300, width=100, height=100)
button_8.place(x=100, y=300, width=100, height=100)
button_9.place(x=200, y=300, width=100, height=100)
button_0.place(x=100, y=400, width=100, height=100)

button_clear.place(x=0, y=400, width=100, height=100)
button_equal.place(x=200, y=400, width=100, height=100)
button_add.place(x=300, y=100, width=100, height=100)
button_subtract.place(x=300, y=200, width=100, height=100)
button_multiply.place(x=300, y=300, width=100, height=100)
button_devide.place(x=300, y=400, width=100, height=100)



wind.mainloop()
