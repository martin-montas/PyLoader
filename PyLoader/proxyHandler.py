import requests
import tkinter as tk


class HTTPHandler:
    def __init__(self):
        pass

    def handle_request(self, url, headers=None, body=None):
        """
        Send the modified request to the actual server.
        """
        try:
            if body:
                response = requests.post(url, headers=headers, data=body)
            else:
                response = requests.get(url, headers=headers)
                return response
        except requests.exceptions.RequestException as e:
            return str(e)


class RequestBoxParser:
    def __init__(self, response):
        self._response = response

    def parse_request_box(self):
        """
        Host: example.com
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
        Accept: text/html,application/xhtml+xml
        Content-Type: application/json
        """
        headers = {}
        for line in self._response.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()

        return headers