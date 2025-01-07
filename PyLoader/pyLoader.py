from tkinter import ttk

import tkinter.font as font
import tkinter as tk

from PyLoader.repeaterLayout import RepeaterLayout


class PyLoader:
    ''' '''

    def __init__(self, root):
        self.root = root
        self.bg = "lightgrey"
        self.fg = "black"
        style = ttk.Style()
        self.tabs = ttk.Notebook(self.root)
        style.configure("TNotebook.Tab", background=self.bg, foreground=self.fg)
        style.configure("TNotebook", background=self.bg, foreground=self.fg)
        style.map("TNotebook.Tab", background=[("selected", self.bg)])
        self.tabs.grid(row=0, column=0, sticky="nsew")
        self.defaultFont = font.nametofont("TkDefaultFont")

        self.defaultFont.configure(family="Arial", size=14)

        repeater = tk.Frame(self.tabs)
        repeater.columnconfigure(0, weight=1)
        repeater.configure(bg=self.bg)
        repeater.grid(row=0, column=0, sticky="nsew")
        repeater.rowconfigure(0, weight=1)
        repeater.columnconfigure(0, weight=1)
        self.tabs.add(repeater, text="Repeater")

        intruder = tk.Frame(self.tabs, width=500, height=500)
        intruder.configure(bg=self.bg)
        intruder.columnconfigure(0, weight=1)
        intruder.grid()
        self.tabs.add(intruder, text="Intruder")

        # the repeater tab
        RepeaterLayout(repeater, fg=self.fg, bg=self.bg)

        # the intruder tab
        # IntruderLayout(intruder)

        self.root.config(bg=self.bg)
