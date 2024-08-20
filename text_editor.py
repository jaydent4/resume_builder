# Check the version of Python
import sys
v = sys.version
if int(v[0]) >= 3:
    import tkinter as tk
    from tkinter import filedialog as fd
else:
    raise Exception(f"Python 3.X or higher is required. You currently have Python {v}")

from category import Category
from section import Section

def main():
    root = tk.Tk()
    root.title("Resume Builder")
    root.minsize(width = 400, height = 400)
    root.maxsize(width = 1000, height = 1000)

    # Create frame to hold scrollbar and input frames
    main_frame = tk.Frame(root)
    main_frame.pack(fill = tk.BOTH, expand = True)

    # Create canvas to hold frame for input frames
    canvas = tk.Canvas(root)
    canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

    # Create scrollbar
    scrollbar = tk.Scrollbar(main_frame, orient = tk.VERTICAL, command = canvas.yview)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

    # Configure scrollbar to the canvas
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', lambda x: canvas.configure(scrollregion = canvas.bbox("all")))

    # Create frame to hold all inputs
    input_frame = tk.Frame(canvas)
    input_frame.pack(fill = tk.BOTH, expand = True)

    # Add input frame to a window in canvas
    canvas.create_window((0, 0), window = input_frame, anchor = 'nw')

    cat = Category(input_frame)

    root.mainloop()


# Create a new file; change name and delete current text
def new_file(text):
    global filename
    filename = "Untitled"
    text.delete(0.0, tk.END)

# Save current file 
def save(text):
    global filename
    t = text.get(0.0, tk.END)
    file = open(filename, 'w')
    file.write(t)
    file.close()

def save_as(text):
    # prompt to save each of the entries within a text file
    file = fd.asksaveasfile(mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, tk.END)
    t = t.rstrip()
    try:
        file.write(t)
    except: # should never reach this point
        tk.showerror(Title="ERROR", message ="Unable to save file")

def open_file(text):
    f = fd.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, tk.END)
    text.insert(0.0, t)

if __name__ == "__main__":
    main()