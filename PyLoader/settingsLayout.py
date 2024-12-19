import tkinter as tk
import socketserver
import threading

from PyLoader.proxyHandler import ProxyHandler
from PyLoader.stoppableThreads import StoppableThread

stop_event = threading.Event()
httpd_instance = None
curr_thread = None


def run_proxy_server(proxy_ip="127.0.0.1", proxy_port=8080):
    global httpd_instance
    global stop_event
    with socketserver.TCPServer((proxy_ip, proxy_port), ProxyHandler) as httpd:
        httpd_instance = httpd
        print(f"Serving proxy at {proxy_ip}:{proxy_port}")
        try:
            while not stop_event.is_set():
                httpd.handle_request()
        except Exception as e:
            print(f"Server stopped: {e}")
        finally:
            httpd_instance.shutdown()
            httpd_instance = None
            stop_event.set()


class SettingsLayout:
    def __init__(self, root) -> None:
        self.root = root
        tk.Label(self.root, text="Proxy IP").grid(row=0, column=0, padx=10, pady=10)
        self.proxy_ip_entry = tk.Entry(self.root)
        self.proxy_ip_entry.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.root, text="Proxy port").grid(row=2, column=0, padx=10, pady=10)
        self.proxy_port_entry = tk.Entry(self.root)
        self.proxy_port_entry.grid(row=3, column=0, padx=10, pady=10)

        tk.Button(
            self.root, text="Set Proxy", bg="orange", command=self.button_command
        ).grid(row=4, column=0, padx=10, pady=10)

        tk.Button(
            self.root,
            text="Disable Proxy",
            bg="orange",
            command=self.stop_proxy_server,
        ).grid(row=5, column=0, padx=10, pady=10)

    def button_command(self):
        global curr_thread, ip, port
        ip = self.proxy_ip_entry.get()
        port = self.proxy_port_entry.get()
        try:
            # Validate port input
            port = int(port)
            print(f"Starting proxy at IP: {ip}, Port: {port}")

            curr_thread = StoppableThread(target=run_proxy_server, args=(ip, port))
            curr_thread.start()

        except ValueError:
            print("Invalid port number. Please enter a valid integer.")

    def stop_proxy_server(self):
        global curr_thread
        if curr_thread:
            curr_thread.stop()
            print("Thread stopped!!!!")
