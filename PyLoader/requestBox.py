import tkinter as tk
from PyLoader.proxyHandler import HTTPHandler, RequestBoxParser


class RequestBox:
    ''' '''

    def __init__(self, root, bg=None, x=30, y=150, width=75, height=25):
        self.root = root
        self.bg = "lightgrey"
        self.x = x
        self.y = y

        # url box
        self.url_box = tk.Entry(self.root)
        self.url_box.pack(side="left")

        self.width = width
        self.height = height
        self.bg = "lightgrey"
        self.fg = "black"
        self.button_rel = 69
        self.button_bg = "lightgrey"
        self.button_fg = "white"

        outer_frame = tk.Frame(self.root, relief="groove", bd=4, bg=self.bg)
        outer_frame.pack(padx=self.width, pady=self.height, fill="both", expand=True)
        outer_frame.place(x=20, y=140)

        label = tk.Label(self.root, text="Requests", fg="black")
        label.place(x=self.x, y=135, anchor="nw")

        spacer_frame = tk.Frame(
            outer_frame,
            padx=30,
            pady=30,
            relief="flat",
        )
        spacer_frame.pack(fill="both", expand=True)

        # Request box text area
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

        # clear button for the RequestBox
        tk.Button(
            self.root,
            text="clear",
            bg=self.button_bg,
            fg=self.fg,
            bd=3,
            width=10,
            height=0,
            relief="raised",
            command=self.clear_command,
        ).place(
            bordermode="outside",
            x=(280 - self.button_rel),
            y=709,
        )
        # Clear button for the RequestBox
        tk.Button(
            self.root,
            text="Paste",
            bg=self.button_bg,
            fg=self.fg,
            bd=3,
            width=10,
            height=0,
            relief="raised",
            command=self.paste_command,
        ).place(
            bordermode="outside",
            x=(400 - self.button_rel),
            y=709,
        )

    def paste_command(self):
        ''' '''
        pass

    def clear_command(self):
        ''' '''
        pass

    def handle_request(self):
        ''' '''
        http = HTTPHandler()
        request = http.handle_request(self.url_box.get())
        parser = RequestBoxParser(request)
        headers = parser.parse_request_box()
        for key, value in headers.items():
            self.text_space.insert(tk.END, f"{key}: {value}\n")
