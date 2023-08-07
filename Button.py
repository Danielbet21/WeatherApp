from tkinter import *

base=Tk()
def click():
    label = Label(base,text = "i have clicked the button")
    label.pack()

button = Button(base,text="Push me if you DaRe!",padx = 50, pady=50, command = click,fg="red", bg="#000") 
#padx/y - reframe the button
#command - associate a function to a specific action
#fg - color the button's text
#bg - color the button's background 
button.pack()

base.mainloop()