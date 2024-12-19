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
                    # TODO(martin-montas) Take this get headers functio
                    # and display it in the Text area of the repeaters
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
                    # TODO(martin-montas) Take this get headers
                    # and display it in the Text area of the repeaters
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Error forwarding request: {e}")
