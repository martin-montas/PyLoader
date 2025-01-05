import requests


class HTTPHandler:
    def __init__(self):
        pass

    def handle_request(self, url, headers=None, body=None):
        '''
        Send the modified request to the actual server.
        '''
        try:
            if not (url.startswith("http://") or url.startswith("https://")):
                url = "https://" + str(url)

            if body:
                return requests.post(url, headers=headers, data=body)
            else:
                return requests.get(url, headers=headers)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


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

        return self._response.headers
