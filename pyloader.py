#!/usr/bin/env python3

import tkinter as tk
from PyLoader.pyLoader import PyLoader


def main():
    root = tk.Tk()
    root.title("PyLoader")
    root.geometry("500x500")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    PyLoader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
