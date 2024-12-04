import tkinter as tk


class RequestText():
    '''
    '''
    def __init__(self, root, color, x=0, y=0, width=0, height=0):
        self.root           = root
        self.x              = 20 
        self.y              = 160
        self.width          = 100
        self.height         = 30
        self.bg             = color 
        self.fg             = "white" 
        self.text_space     = tk.Text(self.root, width=self.width,
        height=self.height, bg=self.bg, fg=self.fg).place(x=self.x, y=self.y)

    def command(self):
        pass
