from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options

class CustomProxy:
    def __init__(self, url):
        # Initialize Proxy and Options
        self.proxy = Proxy()
        self.url = url
        self.options = Options()

        # Configure the proxy
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = "localhost:8080"
        self.proxy.ssl_proxy = "localhost:8080"

        # Set the proxy capabilities
        self.options.set_capability("proxy", self.proxy.to_capabilities())

        # Initialize the WebDriver with the configured options
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get(self.url)
        # Perform actions, mitmproxy will intercept the traffic
