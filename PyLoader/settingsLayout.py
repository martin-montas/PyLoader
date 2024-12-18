import tkinter as tk
import threading
import subprocess
from mitmproxy import http

# Global variables
ip = "127.0.0.1"
port = 8080
stop_event = threading.Event()
mitmproxy_process = None  # To store the mitmproxy subprocess

# Interceptor class to intercept HTTP requests and responses
class Interceptor:
    def request(self, flow: http.HTTPFlow) -> None:
        print(f"Request URL: {flow.request.url}")
        # You can modify the request here if needed

    def response(self, flow: http.HTTPFlow) -> None:
        print(f"Response URL: {flow.request.url}")
        # You can modify the response here if needed

# Write a temporary mitmproxy addon script
def write_addon_script():
    addon_script = """
from mitmproxy import http

class Interceptor:
    def request(self, flow: http.HTTPFlow) -> None:
        print(f"Request URL: {flow.request.url}")
        # You can modify the request here if needed

    def response(self, flow: http.HTTPFlow) -> None:
        print(f"Response URL: {flow.request.url}")
        # You can modify the response here if needed

addons = [
    Interceptor()
]
"""
    script_path = "interceptor_addon.py"
    with open(script_path, "w") as f:
        f.write(addon_script)
    return script_path

# Run the proxy server using subprocess
def start_proxy():
    global ip, port, mitmproxy_process
    port = str(port)
    
    # Write the addon script to a temporary file
    addon_script_path = write_addon_script()
    
    # Start mitmproxy with the addon script as a parameter
    options = [
        "mitmproxy",  # This is the mitmproxy command
        "--listen-host", ip,
        "--listen-port", str(port),
        "--mode", "regular",
        "-s", addon_script_path  # Specify the addon script
    ]
    
    # Start mitmproxy as a subprocess
    mitmproxy_process = subprocess.Popen(options, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"mitmproxy started on {ip}:{port}")

# Stop the mitmproxy process
def stop_proxy():
    global mitmproxy_process
    if mitmproxy_process:
        mitmproxy_process.terminate()  # Terminate the subprocess
        mitmproxy_process = None
        print("mitmproxy process terminated.")
    else:
        print("mitmproxy process not running.")

class SettingsLayout:
    def __init__(self, root) -> None:
        global ip, port

        self.root = root
        tk.Label(self.root, text="Proxy IP").grid(row=0, column=0, padx=10, pady=10)
        self.ip = tk.Entry(self.root)
        self.ip.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.root, text="Proxy port").grid(row=2, column=0, padx=10, pady=10)
        self.port = tk.Entry(self.root)
        self.port.grid(row=3, column=0, padx=10, pady=10)

        # Start Proxy button
        tk.Button(self.root, text="Set Proxy", bg="orange", command=self.start_proxy).grid(row=4, column=0, padx=10, pady=10)

        # Disable Proxy button
        tk.Button(self.root, text="Disable Proxy", bg="orange", command=self.stop_proxy).grid(row=5, column=0, padx=10, pady=10)

    def start_proxy(self):
        global port, ip

        # Get the user-provided IP and port
        port = self.port.get()
        ip = self.ip.get()

        # Start mitmproxy in a new background thread
        proxy_thread = threading.Thread(target=self.run_proxy_in_thread, daemon=True)
        proxy_thread.start()
        print("mitmproxy started in a new thread.")

    def run_proxy_in_thread(self):
        # Run the proxy in the background and pass the Interceptor addon
        start_proxy()

    def stop_proxy(self):
        # Stop mitmproxy gracefully
        stop_proxy()

