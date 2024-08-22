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

        self.add_description(self.frame)

    def insert_section(self, grid_row, grid_col):
        # Place frame in the specified position
        self.frame.grid(row = grid_row, column = grid_col)

        # Place all other widgets in the frame
        self.title_label.grid(row = 0, column = 0)
        self.title_entry.grid(row = 1, column = 0)
        self.subtitle_label.grid(row = 2, column = 0)
        self.subtitle_entry.grid(row = 3, column = 0)
        self.time_label.grid(row = 4, column = 0)
        self.time_entry.grid(row = 5, column = 0)
        self.location_label.grid(row = 6, column = 0)
        self.location_entry.grid(row = 7, column = 0)
        self.descriptions_label.grid(row = 8, column = 0)
        self.add_description_button.grid(row = 9, column = 0)
    
    def add_description(self, frame):
        # Add a description to a section
        self.new_description = tk.Text(frame, width = 10, height = 5)
        
        # Move the add_descriptions_button down one row
        button_position = self.add_description_button.grid_info()
        print(button_position)
        # current_button_row = button_position["row"]
        # self.add_description_button.grid(current_button_row + 1, 0)

        # # Placing new_description into the section frame
        # if len(self.descriptions) != 0: # place new_description under location_entry if there are no description text boxes currently
        #     self.new_description.grid(row = 9, column = 0)
        # else: # place new_description under the last description text box
        #     current_last_row = self.descriptions[-1].grid_info().get('row', 0)
        #     self.new_description.grid(row = current_last_row + 1, column = 0)
    
        self.descriptions.append(self.new_description)