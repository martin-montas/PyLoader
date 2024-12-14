import tkinter as tk
import http.server
import socketserver
import urllib.request

# Store the server instance globally or pass it where needed
httpd_instance = None

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        target_url = self.path
        print(f"Forwarding GET request to: {target_url}")
        try:
            with urllib.request.urlopen(target_url) as response:
                self.send_response(response.status)
                for key, value in response.getheaders():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Error forwarding request: {e}")

    def do_POST(self):
        target_url = self.path
        print(f"Forwarding POST request to: {target_url}")
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)

            req = urllib.request.Request(target_url, data=body, method="POST")
            for key in self.headers:
                req.add_header(key, self.headers[key])

            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                for key, value in response.getheaders():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Error forwarding request: {e}")


def run_proxy_server(proxy_ip="127.0.0.1", proxy_port=8080):
    global httpd_instance
    # Create the proxy server
    with socketserver.TCPServer((proxy_ip, proxy_port), ProxyHandler) as httpd:
        httpd_instance = httpd
        print(f"Serving proxy at {proxy_ip}:{proxy_port}")
        try:
            httpd.serve_forever()
        except Exception as e:
            print(f"Server stopped: {e}")
        finally:
            httpd_instance = None

def stop_proxy_server():
    global httpd_instance
    if httpd_instance:
        print("Stopping the proxy server...")
        httpd_instance.shutdown()
        httpd_instance = None
    else:
        print("Proxy server is not running.")


class SettingsLayout:
    def __init__(self, root) -> None:
        self.root = root
        tk.Label(self.root,text="Proxy IP").grid(row=0,column=0,
        padx=10, pady=10)
        self.proxy_ip_entry = tk.Entry(self.root)
        self.proxy_ip_entry.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.root,text="Proxy port").grid(row=2,column=0,
        padx=10, pady=10)
        self.proxy_port_entry = tk.Entry(self.root)
        self.proxy_port_entry.grid(row=3, column=0, padx=10, pady=10)

        tk.Button(
            self.root, text="Set Proxy", bg="orange", command=self.button_command
        ).grid(row=4, column=0, padx=10, pady=10)

        tk.Button(
            self.root, text="Disable Proxy", bg="orange",
            command=stop_proxy_server,).grid(row=5, column=0, padx=10, pady=10)

    def button_command(self):
        ip = self.proxy_ip_entry.get()
        port = self.proxy_port_entry.get()
        try:
            # Validate port input
            port = int(port)
            print(f"Starting proxy at IP: {ip}, Port: {port}")
            run_proxy_server(ip, port)
        except ValueError:
            print("Invalid port number. Please enter a valid integer.")
