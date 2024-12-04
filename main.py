#!/usr/bin/env python3

import tkinter as tk
from PyLoader.pyLoader import PyLoader




def main():
    root = tk.Tk()
    root.title("PyLoader")
    root.geometry("500x500")

    PyLoader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
