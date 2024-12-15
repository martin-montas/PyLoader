import tkinter as tk
import threading
import urllib.request
import urllib.error
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

# Proxy handler to intercept and forward HTTP requests
class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        # Log the incoming request
        print(f"Intercepted {self.command} request to {self.path}")

        # Parse the destination URL
        url = f"http://{self.headers['Host']}{self.path}"
        headers = {key: value for key, value in self.headers.items()}
        body = self.rfile.read(int(self.headers.get('Content-Length', 0))) if self.command == 'POST' else None

        try:
            # Forward the request to the destination
            if self.command == 'GET':
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req) as response:
                    self._send_response(response)
            elif self.command == 'POST':
                req = urllib.request.Request(url, data=body, headers=headers, method="POST")
                with urllib.request.urlopen(req) as response:
                    self._send_response(response)
        except urllib.error.URLError as e:
            self.send_error(500, f"Error forwarding request: {e}")

    def _send_response(self, response):
        # Send the HTTP response back to the client
        self.send_response(response.status)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.read())

# Start the proxy server
def start_proxy_server(host='127.0.0.1', port=8080):
    server_address = (host, port)
    httpd = HTTPServer(server_address, ProxyHandler)
    print(f"Starting proxy server on {host}:{port}")
    httpd.serve_forever()

# Start the proxy server in a separate thread
if __name__ == "__main__":
    proxy_thread = threading.Thread(target=start_proxy_server, daemon=True)
    proxy_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Proxy server stopped.")

port = 8080
ip = "127.0.0.1"

class SettingsLayout:
    def __init__(self, root) -> None:
        self.root = root
        tk.Label(self.root, text="Proxy IP").grid(row=0, column=0, padx=10, pady=10)
        self.proxy_ip_entry = tk.Entry(self.root)
        self.proxy_ip_entry.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.root, text="Proxy port").grid(row=2, column=0, padx=10, pady=10)
        self.proxy_port_entry = tk.Entry(self.root)
        self.proxy_port_entry.grid(row=3, column=0, padx=10, pady=10)

        tk.Button(self.root, text="Set Proxy", bg="orange", command=self.button_command).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Disable Proxy", bg="orange" ).grid(row=5, column=0, padx=10, pady=10)

    def button_command(self):
        global ip, port
        ip = self.proxy_ip_entry.get()
        port = self.proxy_port_entry.get()


