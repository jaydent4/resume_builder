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

        # Create title entry
        self.title_label = tk.Label(self.frame, text = "Title")
        
        self.title_entry = tk.Entry(self.frame, textvariable = self.title)

        # Create an optional list input
        self.list_label = tk.Label(self.frame, text = "List (Optional)")
        self.list = tk.Text(self.frame, width = 10, height = 5)

        # Create button for sections
        self.sections_label = tk.Label(self.frame, text = "Sections")
        self.add_section_button = tk.Button(self.frame, text = "Add Section", command = lambda: self.add_section(self.frame))
    
    def insert_category(self, grid_row, grid_col):
        
        # Place frame in the specified position
        self.frame.grid(row = grid_row, column = grid_col, padx = 10, pady = 10)

        # Place all other entries within the frame
        self.title_label.grid(row = 0, column = 0)
        self.title_entry.grid(row = 1, column = 0)
        self.list_label.grid(row = 2, column = 0)
        self.list.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.sections_label.grid(row = 4, column = 0)
        self.add_section_button.grid(row = 5, column = 0)

        self.add_section(self.frame)
 

    def add_section(self, frame):
        self.new_section = Section(frame)
        self.new_section.insert()
        self.sections.append(self.new_section)
        self.update_position()
    
    def update_position(self):
        return
