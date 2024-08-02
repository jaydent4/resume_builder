# Check the version of Python
import sys
v = sys.version
if int(v[0]) >= 3:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog as fd
else:
    raise Exception(f"Python 3.X or higher is required. You currently have Python {v}")

# Create a new file; change name and delete current text
def new_file():
    global filename
    filename = "Untitled"
    text.delete(0.0, tk.END)

# Save current file 
def save():
    global filename
    t = text.get(0.0, tk.END)
    file = open(filename, 'w')
    file.write(t)
    file.close()

def save_as():
    file = fd.asksaveasfile(mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, tk.END)
    t = t.rstrip()
    try:
        file.write(t)
    except: # should never reach this point
        fd.showerror(Title="ERROR", message ="Unable to save file")

def open_file():
    f = fd.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, tk.END)
    text.insert(0.0, t)

root = tk.Tk()
root.title("Text Editor")
root.minsize(width = 400, height = 400)
root.maxsize(width = 1000, height = 1000)

text = tk.Text(root, width = 400, height = 400)
text.pack()

mb = tk.Menu(root)
filemenu = tk.Menu(mb)
filemenu.add_command(label = "New File", command = new_file)
filemenu.add_command(label = "Save", command = save)
filemenu.add_command(label = "Save As", command = save_as)
filemenu.add_command(label = "Open File", command = open_file)
filemenu.add_command(label = "Quit", command = root.quit)
mb.add_cascade(label = "File", menu = filemenu)

root.config(menu = mb)
root.mainloop()





