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
from resumestructure import ResumeStructure
import menu_options as mo

def main():
    root = tk.Tk()
    root.title("Resume Builder")
    root.minsize(width = 1000, height = 1000)
    max_width = root.winfo_screenwidth()
    max_height = root.winfo_screenheight()
    root.maxsize(width = max_width, height = max_height)

    # Create frame to hold scrollbar and input frames
    main_frame = tk.Frame(root, bg = "yellow")
    main_frame.pack(fill = tk.BOTH, expand = True, padx = 5, pady = 5)

    # Create canvas to hold frame for input frames
    canvas = tk.Canvas(main_frame, bg = "purple")
    canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

    # Create scrollbar
    scrollbar = tk.Scrollbar(main_frame, orient = tk.VERTICAL, command = canvas.yview)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

    # Configure scrollbar to the canvas
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    # Create frame to hold all inputs
    resume = ResumeStructure(canvas)

    # Add input frame to a window in canvas
    canvas_window = canvas.create_window((0, 0), window = resume.frame, anchor = 'nw')
    canvas.bind('<Configure>', lambda e: canvas.itemconfig(canvas_window, width=canvas.winfo_width()))

    menubar = tk.Menu(root)
    file = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file)
    file.add_command(label="New File", command=lambda: mo.new_file(resume))
    file.add_command(label="Save As", command=lambda: mo.save_as(resume))
    file.add_command(label="Save", command=lambda: mo.save(resume))


    root.config(menu=menubar)
    root.mainloop()


# Update scrollable area for dynamically added frames
def update_scrollable_region(root, canvas):
    root.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))




if __name__ == "__main__":
    main()