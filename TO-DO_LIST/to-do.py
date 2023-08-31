from tkinter import *
from tkinter.font import Font


root = Tk()
root.title('CODSOFT - To-Do Application')
root.iconbitmap()
root.geometry("700x500")

# define my fonts
my_font = Font(
    family='Bernard MT Condensed',
    size=30,
    weight='normal'
)

# create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# create list of todos
my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg= "SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground= "#a6a6a6",
    activestyle="none"
)
my_list.pack(side="left", fill="both")

# create default list
dummy_list = ["Play football", "Go to church", "Have my lunch", "Call my fiance", "I have a dinner date", "Create a website for a ecommerce", "Go and pick up my International Passport",]

# Add the default list to listbox
for item in dummy_list:
    my_list.insert(END, item)

# create functions

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def delete_item():
    my_list.delete(ANCHOR)

def cross_out_item():
    # cross out item
    my_list.itemconfig(
        my_list.curselection(),
        #fg="#0cb70b",
        fg="#dedede"      
    )
    # get rid of selected item
    my_list.selection_clear(0, END)

def uncross_out_item():
    # uncross out item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"
    )
    # get rid of selected item
    my_list.selection_clear(0, END)
    
def delete_crossed_item():
    # count = 0
    # while count < my_list.size():
    #     if (my_list.itemcget(count, "fg")) == "#dedede":
    #         my_list.delete(my_list.index(count))

    # count += 1
    
        


# create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side="right", fill="both")


# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar)
my_scrollbar.config(command=my_list.yview)

# create entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 30))
my_entry.pack(pady=20)

# create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Add some buttons 
delete_button = Button(button_frame, text= "Delete Item", command=delete_item)
add_button = Button(button_frame, text= "Add Item", command=add_item)
cross_out_button = Button(button_frame, text="Cross-Out Item", command=cross_out_item)
uncross_out_button = Button(button_frame, text="Uncross-Out Item", command=uncross_out_item)
delete_crossed_button = Button(button_frame, text="Delete Crossed-Out Item", command=delete_crossed_item)

delete_button.grid(row=0, column=0, padx=20)
add_button.grid(row=0, column=1, padx= 20)
cross_out_button.grid(row=0, column=2, padx= 20)
uncross_out_button.grid(row=0, column=3, padx= 20)
delete_crossed_button.grid(row=0, column=4, padx=20)


root.mainloop()
