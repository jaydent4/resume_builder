from resumestructure import ResumeStructure
import convert
from tkinter import filedialog as fd
import json

ACCEPTED_FILETYPE = [("JSON files", "*.json")]

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

def open_file(root, resume):
    try:
        with fd.askopenfile(mode='r', filetypes=ACCEPTED_FILETYPE) as file:
            resume_data = json.load(file)
            

    except json.JSONDecodeError:
        print("ERROR: wrong json format")
    except KeyError as e:
        print(f"ERROR: Missing {e} attribute")
            
def validate(data):
    return


# # Create a new file; change name and delete current text
# def new_file(text):
#     global filename
#     filename = "Untitled"
#     text.delete(0.0, tk.END)

# # Save current file 
# def save(text):
#     global filename
#     t = text.get(0.0, tk.END)
#     file = open(filename, 'w')
#     file.write(t)
#     file.close()

# def save_as(text):
#     # prompt to save each of the entries within a text file
#     file = fd.asksaveasfile(mode = 'w', defaultextension = '.txt')
#     t = text.get(0.0, tk.END)
#     t = t.rstrip()
#     try:
#         file.write(t)
#     except: # should never reach this point
#         tk.showerror(Title="ERROR", message ="Unable to save file")

# def open_file(text):
#     f = fd.askopenfile(mode='r')
#     t = f.read()
#     text.delete(0.0, tk.END)
#     text.insert(0.0, t)