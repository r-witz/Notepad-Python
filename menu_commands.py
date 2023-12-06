from tkinter import END
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
from notepad_basics import root, text_area


# Creating all the functions of all the buttons in the NotePad
def open_file():
    global file
    file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*")])

    if file != '':
        root.title(f"{os.path.basename(file)}")
        text_area.delete(1.0, END)
        with open(file, "r") as file_:
            text_area.insert(1.0, file_.read())
            file_.close()
    else:
        file = None


def open_new_file():
    root.title("Untitled - Notepad")
    text_area.delete(1.0, END)


def save_file():
    global file
    if file == '':
        file = None
    else:
        file = open(file, "w")
        file.write(text_area.get(1.0, END))
        file.close()

    if file is None:
        file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                    filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")])
    else:
        file = open(file, "w")
        file.write(text_area.get(1.0, END))
        file.close()
        root.title(f"{os.path.basename(file)} - Notepad")


def exit_application():
    root.destroy()


def copy_text():
    text_area.event_generate("<<Copy>>")


def cut_text():
    text_area.event_generate("<<Cut>>")


def paste_text():
    text_area.event_generate("<<Paste>>")


def select_all():
    text_area.event_generate("<<Control-Keypress-A>>")


def delete_last_char():
    text_area.event_generate("<<KP_Delete>>")


def about_notepad():
    mb.showinfo("About Notepad", "This is just another Notepad, but this is better than all others")


def about_commands():
    commands = """
Under the File Menu:
- 'New' clears the entire Text Area
- 'Open' clears text and opens another file
- 'Save' saves your current file 
- 'Save As' saves your file in another extension

Under the Edit Menu:
- 'Copy' copies the selected text to your clipboard
- 'Cut' cuts the selected text and removes it from the text area 
- 'Paste' pastes the copied/cut text
- 'Select All' selects the entire text
- 'Delete' deletes the last character  
"""

    mb.showinfo(title="All commands", message=commands, width=60, height=40)
