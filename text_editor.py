# Check the version of Python
import sys
v = sys.version
if int(v[0]) >= 3:
    from tkinter import ttk
    from tkinter import filedialog as fd
else:
    raise Exception(f"Python 3.X or higher is required. You currently have Python {v}")

# Create a new file; change name and delete current text
def new_file():
    global filename
    filename = "Untitled"
    text.delete(0.0, ttk.END)

def save():
    global filename
    t = text.get(0.0, END)
    file = open(filename, 'w')
    file.write(t)
    file.close()

def save_as():
    file = fd.asksaveasfile(mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, ttk.END)
    t = t.rstrip()
    try:
        file.write(t)
    except: # should never reach this point
        fd.showerror(Title="ERROR", message ="Unable to save file")

def openFile():
    f = fd.askopenfile(mode='r')

