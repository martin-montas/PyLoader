from tkinter                        import messagebox
from PyLoader.buttonTemplate        import Button

class InitialLayout:
  '''
        Initiatests the basic layout
  '''
  def __init__(self, root):
    self.root         = root
    self.x            = 140
    self.y            = 100
    self.fg           = "white"
    self.active_bg    = "#4B3C31"
    self.button_bg    = "turquoise"
    self.button_fg    = "white"
    self.bg           = "#4B3C31"
    self.active_fg    = "black"
    self.menu_x       = 30
    self.menu_y       = 30
    self.menu_y       = 30

    Button(self.root, "Send", self.bg, self.fg, 30, 500, 25, 3)
    '''
    self.menu_button = tk.Menubutton( self.root, text="Attack type: ", 
     relief="raised",direction="right", 
    background="red", foreground=self.fg, 
    activebackground=self.active_bg, activeforeground=self.active_fg
    )
    self.menu               = tk.Menu(self.menu_button, tearoff=0)
    '''
    # self.send_button        = tk.Button(self.root, text="Send", bg=self.button_bg, 
    # fg=self.button_bg).place(x=self.x, y=self.y)

  def option_selected(self, value):
     messagebox.showinfo("Selected Option", value)
  def init(self):
     '''
     self.menu_button.place(x=self.x, y=self.y)
     self.menu.add_command(label="Brute Force Attack Mode", command=lambda: self.option_selected("Mode 1"))
     self.menu.add_command(label="File Traversal Attack Mode", command=lambda: self.option_selected("Mode 2"))
     self.menu_button.config(menu=self.menu)
     '''
