from tkinter import ttk

import tkinter.font as font

from PyLoader.repeaterLayout import RepeaterLayout


class PyLoader:
    """ """

    def __init__(self, root):
        self.root = root
        self.bg = "lightgrey"
        self.fg = "black"
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack()
        self.tabs.grid(row=0, column=0, sticky="nsew")
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Arial", size=15)

        repeater = ttk.Frame(self.tabs, width=500, height=500)
        repeater.columnconfigure(0, weight=1)
        repeater.pack(fill="both", expand=True)
        self.tabs.add(repeater, text="Repeater")

        intruder = ttk.Frame(self.tabs, width=500, height=500)
        intruder.columnconfigure(0, weight=1)
        intruder.pack(fill="both", expand=True)
        self.tabs.add(intruder, text="Intruder")

        # the repeater tab
        RepeaterLayout(repeater)

        # the intruder tab
        # IntruderLayout(intruder)

        self.root.config(bg=self.bg)
