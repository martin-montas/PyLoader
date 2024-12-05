import tkinter as tk
from tkinter import ttk

class TopDefaultMenu:
    '''
        Class to initialize the top menu
        for PyLoader
        @param root - the default window
        @bg - background color
        @fg - foreground color
        @return None
    '''
    def __init__(self, root, bg=None, fg=None):
        self.root           = root
        self.bg             = "lightgrey"
        self.fg             = "black"
        self.button_width   = 10
        self.button_height  = 0

        horizontal_separator = ttk.Separator(self.root, orient="horizontal")
        horizontal_separator.pack(fill="x", pady=75)
