import tkinter as tk
from PyLoader.proxyComponent import CustomProxy


class UrlEntry:
    def __init__(self,root, width=0):
        self.entry      = tk.Entry(root, width=width,font=("Arial", 16))

        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.command_input)

    def command_input(self,event=None):
        '''
                Process user input
        '''
        user_input = self.entry.get()
        try:
            if "https://" in user_input:
                user_input = user_input
            else:
                user_input = "https://" + user_input
        except:
            user_input = "https://" + user_input
        CustomProxy(user_input)
