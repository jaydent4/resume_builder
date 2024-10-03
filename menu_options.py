from resumestructure import ResumeStructure
import convert
from tkinter import filedialog as fd
import json
import tkinter as tk

ACCEPTED_FILETYPE = [("JSON files", "*.json")]

section_schema = {
    "title": str,
    "subtitle": str,
    "time": str,
    "location": str,
    "descriptions": list
}

category_schema = {
    "title": str,
    "list": str,
    "sections": list
}

base_schema = {
    "name": str,
    "subheading": str,
    "categories": list
}

schema = [base_schema, category_schema, section_schema]

# Clear the resume
def new_file(resume):
    resume.clear_resume()

# Save resume as json file 
def save_as(resume):
    with fd.asksaveasfile(defaultextension=".json", filetypes=ACCEPTED_FILETYPE) as file:
        if file:
            resume.filename = file.name
            json.dump(convert.parse_resume(resume), file, indent=4)
            file.close()

# Save resume with the given filename or create a new file
def save(resume):
    if resume.filename == "Untitled":
        save_as(resume)
    else:
        file = open(resume.filename, 'w')
        json.dump(convert.parse_resume(resume), file, indent=4)

def open_file(resume):
    try:
        with fd.askopenfile(mode='r', filetypes=ACCEPTED_FILETYPE) as file:
            resume_data = json.load(file)
    except json.JSONDecodeError:
        print("ERROR: wrong json format")
    validate(resume_data)
    resume.clear_resume()
    fill(resume_data, resume)

def validate(data, level=0):
    # Check descriptions
    if level == 3:
        for description in data:
            if not isinstance(description, str):
                raise ValueError(f"Non-string value is stored in descriptions.")
        return
            
    # Compare to schema of the current data level of the json
    for key, type in schema[level].items():
        if key not in data:
            raise KeyError(f"Missing key: {key}")
        if not isinstance(data[key], type):
            raise ValueError(f"{key} is mapped to {type(data[key])}. {key} must be mapped to {type}.")
        if type is list:
            for item in data[key]:
                validate(item, level + 1)

def fill(data, resume):

    # Insert section information
    def fill_section(data, section):
        section.title.set(data["title"])
        section.subtitle.set(data["subtitle"])
        section.time.set(data["time"])
        section.location.set(data["location"])
        num_descriptions = len(data["descriptions"])
        for i in range(num_descriptions):
            section.add_description(section.frame)
            section.descriptions[i].insert(tk.INSERT, data["descriptions"][i])

    # Insert category information
    def fill_category(data, category):
        category.title.set(data["title"])
        category.list.insert(tk.INSERT, data["list"])
        num_sections = len(data["sections"])
        for i in range(num_sections):
            category.add_section(category.frame)
            fill_section(data["sections"][i], category.sections[i])
    
    resume.name.set(data["name"])
    resume.subheading.set(data["subheading"])
    num_categories = len(data["categories"])
    for i in range(num_categories):
        resume.add_category(resume.frame)
        fill_category(data["categories"][i], resume.categories[i])