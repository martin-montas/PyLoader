from tkinter import ttk
from PyLoader.topMenu import TopDefaultMenu
from PyLoader.initialLayout import InitialLayout


class PyLoader:
    """ """

    def __init__(self, root):
        self.root = root
        self.bg = "lightgrey"
        self.fg = "black"
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack()
        self.tabs.grid(row=0, column=0, sticky="nsew")

        repeater = ttk.Frame(self.tabs, width=500, height=500)
        intruder = ttk.Frame(self.tabs, width=500, height=500)
        settings = ttk.Frame(self.tabs, width=500, height=500)

        repeater.columnconfigure(0, weight=1)
        intruder.columnconfigure(0, weight=1)
        settings.columnconfigure(0, weight=1)

        repeater.pack(fill="both", expand=True)
        intruder.pack(fill="both", expand=True)
        settings.pack(fill="both", expand=True)

        self.tabs.add(repeater, text="Repeater")
        self.tabs.add(intruder, text="Intruder")
        self.tabs.add(settings, text="Settings")

        InitialLayout(repeater)
        TopDefaultMenu(root)

        self.root.config(bg=self.bg)
