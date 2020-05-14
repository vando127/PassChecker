import tkinter as Tk
import checker

window = Tk.Tk()
window.wm_title("PassChecker")
window.wm_minsize(width=500, height=90)


def check_it():
    checked = checker.main([text.get()])
    l3 = Tk.Label(window, text="text")
    l3.grid(row=3, column=0)
    l3["text"] = checked


l2 = Tk.Label(window, text='Enter the password on the box bellow!')
l2.grid(row=1, column=0)



text = Tk.StringVar()
e1 = Tk.Entry(window, textvariable=text, width=50)
e1.grid(row=2, column=0)


b1 = Tk.Button(window, text='Check It!', width=12, command=check_it)
b1.grid(row=2, column=3)


window.mainloop()
