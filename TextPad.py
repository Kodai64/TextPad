# **** TextPad text editor ****
# basic text editor programmed using Python 3.7 and tkinter library.
# version: 1.0.1
# 2019
# By: Kodai64


# =====================================
# **** importing libraries/modules ****

import tkinter as tk
from tkinter.ttk import Sizegrip
from tkinter.filedialog import *
from tkinter.messagebox import showinfo, askokcancel
from tkinter.scrolledtext import ScrolledText
from os.path import basename



# =====================================
# **** functions ****

file_name = ''
# using 'file_name' as a global variable to manage the name displayed in the program's title bar.

def warning_message(msg='!!!'):
    """ Display a warning message whenever changing the editor contents (new/open file) without saving. """
    content_ = text_entry.get('1.0', END)
    if content_ != '\n':
        warning = askokcancel('Warning', msg)
        if warning:
            return True
        else:
            return False
        

def new_file(*args):
    global file_name
    
    msg= 'Any progress will be lost if not saved!\nDo you want to proceed?'
    if warning_message(msg):
        text_entry.delete('1.0', END)
        root.title('Untitled - TextPad')
        file_name= ''
        

def open_file(*args):
    global file_name
    
    msg= 'Any progress will be lost if not saved!\nDo you want to proceed?'
    if text_entry.get('1.0', END)=='\n'  or  warning_message(msg):
        file_name = askopenfilename(title= 'Open', filetypes= (('text files','*.txt'),('all files','*.*')))

        try:
            with open(file_name, 'r') as openned_file:
                text_entry.delete(1.0, END)
                text_entry.insert(1.0, openned_file.read())
            root.title(os.path.basename(file_name) + ' - TextPad')

        except FileNotFoundError:
            pass
    
    
def save_file(*args):
    global file_name
    if file_name == '':
        save_as_file()
    try:
        with open(file_name, 'w') as saved_file:
            saved_file.write(text_entry.get(1.0, END))
    except FileNotFoundError:        
        pass


def save_as_file(*args):
    global file_name
    
    file_name = asksaveasfilename(title= 'Save As', defaultextension=".txt",
                                  filetypes= (('text files', '*.txt'),('all files','*.*')))
    
    try:
        with open(file_name, 'w') as saved_file:
            saved_file.write(text_entry.get(1.0, END))
        root.title(os.path.basename(file_name) + ' - TextPad')
        
    except FileNotFoundError:
        pass
    
    
def exit_app():
    if text_entry.get('1.0', END)=='\n'  or  warning_message('Exit without saving?'):
        root.clipboard_clear()
        root.destroy()
    
    
def about_info():
    showinfo('About TextPad','TextPad   (Python/Tkinter based text editor)\nVersion 1.0.1\n2019\n\nProgramed by: Kodai64')



def undo_text(event= None):
    try:
        text_entry.edit_undo()
    except tk.TclError:
        pass
    
def redo_text(event= None):
    try:
        text_entry.edit_redo()
    except tk.TclError:
        pass

def cut_text(event= None):
    text_entry.event_generate('<<Cut>>')

def copy_text(event= None):
    text_entry.event_generate('<<Copy>>')

def paste_text(event= None):
    text_entry.event_generate('<<Paste>>')

def delete_text(event= None):
    text_entry.event_generate('<Delete>')
    


# =====================================
# **** main window ****

root = tk.Tk()
root.wm_iconbitmap("Notepad.ico")
root.title('Untitled - TextPad')
root.geometry('700x350+70+50') # (Width x Height + Padding from left + Padding from top)



# =====================================
# **** Menus ****

main_menu = tk.Menu(root)
root.config(menu= main_menu)


# =====================================
## **** File menu ****

file_menu = tk.Menu(main_menu, tearoff= 0)
main_menu.add_cascade(label= 'File', underline= 0, menu= file_menu)

file_menu.add_command(label= 'New', underline= 0, accelerator= 'Ctrl+N', command= new_file)
file_menu.add_command(label= 'Open', underline= 0, accelerator= 'Ctrl+O', command= open_file)
file_menu.add_command(label= 'Save', underline= 0, accelerator= 'Ctrl+S', command= save_file)
file_menu.add_command(label= 'Save As', underline= 5, accelerator= 'Ctrl+Shift+S', command= save_as_file)
file_menu.add_separator()
file_menu.add_command(label= 'Exit', underline= 1, accelerator= 'Alt+F4', command= exit_app)


# =====================================
## **** Edit menu ****

edit_menu = tk.Menu(main_menu, tearoff= 0)
main_menu.add_cascade(label= 'Edit', underline= 0, menu= edit_menu)

edit_menu.add_command(label= 'Undo', underline= 0, accelerator='Ctrl+Z', command= undo_text)
edit_menu.add_command(label= 'Redo', underline= 0, accelerator= 'Ctrl+Y', command= redo_text)
edit_menu.add_separator()
edit_menu.add_command(label= 'Cut', underline= 2, accelerator= 'Ctrl+X', command= cut_text)
edit_menu.add_command(label= 'Copy', underline= 0, accelerator= 'Ctrl+C', command= copy_text)
edit_menu.add_command(label= 'Paste', underline= 0, accelerator= 'Ctrl+V', command= paste_text)
edit_menu.add_separator()
edit_menu.add_command(label= 'Delete', underline= 2, accelerator= 'Del', command= delete_text)



# =====================================
## **** Help menu ****

help_menu = tk.Menu(main_menu, tearoff= 0)
main_menu.add_cascade(label= 'Help', underline= 0, menu= help_menu)

help_menu.add_command(label= 'About TextPad', underline= 0, command= about_info)



# =====================================
## **** popup context menu (mouse right click) ****

context_menu= tk.Menu(root, tearoff= 0)

context_menu.add_command(label= 'Undo', command= undo_text)
context_menu.add_command(label= 'Redo', command= redo_text)
context_menu.add_separator()
context_menu.add_command(label= 'Cut', command= cut_text)
context_menu.add_command(label= 'Copy', command= copy_text)
context_menu.add_command(label= 'Paste', command= paste_text)
context_menu.add_separator()
context_menu.add_command(label= 'Delete', command= delete_text)

root.bind('<3>', lambda e: context_menu.post(e.x_root, e.y_root))



# =====================================
# **** status bar ****

# status bar is drawn before the text entry box 'text_entry' in order to keep it higher in priority of display.
status_bar = tk.Label(root, bd= 5, anchor= tk.W)
status_bar.pack(side= BOTTOM, fill= tk.X)

Sizegrip(status_bar).pack(side= 'right')
# 'Sizegrip' displays a lower right corner, making it easier to resize the editor window.



# =====================================
# **** Text area ****

text_entry = ScrolledText(root, relief= 'flat', bd= 2, wrap= 'word', undo= 1, padx= 3, pady= 3, font= ("Tahoma", "12"))
text_entry.pack(expand= True, fill= 'both')
text_entry.focus()
# ScrolledText is a Text widget with an implemented vertical scroll bar.



# =====================================
# **** keyboard shortcuts ****

text_entry.bind('<Control-n>', new_file)
text_entry.bind('<Control-N>', new_file)
text_entry.bind('<Control-o>', open_file)
text_entry.bind('<Control-O>', open_file)
text_entry.bind('<Control-s>', save_file)
text_entry.bind('<Control-S>', save_file)
text_entry.bind('<Control-Shift-s>', save_as_file)
text_entry.bind('<Control-Shift-S>', save_as_file)
#text_entry.bind('<Control-a>')
#text_entry.bind('<Control-A>')



# **** window/GUI loop ****
root.mainloop()
