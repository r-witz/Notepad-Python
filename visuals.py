from tkinter import Menu, Text, Scrollbar, NSEW, VERTICAL, Y, RIGHT
from notepad_basics import root
from menu_commands import *

menu_bar = Menu(root)
root.config(menu=menu_bar)

# Setting the basic components of the window
text_area = Text(root, font=("Times New Roman", 12))
text_area.grid(sticky=NSEW)

scroller = Scrollbar(text_area, orient=VERTICAL)
scroller.pack(side=RIGHT, fill=Y)

scroller.config(command=text_area.yview)
text_area.config(yscrollcommand=scroller.set)

# Adding the File Menu and its components to create Python Text Editor
file_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

file_menu.add_command(label="New", command=open_new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close File", command=exit_application)

menu_bar.add_cascade(label="File", menu=file_menu)

# Adding the Edit Menu and its components
edit_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
edit_menu.add_command(label='Delete', command=delete_last_char)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Adding the Help Menu and its components
help_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

help_menu.add_command(label='About Notepad', command=about_notepad)
help_menu.add_command(label='About Commands', command=about_commands)

menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
