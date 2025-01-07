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
        request_text=None,
    ):
        self.root = root
        self.win_height = self.root.winfo_height()
        self.win_width = self.root.winfo_width()
        self.width = width
        self.height = height
        self.x =x  
        self.button_bg = "lightgrey"
        self.y = y
        self.bg = bg
        self.fg = fg

        '''
        outer_frame = tk.Frame(self.root, relief="groove", bd=4, bg=self.bg)
        outer_frame.pack(
            padx=self.width, pady=self.height, fill="both",  side="right"
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
        spacer_frame.pack(fill="both", side="right")
        '''

        self.response_box = tk.Text(
            self.root,
            width=75,
            height=30,
            bg=self.bg,
            fg=self.fg,
            bd=3,
            relief="flat",
            wrap="word",
        )
        self.response_box.configure(state="disabled")
        if request_text:
            # request_width = request_text.winfo_width()
            self.width = self.root.winfo_width()
            self.response_box.place(x=self.width -10, y=340, anchor="e")

    def insert_to_box(self, index, text):
        self.response_box.configure(state="normal")
        self.response_box.insert(index, text)
        self.response_box.configure(state="disabled")

    def delete_to_box(self, index, text):
        self.response_box.configure(state="normal")
        self.response_box.delete(index, text)
        self.response_box.configure(state="disabled")
