import section
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class Category:
    def __init__(self, root):

        self.title = tk.StringVar()
        self.sec = []

        # Create a frame
        self.frame = tk.Frame(root, bd = 2, relief = "raised")
        self.frame.pack(padx = 10, pady = 10, fill = 'x', expand = True)

        # Create title entry
        self.title_entry = tk.Entry(self.frame, textvariable = self.title)
        self.title_entry.pack(anchor = 'nw', padx = 5, pady = (10, 5))
    
    def add_section(category):
        #todo: add function to append a section to list
        return
