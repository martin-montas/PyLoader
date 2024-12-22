import socket
import ssl
import http.server
import urllib.request

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        target_url = self.path
        print(f"Forwarding GET request to: {target_url}")
        try:
            with urllib.request.urlopen(target_url) as response:
                self.send_response(response.status)

                for key, value in response.getheaders():
                    print(f"{key} is {value}")
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

    def do_CONNECT(self):
        host, port = self.path.split(":")
        port = int(port)

        try:
            upstream_socket = socket.create_connection((host, port))
            self.send_response(200)
            self.end_headers()
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile="/home/william/personal/pyloader.cer", keyfile="pyloader.key")
            client_ssl = context.wrap_socket(self.connection, server_side=True)
            self._tunnel_data(client_ssl, upstream_socket)
        except Exception as e:
            self.send_error(500, f"Failed to establish a connection: {e}")
    def _tunnel_data(self, client_socket, upstream_socket):
        import threading
        def forward(source, target):
            try:
                while True:
                    data = source.recv(4096)
                    if not data:
                        break
                    target.sendall(data)
            except:
                pass
            finally:
                source.close()
                target.close()
        threading.Thread(target=forward, args=(client_socket, upstream_socket), daemon=True).start()
        threading.Thread(target=forward, args=(upstream_socket, client_socket), daemon=True).start()
