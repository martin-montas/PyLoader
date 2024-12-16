import tkinter as tk
from mitmproxy import http


def request_handler():
    def request(flow: http.HTTPFlow) -> None:
        '''
        This hook is triggered for every HTTP request.
        '''
        print(f"Request: {flow.request.method} {flow.request.url}")
        #flow.request.host = 
        flow.request.port =  8080

def response(flow: http.HTTPFlow) -> None:
    '''
    This hook is triggered for every HTTP response.
    '''

    if flow.response:
        print(f"Response: {flow.request.url} - Status: {flow.response.status_code}")

class SettingsLayout:
    def __init__(self, root) -> None:
        global ip, port

        self.root = root
        tk.Label(self.root, text="Proxy IP").grid(row=0, column=0, padx=10, pady=10)
        ip= tk.Entry(self.root)
        ip.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.root, text="Proxy port").grid(row=2, column=0, padx=10, pady=10)
        port = tk.Entry(self.root)
        port.grid(row=3, column=0, padx=10, pady=10)

        tk.Button(self.root, text="Set Proxy", bg="orange", command=lambda: start_proxy(ip,port)).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Disable Proxy", bg="orange" ).grid(row=5, column=0, padx=10, pady=10)

def start_proxy(ip,port):
    port.get()
    ip.get()
