from tkinter import *

window = Tk()

window.title("My first GUI")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)


def button_clicked():
    print("I got clicked")
    # label.config(text="button got clicked")
    label.config(text=input.get())


# TODO: Label Widget
label = Label(text="Im a label", font=("Arial", 24, "bold"))
# label.pack()  # puts the text in the screen
# label.place(x=100 , y=200) Precise coordinate
label.grid(column=0, row=0)

label["text"] = "New Text"
label.config(text="New Text")

# TODO: Button Widget
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# TODO: New Button Widget
new_button = Button(text="double click me")
new_button.grid(column=2, row=0)

# TODO: Entry Widget
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
input.get()

window.mainloop()  # keeps the screen running
