# Check the version of Python
import sys
v = sys.version
if int(v[0]) >= 3:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog as fd
else:
    raise Exception(f"Python 3.X or higher is required. You currently have Python {v}")

def main():
    root = tk.Tk()
    root.title("Resume Builder")
    root.minsize(width = 400, height = 400)
    root.maxsize(width = 1000, height = 1000)
    
    # Step 2: Create frames to hold the Text widgets
    frame1 = tk.Frame(root)
    frame1.pack(fill=tk.BOTH, expand=True)

    frame2 = tk.Frame(root)
    frame2.pack(fill=tk.BOTH, expand=True)

    # Step 3: Add Text widgets to each frame
    text_widget1 = tk.Text(frame1, height=5, width=40)
    text_widget1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    text_widget2 = tk.Text(frame2, height=5, width=40)
    text_widget2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # text = tk.Text(root, width = 400, height = 400)
    # text.pack()

    # text2 = tk.Text(root, width = 100, height = 100)
    # text2.pack()

    # mb = tk.Menu(root)
    # filemenu = tk.Menu(mb)
    # filemenu.add_command(label = "New File", command = lambda: new_file(text))
    # filemenu.add_command(label = "Save", command = lambda: save(text))
    # filemenu.add_command(label = "Save As", command = lambda: save_as(text))
    # filemenu.add_command(label = "Open File", command = lambda: open_file(text))
    # filemenu.add_command(label = "Quit", command = lambda: root.quit(text))
    # mb.add_cascade(label = "File", menu = filemenu)

    # root.config(menu = mb)
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