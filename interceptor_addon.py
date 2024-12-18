
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
