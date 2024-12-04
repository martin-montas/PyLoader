import tkinter as tk
from tkinter import messagebox

class TopDefaultMenu:
  '''
  '''
  def __init__(self, root, bg_color, fg_color):
    self.root       = root
    self.fg       = bg_color
    self.bg       = fg_color
    self.menu_bar   = tk.Menu(self.root, bg=self.bg, fg=self.fg)
    self.file_menu  = tk.Menu(self.menu_bar, tearoff=0)
    self.edit_menu  = tk.Menu(self.menu_bar, tearoff=0)

  def init(self):
    '''
    '''
    self.file_menu.add_command(label="New", command=self.new_file)
    self.file_menu.add_command(label="Open", command=self.open_file)
    self.file_menu.add_command(label="Save", command=self.save_file)
    self.file_menu.add_separator()  # Adds a separator line
    self.file_menu.add_command(label="Exit", command=self.exit_app)
    self.menu_bar.add_cascade(label="File", menu=self.file_menu)
    self.edit_menu.add_command(label="Undo")
    self.edit_menu.add_command(label="Redo")
    self.edit_menu.add_separator()  
    self.edit_menu.add_command(label="Cut")
    self.edit_menu.add_command(label="Copy")
    self.edit_menu.add_command(label="Paste")
    self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
    self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
    self.help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a simple menu example"))
    self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

  def new_file(self):
      '''
      '''
      messagebox.showinfo("New File", "Create a new file")

  def open_file(self):
      '''
      '''
      messagebox.showinfo("Open File", "Open an existing file")

  def save_file(self):
      '''
      '''
      messagebox.showinfo("Save File", "Save the current file")

  def exit_app(self):
      '''
      '''
      self.root.quit()
