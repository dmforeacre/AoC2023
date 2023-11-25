import os
from pathlib import Path
from functools import partial
from tkinter import *
from tkinter import ttk

def RunTest(testPath):
    os.system("python3 src\\" + testPath.name)

def RunAllTests(testFiles):
    for f in testFiles:
        RunTest(f)

srcPath = Path("src/")
testFiles = []
root = Tk()
root.title("Advent of Code 2023")
frm = ttk.Frame(root, padding=10)
frm.grid(padx=10,pady=10)
ttk.Style
numRows = 0
for x in srcPath.iterdir():
    testFiles.append(x)
    testFunc = partial(RunTest, x)
    ttk.Label(frm, text="Run "+x.name[:-3], padding=5).grid(column=0, row=numRows)
    ttk.Label(frm, text="   ", padding=5).grid(column=1, row=numRows)
    ttk.Button(frm, text="Run Test", command= testFunc, padding=5).grid(column=2, row=numRows)
    numRows += 1
allTestsFunc = partial(RunAllTests, testFiles)
ttk.Button(frm, text="All Tests", command= allTestsFunc, padding=5).grid(column=2, row=numRows)
ttk.Button(frm, text="Quit", command=root.destroy, padding=5).grid(column=0, row=numRows)
root.mainloop()