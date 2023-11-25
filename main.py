import os
from tkinter import *
from tkinter import ttk

def RunTests():
    print("Tests")

os.system("python3 src\\1_1.py")
root = Tk()
root.title("Advent of Code 2023")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Style
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="All Tests", command=RunTests).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()