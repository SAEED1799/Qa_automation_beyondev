from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class BrowserWrapper:
    def __init__(self, browser_name='chrome'):
        self.browser_name = browser_name
        self.driver = None

    def start_browser(self):
        if self.browser_name.lower() == 'chrome':
            self.driver = webdriver.Chrome(service=ChromeService(executable_path="/path/to/chromedriver"))
        elif self.browser_name.lower() == 'firefox':
            self.driver = webdriver.Firefox(service=FirefoxService(executable_path="/path/to/geckodriver"))
        elif self.browser_name.lower() == 'edge':
            self.driver = webdriver.Edge(service=EdgeService(executable_path="/path/to/msedgedriver"))
        else:
            raise ValueError("Invalid browser specified")

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def get_driver(self):
        if not self.driver:
            self.start_browser()
        return self.driver
