import tkinter as tk



class RightFrameInput:
    def __init__(self, root, bg=None, x=None, y=None, width=0, height=0):
        self.root           = root
        self.win_width      = self.root.winfo_width()
        self.win_height     = self.root.winfo_height()
        self.x              = 600
        self.y              = 150
        self.width          = 75
        self.height         = 25
        self.bg             = "#FFEFD5"
        self.fg             = "black" 

        '''
        outer_frame = tk.Frame(self.root,
        relief="groove", bd=4, bg="lightgrey")
        outer_frame.pack(padx=self.width, pady=self.height, fill="both", expand=True)
        outer_frame.place(x=1000, y=140)

        spacer_frame = tk.Frame(
        outer_frame, bg="lightgrey",
        padx=30, pady=30,
        relief="flat")
        '''




