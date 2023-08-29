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
stuffs = ["Play football", "Go to church", "Have my lunch", "Call my fiance", "I have a dinner date", "Create a website for a ecommerce", "Go and pick up my International Passport",]

# Add the default list to listbox
for item in stuffs:
    my_list.insert(END, item)

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
delete_button = Button(button_frame, text= "Delete Item")
add_button = Button(b)

root.mainloop()
