import tkinter as tk
from tkinter import messagebox
from PyLoader.requestBox import RequestBox
from PyLoader.responseBox import ResponseBox
from PyLoader.rightFrameInput import RightFrameInput


class RepeaterLayout:
    """
    Initiatests the basic layout

    @param root - the default window
    @return None
    """

    def __init__(self, root):
        self.root = root
        self.x = 140
        self.y = 100
        self.left_pad = 20
        self.footer_version = "PyLoader v0.0.1"
        self.fg = "black"
        self.button_bg = "lightgrey"
        self.button_fg = "black"
        self.bg = "lightgrey"
        self.bg2 = "lightgrey"
        self.win_width = self.root.winfo_width()
        self.win_height = self.root.winfo_height()
        self.button_rel = 69

        RequestBox(self.root)
        ResponseBox(self.root)
        RightFrameInput(self.root)

        footer = tk.Label(self.root, text=self.footer_version, bg=self.bg, fg=self.fg)
        footer.pack(side="bottom")

    def option_selected(self, value):
        messagebox.showinfo("Selected Option", value)
