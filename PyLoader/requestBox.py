import tkinter as tk
from PyLoader.httpHandler import HTTPHandler, RequestBoxParser
from PyLoader.responseBox import ResponseBox


class RequestBox:
    '''
    Class to initialize the request box
    '''

    def __init__(self, root, bg, fg, x=30, y=150, width=75, height=25):
        self.root = root
        self.bg = bg
        self.fg = fg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.headers = None
        self.button_rel = 69
        self.button_bg = "lightgrey"
        self.button_fg = "white"
        self.text_color_bg = "#ffedc7"

        self.http = HTTPHandler()

        # Url box
        self.url_box = tk.Entry(self.root, bg=self.bg, fg=self.fg)
        self.url_box.grid(row=0, column=0, sticky="n", padx=10, pady=10)

        # Configure column weight to allow resizing
        self.root.columnconfigure(0, weight=1)
        self.url_box.focus_set()
        self.url_box.insert(0, "https://google.com")

        # URL box button
        self.send_button = tk.Button(
            self.root,
            text="Send",
            bg=self.bg,
            fg=self.fg,
            bd=3,
            width=10,
            height=0,
            relief="raised",
            command=self.handle_request_button,
        )
        # self.send_button.place(x=50, y=90)
        self.url_box.bind("<Return>", self.handle_request_event)

        # Request button
        self.request_button = tk.Button(
            self.root,
            text=">>",
            bg=self.bg,
            fg=self.fg,
            bd=3,
            width=0,
            height=0,
            command=self.handle_request_middle_button,
        )
        self.request_button.place(relx=0.5, rely=0.4, anchor="center")

        # Clear button
        self.clear_button = tk.Button(
            self.root,
            text="Clear",
            bg=self.bg,
            fg=self.fg,
            bd=3,
            width=10,
            height=0,
            relief="raised",
            command=self.clear_command,
        )
        self.request_button.place(relx=0.5, rely=0.4, anchor="w")

        # Request box label
        outer_frame = tk.Frame(self.root, relief="groove", bd=4, bg=self.bg)
        spacer_frame = tk.Frame(
            outer_frame,
            padx=30,
            pady=30,
            relief="flat",
            bg=self.bg,
        )

        # Request box
        self.request_text = tk.Text(
            spacer_frame,
            width=70,
            bg=self.text_color_bg,
            height=30,
            bd=3,
            relief="flat",
            wrap="word",
            fg=self.fg,
        )

        # Layout
        self.request_text.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        spacer_frame.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        outer_frame.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.request_text.bind("<Return>", self.handle_request_event)
        self.response_box = ResponseBox(
            self.root,
            bg=bg,
            fg=fg,
            text_color_bg=self.text_color_bg,
        )

    def return_request_box(self):
        return self.request_text

    def clear_command(self):
        self.request_text.delete(1.0, tk.END)

    def handle_request_button(self):
        if not self.url_box.get():
            self.clear_command()

        request = self.http.handle_request(self.url_box.get())
        if request:
            self.headers = request.headers
        parser = RequestBoxParser(request)
        headers = parser.parse_request_box()
        self.request_text.insert(tk.END, f"Host: {self.url_box.get()}\n")
        if request:
            self.request_text.insert(tk.END, f"Status Code: {request.status_code}\n")
        for key, value in headers.items():
            self.request_text.insert(tk.END, f"{key}: {value}\n")

    def handle_request_event(self, event: tk.Event) -> None:
        if not self.url_box.get():
            self.clear_command()
        request = self.http.handle_request(self.url_box.get())
        if request:
            self.headers = request.headers
        parser = RequestBoxParser(request)
        headers = parser.parse_request_box()
        self.request_text.insert(tk.END, f"Host: {self.url_box.get()}\n")
        if request:
            self.request_text.insert(tk.END, f"Status Code: {request.status_code}\n")
        for key, value in headers.items():
            self.request_text.insert(tk.END, f"{key}: {value}\n")

    def handle_request_middle_button(self):
        if self.request_text.get("1.0", tk.END):
            new_headers = {}
            if self.headers:
                for line in self.request_text.get("1.0", tk.END).split("\n"):
                    if ": " in line:
                        key, value = line.split(": ", 1)
                        new_headers[key.strip()] = value.strip()

            self.response_box.delete_to_box(1.0, tk.END)
            request = self.http.handle_request(self.url_box.get(), new_headers)
            if request:
                self.headers = request.headers
            parser = RequestBoxParser(request)
            headers = parser.parse_request_box()
            self.response_box.insert_to_box(tk.END, f"Host: {self.url_box.get()}\n")
            if request:
                self.response_box.insert_to_box(
                    tk.END, f"Status Code: {request.status_code}\n"
                )
            for key, value in headers.items():
                self.response_box.insert_to_box(tk.END, f"{key}: {value}\n")
