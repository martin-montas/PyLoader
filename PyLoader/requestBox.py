import tkinter as tk


class RequestBox():
    '''
    '''
    def __init__(self, root, bg=None, x=None, y=None, width=0, height=0):
        self.root           = root
        self.x              = 30 
        self.y              = 150
        self.width          = 75
        self.height         = 25
        self.bg             = "#FFEFD5"
        self.fg             = "black" 

        outer_frame = tk.Frame(self.root,
        relief="groove", bd=4, bg="lightgrey")
        outer_frame.pack(padx=self.width, pady=self.height, fill="both", expand=True)
        outer_frame.place(x=20, y=140)

        label = tk.Label(self.root, text="Requests",
        bg="lightgrey", fg="black")
        label.place(x=self.x, y=135, anchor="nw")

        spacer_frame = tk.Frame(
        outer_frame, bg="lightgrey",
        padx=30, pady=30,
        relief="flat",
        )
        spacer_frame.pack(fill="both", expand=True)
        self.text_space     = tk.Text(spacer_frame,
        width=self.width,
        bg=self.bg,
        height=self.height,
        bd=3, relief="flat",
        wrap="word",)
        self.text_space.pack(fill="both", expand=True)

    def command(self):
        pass
