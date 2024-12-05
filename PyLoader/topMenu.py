import tkinter as tk
#from tkinter import messagebox

class TopDefaultMenu:
  '''
  '''
  def __init__(self, root, bg=None, fg=None):
    self.root           = root
    self.bg             = "lightgrey"
    self.fg             = "black"
    self.button_width   = 10
    self.button_height  = 0
    menu_frame          = tk.Frame(self.root, bg=self.bg)
    self.result_frame   = tk.Frame(self.root, bg=self.bg)
    self.result_label   = tk.Label(self.result_frame, font=("Arial", 16), 
    bg=self.bg, fg=self.fg)
    self.result_frame.pack(pady=30)
    self.result_label.pack()

    # Create a frame for the horizontal menu (buttons)
    menu_frame.pack(side=tk.TOP, fill=tk.X)
    
    # Define the menu buttons
    menu_options = ["Seeker", "shooter", "Blah", "Nothing"]
    for option in menu_options:
        button = tk.Button(menu_frame, text=option, font=("Arial", 16), 
        command=lambda opt=option: self.show_content(opt),
        bg=self.bg, fg=self.fg,
        width=self.button_width, height=self.button_height
        )
        button.pack(side=tk.LEFT, padx=10)

  def show_content(self,option):

    self.result_label.config(text="")
    if option == "Option 1":
        # TODO: called the classes here
        # make sure you pass the proper elements to it
        self.result_label.config(text="You selected Option 1: Information about Option 1.")
    elif option == "Option 2":
        self.result_label.config(text="You selected Option 2: Information about Option 2.")
    elif option == "Option 3":
        self.result_label.config(text="You selected Option 3: Information about Option 3.")
    elif option == "Option 4":
        self.result_label.config(text="You selected Option 4: Information about Option 4.")

