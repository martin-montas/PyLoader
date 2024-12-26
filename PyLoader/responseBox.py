import tkinter as tk


class ResponseBox:
    """ """

    def __init__(
        self,
        root,
        bg="#FFEFD5",
        x=800,
        y=150,
        # FIXME(martin-montas) Just hard code the width and height when you have time
        width=75,
        height=25,
        fg="black",
    ):
        self.root = root
        self.win_height = self.root.winfo_height()
        self.win_width = self.root.winfo_width()
        self.width = width
        self.height = height
        self.x = 1000 - (75)
        self.button_bg = "lightgrey"
        self.y = y
        self.bg = bg
        self.fg = fg

        outer_frame = tk.Frame(self.root, relief="groove", bd=4, bg=self.bg)
        outer_frame.pack(
            padx=self.width, pady=self.height, fill="both", expand=True, side="right"
        )
        outer_frame.place(x=self.x, y=140)

        label = tk.Label(self.root, text="Response", bg=self.bg, fg=self.fg)
        label.place(x=self.x + 15, y=135)

        spacer_frame = tk.Frame(
            outer_frame,
            bg=self.bg,
            padx=30,
            pady=30,
            relief="flat",
        )

        spacer_frame.pack(fill="both", expand=True, side="right")
        self.response_box_text = tk.Text(
            spacer_frame,
            width=self.width,
            height=self.height,
            bg=self.bg,
            fg=self.fg,
            bd=3,
            relief="flat",
            wrap="word",
        )

        self.response_box_text.configure(state="disabled")
        self.response_box_text.pack(fill="both", expand=True)

    def insert_to_box(self, index, text):
        self.response_box_text.configure(state="normal")
        self.response_box_text.insert(index, text)
        self.response_box_text.configure(state="disabled")

    def delete_to_box(self, index, text):
        self.response_box_text.configure(state="normal")
        self.response_box_text.delete(index, text)
        self.response_box_text.configure(state="disabled")
