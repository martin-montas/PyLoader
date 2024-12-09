import tkinter as tk


class SendButton:
    """
    Class to initialize buttons
    for PyLoader tkinter
    """

    def __init__(
        self, root, text, bg="#f58216", fg="white", x=280, y=709, width=10, height=0
    ):

        self.root = root
        self.win_width = self.root.winfo_width()
        self.win_height = self.root.winfo_height()
        self.button = tk.Button(
            self.root,
            text=text,
            bg=bg,
            fg=fg,
            bd=3,
            width=width,
            height=height,
            relief="raised",
            command=self.command,
        ).place(
            bordermode="outside",
            x=x,
            y=y,
        )

    def command(self):
        pass
