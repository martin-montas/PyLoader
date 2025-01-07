import tkinter as tk


class ResponseBox:
    """ """

    def __init__(
        self,
        root,
        bg="#FFEFD5",
        x=850,
        y=150,
        # FIXME(martin-montas) Just hard code the width and height when you have time
        width=75,
        height=25,
        fg="black",
        text_color_bg="#E8DCB8",
    ):
        self.root = root
        self.win_height = self.root.winfo_height()
        self.win_width = self.root.winfo_width()
        self.width = width
        self.height = height
        self.x = x
        self.button_bg = "lightgrey"
        self.y = y
        self.bg = bg
        self.fg = fg
        self.text_color_bg = text_color_bg
        outer_frame = tk.Frame(self.root, relief="groove", bd=4, bg=self.bg)

        spacer_frame = tk.Frame(
            outer_frame,
            bg=self.bg,
            padx=30,
            pady=30,
            relief="flat",
        )

        # Response box
        self.response_box = tk.Text(
            spacer_frame,
            width=70,
            height=30,
            bg=text_color_bg,
            fg=self.fg,
            bd=3,
            relief="flat",
            wrap="word",
        )

        # layout
        self.response_box.grid(row=0, column=1, sticky="e", padx=10, pady=10)
        spacer_frame.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        outer_frame.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    def insert_to_box(self, index, text):
        self.response_box.configure(state="normal")
        self.response_box.insert(index, text)
        self.response_box.configure(state="disabled")

    def delete_to_box(self, index, text):
        self.response_box.configure(state="normal")
        self.response_box.delete(index, text)
        self.response_box.configure(state="disabled")
