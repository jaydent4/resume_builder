from section import Section
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class Category:
    def __init__(self, root):

        self.title = tk.StringVar()
        self.sections = []

        # Create a frame
        self.frame = tk.Frame(root, bd = 2, relief = "raised")
        self.frame.pack(padx = 10, pady = 10, fill = 'x', expand = True)

        # Create title entry
        self.title_label = tk.Label(self.frame, text = "Title")
        self.title_label.pack(anchor = "nw")
        self.title_entry = tk.Entry(self.frame, textvariable = self.title)
        self.title_entry.pack(anchor = 'nw', padx = 5, pady = (5, 10))

        # Create an optional list input
        self.list_label = tk.Label(self.frame, text = "List (Optional)")
        self.list_label.pack(anchor = 'w', padx = 5, pady = (5, 5))
        self.list = tk.Text(self.frame, width = 10, height = 5)
        self.list.pack(anchor = 'w', padx = 5, pady = (5, 10), fill = 'x', expand = True)


        # Create button for sections
        self.sections_label = tk.Label(self.frame, text = "Sections")
        self.sections_label.pack(anchor = 'w', padx = 5, pady = (5, 5))
        self.add_section_button = tk.Button(self.frame, text = "Add Section", command = lambda: self.add_section(self.frame))
        self.add_section_button.pack(anchor = 'w', padx = 5, pady = (5, 10))
    
    def add_section(self, frame):
        self.new_section = Section(frame, self.add_section_button)
        self.sections.append(self.new_section)
