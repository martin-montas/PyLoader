import tkinter as tk


class RequestBox():
    '''
    '''
    def __init__(self, root, bg=None, x=None, y=None, width=200, height=140):
        self.root           = root
        self.x              = 20 
        self.y              = 150
        self.bg             = "#FAF0C1"
        self.fg             = "black" 

        outer_frame         = tk.Frame(self.root,
        relief="groove", bd=6, bg="lightgrey")

        outer_frame.pack(padx=200, pady=height, fill="both", expand=True)
        outer_frame.place(x=20, y=150)
        request_label       = tk.Label(self.root, text="Requests",
        bg="lightgrey", fg="black")
        request_label.place(x=28, y=143, anchor="nw")

        spacer_frame = tk.Frame(
        outer_frame, bg="lightgrey",
        padx=30, pady=30,
        relief="flat")
        
        spacer_frame.pack(fill="both", expand=True)
        self.text_space     = tk.Text(spacer_frame,
        width=width,
        bg=self.bg,
        height=height,
        bd=3, relief="flat",
        wrap="word")
        self.text_space.pack(fill="both", expand=True)

    def command(self):
        pass
