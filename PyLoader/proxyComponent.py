import http.server
import urllib.request

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Forward the GET request to the target URL
        target_url = self.path
        print(f"Forwarding GET request to: {target_url}")
        try:
            # Send the request to the target server
            with urllib.request.urlopen(target_url) as response:
                # Get the response data
                self.send_response(response.status)
                for key, value in response.getheaders():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            # Handle errors
            self.send_error(500, f"Error forwarding request: {e}")

    def do_POST(self):
        # Forward the POST request to the target URL
        target_url = self.path
        print(f"Forwarding POST request to: {target_url}")
        try:
            # Read the body of the POST request
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)

            # Create a request to the target server
            req = urllib.request.Request(target_url, data=body, method='POST')
            for key in self.headers:
                req.add_header(key, self.headers[key])

            # Send the request and get the response
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                for key, value in response.getheaders():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            # Handle errors
            self.send_error(500, f"Error forwarding request: {e}")


