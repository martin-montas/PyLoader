import tkinter as tk
from PyLoader.proxyHandler import HTTPHandler, RequestBoxParser

class RequestBox:
    '''
    '''
    def __init__(self, root, bg=None, x=30, y=150, width=75, height=25):
        self.root = root
        self.bg = "lightgrey"
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg = "lightgrey"
        self.fg = "black"
        self.button_rel = 69
        self.button_bg = "lightgrey"
        self.button_fg = "white"

        # Url box
        self.url_box = tk.Entry(self.root)

        self.url_box.pack(side="top")
        self.url_box.place(x=50, y=5)

        self.url_box_tag = tk.Label(self.root, text="URL: ")
        self.url_box_tag.place(x=0, y=5)

        self.url_box_button = tk.Button(
            self.root,
            text="Send",
            bg="lightgrey",
            fg="black",
            bd=3,
            width=10,
            height=0,
            relief="raised",
            command=self.handle_request,
        )

        # info label
        self.info_label = tk.Label(self.root, text="Info", fg="black")
        self.info_label.place(x=0, y=30, anchor="nw")

        self.url_box_button.place(bordermode="outside", x=50,  y=30)
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
        '''
        '''
        pass

    def clear_command(self):
        '''
        '''
        pass

    def handle_request(self):
        '''
        Host: example.com
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
        Accept: text/html,application/xhtml+xml
        Content-Type: application/json
        '''
        http = HTTPHandler()
        if not self.url_box.get():
            return
        request = http.handle_request(self.url_box.get())
        parser = RequestBoxParser(request)
        headers = parser.parse_request_box()
        self.text_space.insert(tk.END, f"Host: {self.url_box.get()}\n")
        if request:
            self.text_space.insert(tk.END, f"Status Code: {request.status_code}\n")
        for key, value in headers.items():
            self.text_space.insert(tk.END, f"{key}: {value}\n")
