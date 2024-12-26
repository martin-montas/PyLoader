import tkinter as tk
from PyLoader.httpHandler import HTTPHandler, RequestBoxParser


class RequestBox:
    """
    Class to initialize the request box
    """

    def __init__(self, root, bg, fg, x=30, y=150, width=75, height=25):
        self.root = root
        self.bg = bg
        self.fg = fg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_rel = 69
        self.button_bg = "lightgrey"
        self.button_fg = "white"

        # Url box
        self.url_box = tk.Entry(self.root)
        self.url_box.pack(side="top")
        self.url_box.place(x=50, y=5)
        self.url_box_tag = tk.Label(self.root, text="URL: ")
        self.url_box_tag.place(x=0, y=5)

        # URL box button
        self.send_button = tk.Button(
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

        self.send_button.place(x=50, y=90)
        self.url_box.bind("<Return>", self.handle_request_event)

        # Clear button
        self.clear_button = tk.Button(
            self.root,
            text="Clear",
            bg="lightgrey",
            fg="black",
            bd=3,
            width=10,
            height=0,
            relief="raised",
            command=self.clear_command,
        )
        self.clear_button.place(x=190, y=90)

        # Request box label
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

    def clear_command(self):
        """ """
        self.text_space.delete(1.0, tk.END)

    def handle_request(self):
        http = HTTPHandler()
        if not self.url_box.get():
            self.clear_command()
        request = http.handle_request(self.url_box.get())
        parser = RequestBoxParser(request)
        headers = parser.parse_request_box()
        self.text_space.insert(tk.END, f"Host: {self.url_box.get()}\n")
        if request:
            self.text_space.insert(tk.END, f"Status Code: {request.status_code}\n")
        for key, value in headers.items():
            self.text_space.insert(tk.END, f"{key}: {value}\n")

    def handle_request_event(self, event: tk.Event) -> None:
        http = HTTPHandler()
        if not self.url_box.get():
            self.clear_command()
        request = http.handle_request(self.url_box.get())
        parser = RequestBoxParser(request)
        headers = parser.parse_request_box()
        self.text_space.insert(tk.END, f"Host: {self.url_box.get()}\n")
        if request:
            self.text_space.insert(tk.END, f"Status Code: {request.status_code}\n")
        for key, value in headers.items():
            self.text_space.insert(tk.END, f"{key}: {value}\n")
