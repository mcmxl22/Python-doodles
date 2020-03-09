#!/usr/bin/env python3
"""
calculator version 1.1
Python 3.7
"""

from tkinter import *

# Define the window.
window = Tk()
window.geometry("133x134")
window.title("Calculator")
window.configure(background="black")

text_in = StringVar()
operator = ""

def set_number(number):
    """Enter the equation."""
    global operator
    operator=operator+str(number)
    text_in.set(operator)


def equals():
    """Adds"""
    global operator
    solve = str(eval(operator))

    if "+" in operator:
        add = solve
        text_in.set(add)
        operator = ""

    elif "-" in operator:
        sub = solve
        text_in.set(sub)
        operator = ""

    elif "*" in operator:
        mult = solve
        text_in.set(mult)
        operator = ""

    elif "/" in operator:
        div = solve
        text_in.set(div)
        operator = ""
    
    else:
        return


def clear():
    """Clears the text box."""
    text_in.set("")


# Define the text entery box.
text_entry = Entry(window, textvar=text_in, width=129, bg="black", fg="white") 
text_entry.place(x=2, y=2)

# Define the buttons.
# Row 1
one_button = Button(window, text="1", command=lambda:set_number(1), width=3, bg="black", fg="white")
one_button.place(x=2, y=23)

two_button = Button(window, text="2", command=lambda:set_number(2), width=3, bg="black", fg="white")
two_button.place(x=35, y=23)

three_button = Button(window, text="3", command=lambda:set_number(3), width=3, bg="black", fg="white")
three_button.place(x=68, y=23)

addition_button = Button(window, text="+", command=lambda:set_number("+"), width=3, bg="black", fg="white")
addition_button.place(x=101, y=23)

# Row 2
four_button = Button(window, text="4", command=lambda:set_number(4), width=3, bg="black", fg="white")
four_button.place(x=2, y=51)

five_button = Button(window, text="5", command=lambda:set_number(5), width=3, bg="black", fg="white")
five_button.place(x=35, y=51)

six_button = Button(window, text="6", command=lambda:set_number(6), width=3, bg="black", fg="white")
six_button.place(x=68, y=51)

subtraction_button = Button(window, text="-", command=lambda:set_number("-"), width=3, bg="black", fg="white")
subtraction_button.place(x=101, y=51)

# Row 3
seven_button = Button(window, text="7", command=lambda:set_number(7), width=3, bg="black", fg="white") 
seven_button.place(x=2, y=79)

eight_button = Button(window, text="8", command=lambda:set_number(8),  width=3, bg="black", fg="white")
eight_button.place(x=35, y=79)

nine_button = Button(window, text="9", command=lambda:set_number(9), width=3, bg="black", fg="white")
nine_button.place(x=68, y=79)

multiply_button = Button(window, text="*", command=lambda:set_number("*"), width=3, bg="black", fg="white")
multiply_button.place(x=101, y=79)

# Row 4
zero_button = Button(window, text="0", command=lambda:set_number(0), width=3, bg="black", fg="white")
zero_button.place(x=2, y=107)

clear_button = Button(window, text="C", command=clear, width=3, bg="black", fg="white")
clear_button.place(x=68, y=107)

clear_button = Button(window, text="/", command=lambda:set_number("/"), width=3, bg="black", fg="white")
clear_button.place(x=101, y=107)

equals_button = Button(window, text="=", command=equals, width=3, bg="black", fg="white")
equals_button.place(x=35, y=107)


window.mainloop()
