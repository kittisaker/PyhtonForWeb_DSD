# GUI receive data

from tkinter import *

window = Tk()

window.geometry("250x120")
window.resizable(width=0, height=0)
window.title("RECORD")

def get_data():
    p = int(E1.get())
    u = int(E2.get())
    print(p, u)

L1 = Label(window, text = "Price : ")   
L1.place(x=10, y=10)
E1 = Entry(window)
E1.place(x=50, y=10)

L2 = Label(window, text = "UNIT : ")   
L2.place(x=10, y=50)
E2 = Entry(window)
E2.place(x=50, y=50)

B1 = Button(window, text="Submit", command=get_data)
B1.place(x=80, y=80)
window.mainloop()