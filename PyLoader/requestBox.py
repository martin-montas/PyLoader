from PyLoader.sendButton        import SendButton
import tkinter as tk



class RequestBox():
    '''
    '''
    def __init__(self, root, bg=None, x=30, y=150, width=75, height=25):
        self.root           = root
        #self.bg             = "lightgrey"
        self.x              = x 
        self.y              = y
        self.width          = width 
        self.height         = height
        self.bg             = "#FFEFD5"
        self.fg             = "black" 
        self.button_rel     = 69 
        self.button_bg      = "#f58216"
        self.button_fg      = "white"

        outer_frame = tk.Frame(self.root,
        relief="groove", bd=4, bg=self.bg)
        outer_frame.pack(padx=self.width, pady=self.height, fill="both", expand=True)
        outer_frame.place(x=20, y=140)

        label = tk.Label(self.root, text="Requests",
        fg="black")
        label.place(x=self.x, y=135, anchor="nw")

        spacer_frame = tk.Frame(
        outer_frame,
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




        # clear button for the RequestBox
        SendButton(
        self.root, "Clear",
        self.button_bg, "white",
        x=(280 - self.button_rel), y=709, width=10, height=0)

        # paste button for the RequestBox
        SendButton(
        self.root, "Paste",
        self.button_bg, "white",
        x=(400 - self.button_rel), y=709, width=10, height=0)

    def command(self):
        pass
