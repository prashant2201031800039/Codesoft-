"""
This is a simple calculator with basic arithmetic
operations. Prompts users to input two numbers
and an operation choice. Perform the calculation,
before displaying the result
"""


from tkinter import *

# configure the tkinter
# components
app = Tk()
app.title("Simple Calculator by Charles Lughas")
app.iconbitmap()
app.config(background="#54AB80")


# colors pallette
# background=#54AB80
# buttons=#AB8054
# operations=#8054AB

# globally declare the expression variable
expression = ""

# functions
##########
def add_button():
    pass


# create entry for input & output
entry_field = Entry(app,
                width=35,
                justify="right",
                borderwidth=5
            )
# make the entry field into grid
# giving it a columnspan to address for
# other columns in the other rows
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# create buttons for each numbers between 0-9
button_1 = Button(app, text="1", padx=40, pady=20, command=add_button)
button_2 = Button(app, text="2", padx=40, pady=20, command=add_button)
button_3 = Button(app, text="3", padx=40, pady=20, command=add_button)
button_4 = Button(app, text="4", padx=40, pady=20, command=add_button)
button_5 = Button(app, text="5", padx=40, pady=20, command=add_button)
button_6 = Button(app, text="6", padx=40, pady=20, command=add_button)
button_7 = Button(app, text="7", padx=40, pady=20, command=add_button)
button_8 = Button(app, text="8", padx=40, pady=20, command=add_button)
button_9 = Button(app, text="9", padx=40, pady=20, command=add_button)
button_0 = Button(app, text="0", padx=40, pady=20, command=add_button)
button_add = Button(app, text="+", padx=40, pady=20, command=add_button)
button_subtract = Button(app, text="-", padx=40, pady=20, command=add_button)
button_divide = Button(app, text="/", padx=41, pady=20, command=add_button)
button_multiply = Button(app, text="x", padx=39, pady=20, command=add_button)
button_clear = Button(app, text="=", padx=89, pady=20, command=add_button)
button_equal = Button(app, text="clear", padx=79, pady=20, command=add_button)


# arrange the button in the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=6, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_clear.grid(row=6, column=1, columnspan=2)


# run the tkinter application
app.mainloop()