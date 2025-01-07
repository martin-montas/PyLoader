from tkinter import messagebox
from PyLoader.requestBox import RequestBox


class RepeaterLayout:
    '''
    Initiatests the basic layout

    @param root - the default window
    @return None
    '''

    def __init__(self, root, bg, fg):
        self.root = root
        self.x = 140
        self.y = 100
        self.left_pad = 20
        self.button_bg = "lightgrey"
        self.button_fg = "black"
        self.win_width = self.root.winfo_width()
        self.win_height = self.root.winfo_height()
        self.button_rel = 69

        root.grid_rowconfigure(0, weight=1)  # Allow the row to expand
        root.grid_columnconfigure(0, weight=1)  # Allow the column to expand

        RequestBox(self.root, bg=bg, fg=fg)


    def option_selected(self, value):
        messagebox.showinfo("Selected Option", value)
