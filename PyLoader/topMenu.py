from PyLoader.initialLayout   import InitialLayout
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
        self.tabs            = ttk.Notebook(self.root)
        self.tabs.pack()
        self.tabs.grid(row=0, column=0, sticky="nsew")

        repeater = ttk.Frame(self.tabs,width=500, height=500)
        intruder = ttk.Frame(self.tabs,width=500, height=500)

        repeater.columnconfigure(0, weight=1)
        intruder.columnconfigure(0, weight=1)


        repeater.pack(fill="both", expand=True)
        intruder.pack(fill="both", expand=True)

        self.tabs.add(repeater, text="Repeater")
        self.tabs.add(intruder, text="Intruder")

        InitialLayout(repeater)
