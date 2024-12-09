import tkinter as tk


class ResponseBox:
    """ """

    def __init__(self, root, bg="#FFEFD5", x=800, y=150, width=75, height=25):
        self.root = root
        self.win_height = self.root.winfo_height()
        self.win_width = self.root.winfo_width()
        self.width = width
        self.height = height
        self.x = x + 60
        self.button_rel = 721
        self.button_bg = "lightgrey"
        self.y = y
        self.bg = bg
        self.fg = "black"

        outer_frame = tk.Frame(self.root, relief="groove", bd=4, bg="lightgrey")
        outer_frame.pack(padx=self.width, pady=self.height, fill="both", expand=True)
        outer_frame.place(x=self.x, y=140)

        label = tk.Label(self.root, text="Response", bg="lightgrey", fg="black")
        label.place(x=self.x + 75, y=135, anchor="ne")

        spacer_frame = tk.Frame(
            outer_frame,
            bg="lightgrey",
            padx=30,
            pady=30,
            relief="flat",
        )

        spacer_frame.pack(fill="both", expand=True)
        self.text_space = tk.Text(
            spacer_frame,
            width=self.width,
            bg=self.bg,
            height=self.height,
            bd=3,
            relief="flat",
            wrap="word",
        )

        self.text_space.pack(fill="both", expand=True)

        tk.Label(self.root, bg="lightgrey", fg="black", text="Send").place(
            bordermode="outside", relx=0.5, anchor="center", y=350
        )

        tk.Button(
            self.root,
            text=">>",
            fg="black",
            bd=3,
            width=10,
            height=0,
            relief="raised",
            command=self.response_button_command,
        ).place(bordermode="outside", relx=0.5, anchor="center", y=400)

        # SendButton(
        # self.root, "Clear",
        # self.button_bg, "white",
        # x=(280 - self.button_rel), y=709, width=10, height=0)

        # # paste button for the RequestBox
        # SendButton(
        # self.root, "Paste",
        # self.button_bg, "white",
        # x=(400 - self.button_rel), y=709, width=10, height=0)

        tk.Button(self.root, text="Clear", bg=self.button_bg, fg="black").place(
            relx=0.5, y=710
        )

        tk.Button(self.root, text="Paste", bg=self.button_bg, fg="black").place(
            relx=0.5, y=740
        )

    def response_button_command(self):
        pass
