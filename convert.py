import json
import tkinter as tk
from resumestructure import ResumeStructure
from category import Category
from section import Section

def convert_section(sec: Section) -> dict:
    sec_dict = {}
    
    # Insert non-dynamically added components
    sec_dict["title"] = sec.title.get().strip()
    sec_dict["subtitle"] = sec.subtitle.get().strip()
    sec_dict["time"] = sec.time.get().strip()
    sec_dict["location"] = sec.location.get().strip()

    # Insert dynamically added components
    descriptions_list = []
    for description in sec.descriptions:
        t = description.get(0.0, tk.END).strip()
        if t == "":
            descriptions_list.append(t)
    sec_dict["descriptions"] = descriptions_list


def convert_category(cat: Category) -> dict:
    cat_dict = {}

    # Insert non-dynamically added components
    cat_dict["title"] = cat.title.get().strip()
    cat_dict["list"] = cat.list.get(0.0, tk.END).strip()

    # Insert dynamically added componenets
    section_list = []
    for section in cat.sections:
        sec_dict = convert_section(section)
        section_list.append(sec_dict)
    cat_dict["sections"] = section_list
    
def parse_resume(resume: ResumeStructure) -> dict:
    res_dict = {}

    # Insert non-dynamically added components
    res_dict["name"] = resume.name_entry_text.get().strip()
    res_dict["subheading"] = resume.subheading_text.get().strip()
    
    # Insert dynamically added components
    category_list = []
    for category in resume.categories:
        cat_dict = convert_category(category)
        category_list.append(cat_dict)
    res_dict["categories"] = category_list
    return res_dict