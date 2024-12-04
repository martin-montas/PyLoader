import tkinter as tk


class Button:
    '''
            Class to initialize buttons
            for PyLoader tkinter
    '''
    def __init__(self, root, text, bg, fg, relx, rely, width, height):

        self.root           = root
        self.win_width      = self.root.winfo_width()
        self.win_height     = self.root.winfo_height()
        self.width          = width
        self.height         = height
        self.bg             = bg
        self.fg             = fg
        self.relx           = relx
        self.rely           = rely
        self.button         = tk.Button(self.root, text=text, bg=bg, fg=fg,
        width=self.width, height=self.height, 
        command=self.command).place(relx=0.3, rely=1.0, anchor="s")

    def command(self):
        pass
