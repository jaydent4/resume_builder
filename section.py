import tkinter as tk

class Section:
    def __init__(self, root):
        self.title = tk.StringVar()
        self.subtitle = tk.StringVar()
        self.time = tk.StringVar()
        self.location = tk.StringVar()
        self.descriptions = []

        # Create a frame
        self.frame = tk.Frame(root, bd = 2, relief = "raised")
        
        # Set frame grid
        for i in range(30):
            self.frame.grid_columnconfigure(i, weight = 1)

        # Create a title entry box
        self.title_label = tk.Label(self.frame, text = "Title")
        self.title_entry = tk.Entry(self.frame, textvariable = self.title)

        # Create a subtitle entry box
        self.subtitle_label = tk.Label(self.frame, text = "Subtitle")
        self.subtitle_entry = tk.Entry(self.frame, textvariable = self.subtitle)

        # Create a time frame entry box
        self.time_label = tk.Label(self.frame, text = "Time")
        self.time_entry = tk.Entry(self.frame, textvariable = self.time)

        # Create a location entry box
        self.location_label = tk.Label(self.frame, text = "Location")
        self.location_entry = tk.Entry(self.frame, textvariable = self.location)

        # Create label for descriptions section
        self.descriptions_label = tk.Label(self.frame, text = "Description")

        # Add button to add a description text box
        self.add_description_button = tk.Button(self.frame, text = "Add Description", command = lambda: self.add_description(self.frame))

        # Place all widgets in the frame
        self.title_label.grid(row=0, column=0, sticky="w", padx=(5, 2), pady=(5, 2))
        self.title_entry.grid(row=0, column=1, sticky="ew", padx=(2, 5), pady=(5, 2))
        self.subtitle_label.grid(row=1, column=0, sticky="w", padx=(5, 2), pady=(5, 2))
        self.subtitle_entry.grid(row=1, column=1, sticky="ew", padx=(2, 5), pady=(5, 2))
        self.time_label.grid(row=2, column=0, sticky="w", padx=(5, 2), pady=(5, 2))
        self.time_entry.grid(row=2, column=1, sticky="ew", padx=(2, 5), pady=(5, 2))
        self.location_label.grid(row=3, column=0, sticky="w", padx=(5, 2), pady=(5, 2))
        self.location_entry.grid(row=3, column=1, sticky="ew", padx=(2, 5), pady=(5, 2))
        self.descriptions_label.grid(row=4, column=0, sticky="w", padx=(5, 2), pady=(10, 2))
        self.add_description_button.grid(row=5, column=0, pady=(5, 2))
    
    def delete_section(self):
        # Delete all descriptions
        while self.descriptions:
            description = self.descriptions.pop()
            description.destroy()
        self.descriptions.clear()
        # Delete the frame and its children
        self.frame.destroy()

    def insert_section(self, grid_row, grid_col):
        # Place frame in the specified position
        self.frame.grid(row = grid_row, column = grid_col, sticky = "ew", padx = (5, 5), pady = (5, 5))
    
    def add_description(self, frame):
        # Add a description to a section
        self.new_description = tk.Text(frame, width = 10, height = 5)
        curr_button_row = self.add_description_button.grid_info()["row"]
        
        # Move add_description_button down one row
        self.add_description_button.grid(row = curr_button_row + 1, column = 0)

        # Add new_description above the button
        self.new_description.grid(row = curr_button_row, column = 0, sticky = "ew", columnspan = 30)
        self.descriptions.append(self.new_description)
        self.update_scrollable_region()

    def update_scrollable_region(self):
        self.frame.update_idletasks()
        c = self.frame.master.master.master
        c.configure(scrollregion=c.bbox("all"))