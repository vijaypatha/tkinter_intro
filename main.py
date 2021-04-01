import tkinter

window = tkinter.Tk()

window.title("My first GUI")
window.minsize(width=500, height=500)

#Label
label = tkinter.Label(text="Im a label", font=("Arial", 24, "bold"))
label.pack() # puts the text in the screen



window.mainloop() # keeps the screen running