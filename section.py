import category
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
        self.frame.pack(padx = 10, pady = 10, fill = 'x', expand = True)

        # Create a title entry box
        self.title_label = tk.Label(self.frame, text = "Title")
        self.title_label.pack(anchor = 'nw')
        self.title_entry = tk.Entry(self.frame, textvariable = self.title)
        self.title_entry.pack(anchor = 'nw', padx = 5, pady = (5, 5))

        # Create a subtitle entry box
        self.subtitle_label = tk.Label(self.frame, text = "Subtitle")
        self.subtitle_label.pack(anchor = 'w')
        self.subtitle_entry = tk.Entry(self.frame, textvariable = self.subtitle)
        self.subtitle_entry.pack(anchor = 'w', padx = 5, pady = (5, 5))

        # Create a time frame entry box
        self.time_label = tk.Label(self.frame, text = "Time")
        self.time_label.pack(anchor = 'w')
        self.time_entry = tk.Entry(self.frame, textvariable = self.time)
        self.time_entry.pack(anchor = 'w', padx = 5, pady = (5,5))

        # Create a location entry box
        self.location_label = tk.Label(self.frame, text = "Location")
        self.location_label.pack(anchor = 'w')
        self.location_entry = tk.Entry(self.frame, textvariable = self.location)
        self.location_entry.pack(anchor = 'w', padx = 5, pady = (5,5))

        # Add one description text box
        self.descriptions_label = tk.Label(self.frame, text = "Description")
        self.descriptions_label.pack(anchor = 'w', pady = (10, 5))
        self.starting_textbox = tk.Text(self.frame, width = 10, height = 5)
        self.starting_textbox.pack(expand = True, fill = 'x')
    
    def add_description(self, root):
        #todo
        return