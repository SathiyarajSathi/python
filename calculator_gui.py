import tkinter as tk

window = tk.Tk()
window.title("Calculator")

def number(no):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(no))

def add(sign):
    first_num=e.get()
    global ind
    global f_num
    ind = sign
    f_num = int(first_num)
    e.delete(0, tk.END)
def sub(sign):
    first_num=e.get()
    global ind
    global f_num
    ind = sign
    f_num = int(first_num)
    e.delete(0, tk.END)
def mul(sign):
    first_num=e.get()
    global ind
    global f_num
    ind = sign
    f_num = int(first_num)
    e.delete(0, tk.END)    
def div(sign):
    first_num=e.get()
    global ind
    global f_num
    ind = sign
    f_num = int(first_num)
    e.delete(0, tk.END)
def equal():
    second_num=e.get()
    e.delete(0, tk.END)
    if ind == "+":
        e.insert(0, f_num + int(second_num))     
    elif ind == "-":
        e.insert(0, f_num - int(second_num))
    elif ind == "*":
        e.insert(0, f_num * int(second_num))
    elif ind == "%":
        e.insert(0, f_num / int(second_num))
def clear():
    e.delete(0, tk.END)


# Number buttons    
e = tk.Entry(window, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
button1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: number("1"))
button2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: number("2"))
button3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: number("3"))
button4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: number("4"))
button5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: number("5"))
button6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: number("6"))
button7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: number("7"))
button8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: number("8"))
button9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: number("9"))
button0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: number("0"))
buttoneql = tk.Button(window, text="=", padx=40, pady=20, command=equal)
buttonclr = tk.Button(window, text="Clear", padx=40, pady=20, command=clear)
buttonadd = tk.Button(window, text="+", padx=40, pady=20, command=lambda: add("+"))
buttonsub = tk.Button(window, text="-", padx=40, pady=20, command=lambda: sub("-"))
buttonmul = tk.Button(window, text="x", padx=40, pady=20, command=lambda: mul("*"))
buttondiv = tk.Button(window, text="%", padx=40, pady=20, command=lambda: div("/"))

# button allign
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

buttonclr.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttoneql.grid(row=4, column=2)
buttonadd.grid(row=4, column=3)

buttonsub.grid(row=3, column=3)
buttonmul.grid(row=2, column=3)
buttondiv.grid(row=1, column=3)

window.mainloop()