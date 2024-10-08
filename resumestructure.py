from category import Category
import tkinter as tk

class ResumeStructure:
    def __init__(self, root):
        self.filename = "Untitled"

        # Initialize variables
        self.name = tk.StringVar()
        self.subheading = tk.StringVar()
        self.categories = []

        # Create a frame
        self.frame = tk.Frame(root, bg = "blue")

        # Create entry for name
        self.name_label = tk.Label(self.frame, text = "Name")
        self.name_entry = tk.Entry(self.frame, text = self.name)

        # Create entry for subheading
        self.subheading_label = tk.Label(self.frame, text = "Subheading")
        self.subheading_entry = tk.Entry(self.frame, text = self.subheading)
        # Create a button to add a category
        self.add_category_button = tk.Button(self.frame, text = "Add Category", command = lambda: self.add_category(self.frame))

        # Adjust frame grid
        for i in range(30):
            self.frame.grid_columnconfigure(i, weight = 1)
        
        # Add widgets to the frame
        self.name_label.grid(row = 0, column = 0)
        self.name_entry.grid(row = 0, column = 1)
        self.subheading_label.grid(row = 1, column = 0)
        self.subheading_entry.grid(row = 1, column = 1)
        self.add_category_button.grid(row = 2, column = 0)

    def add_category(self, frame):
        # Create a new category
        self.new_cat = Category(frame)

        # Move add_category_button down a unit
        current_button_row = self.add_category_button.grid_info()["row"]
        self.add_category_button.grid(row = current_button_row + 1, column = 0)

        # Place category
        self.new_cat.insert_category(current_button_row, 0)
        self.categories.append(self.new_cat)

        self.update_scrollable_region()
    
    def update_scrollable_region(self):
        self.frame.update_idletasks()
        c = self.frame.master
        c.configure(scrollregion=c.bbox("all"))

    def clear_resume(self):
        # Clear filename
        self.filename = "Untitled"

        # Clear entries
        self.name.set("")
        self.subheading.set("")

        # Empty and delete categories and its children
        for category in self.categories:
            category.delete_category()
        self.categories.clear()
        
        

        
        
    


