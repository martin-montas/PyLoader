import tkinter as tk
import socket
import socketserver
import threading
from datetime import datetime

from PyLoader.proxyHandler import ProxyHandler


RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

class ThreadedTCPServer(socketserver.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = True

class ProxyServer:
    def __init__(self, proxy_ip, proxy_port):
        self._proxy_ip = proxy_ip
        self._proxy_port = proxy_port
        self._thread = None
        self._stop_event = threading.Event()
        self._server = None
    def start(self):
        if self._thread is None:
            self._thread = threading.Thread(target=self._run_server)
            self._thread.daemon = True
            self._thread.start()
    def stop(self):
        if self._thread and self._server:
            self._stop_event.set()
            self._server.shutdown()
            self._server.server_close()
            self._thread.join()
            self._thread = None
            self._server = None
            self._stop_event.clear()
    def _run_server(self):
        current_time = datetime.now().time()
        try:
            self._server = ThreadedTCPServer((self._proxy_ip, self._proxy_port), ProxyHandler)
            try:
                self._server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            except AttributeError:
                pass
            print(f"{current_time} {BLUE}[INFO]{RESET} Serving proxy at {self._proxy_ip}:{self._proxy_port}")
            while not self._stop_event.is_set():
                self._server.serve_forever()
            self._server.shutdown()

        except Exception as e:
            print(f"{current_time} {RED}[ERROR]{RESET} Error running proxy server: {e}")
        finally:
            if self._server:
                try:
                    self._server.server_close()
                except Exception as e:
                    print(f"{current_time}{current_time} {RED}[ERROR]{RESET} Error closing server: {e}")

class SettingsLayout:
    def __init__(self, root):
        self.root = root
        self.proxy_server = None
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.status_var = tk.StringVar(value="Status: Stopped")
        self.status_label = tk.Label(main_frame, textvariable=self.status_var)
        self.status_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        tk.Label(main_frame, text="Proxy IP:").grid(row=1, column=0, sticky="w")
        self.proxy_ip_entry = tk.Entry(main_frame)
        self.proxy_ip_entry.insert(0, "127.0.0.1")
        self.proxy_ip_entry.grid(row=1, column=1, sticky="ew", padx=(10, 0))
        tk.Label(main_frame, text="Proxy Port:").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.proxy_port_entry = tk.Entry(main_frame)
        self.proxy_port_entry.insert(0, "8080")
        self.proxy_port_entry.grid(row=2, column=1, sticky="ew", padx=(10, 0), pady=(10, 0))
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(20, 0))
        self.start_button = tk.Button(
            button_frame,
            text="Start Proxy",
            command=self.start_proxy,
            width=12
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(
            button_frame,
            text="Stop Proxy",
            command=self.stop_proxy,
            width=12,
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def start_proxy(self):
        if self.proxy_server:
            self.stop_proxy()
        ip = self.proxy_ip_entry.get()
        port = self.proxy_port_entry.get()
        try:
            port = int(port)
            self.proxy_server = ProxyServer(ip, port)
            self.proxy_server.start()
            current_time = datetime.now().time()
            self.status_var.set(f"Status: Running on {ip}:{port}")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.proxy_ip_entry.config(state=tk.DISABLED)
            self.proxy_port_entry.config(state=tk.DISABLED)
        except ValueError:
            current_time = datetime.now().time()
            print(f"{current_time} {RED}[ERROR]{RESET} Invalid port number. Please enter a valid integer.")
            self.status_var.set(f"Invalid port number. Please enter a valid integer{ip}:{port}")
        except Exception as e:
            current_time = datetime.now().time()
            print(f"{current_time} {RED}[ERROR] {RESET} Error starting proxy: {e}")

    def stop_proxy(self):
        if self.proxy_server:
            try:
                self.proxy_server.stop()
            except Exception as e:
                current_time = datetime.now().time()
                print(f"{current_time} {RED} [ERROR]{RESET} Error stopping proxy: {e}")
            finally:
                self.proxy_server = None
                self.status_var.set("Status: Stopped")
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                self.proxy_ip_entry.config(state=tk.NORMAL)
                self.proxy_port_entry.config(state=tk.NORMAL)
