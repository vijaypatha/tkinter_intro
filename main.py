from tkinter import *

window = Tk()

window.title("My first GUI")
window.minsize(width=500, height=500)

# Label
label = Label(text="Im a label", font=("Arial", 24, "bold"))
label.pack()  # puts the text in the screen

label["text"] = "New Text"
label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    # label.config(text="button got clicked")
    label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
input.get()

window.mainloop()  # keeps the screen running
