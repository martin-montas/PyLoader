import tkinter as tk
from PyLoader.pyLoader import PyLoader


def on_resize(event):
    # TODO:
    # try to prevent too much small resizing
    print(f"New size: {event.width}x{event.height}")


def main():
    root = tk.Tk()
    root.title("PyLoader v0.0.1")

    root.attributes("-zoomed", True)

    root.geometry("500x500")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Bind the resize event
    root.bind("<Configure>", on_resize)
    PyLoader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
