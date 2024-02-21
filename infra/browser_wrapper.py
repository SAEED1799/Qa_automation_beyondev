import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class BrowserWrapper:
    try:
        with open('../tests/config.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
        raise  # Raise the error to halt execution if the file is essential for the script to run

    def __init__(self):
        self.browser_name = None
        self.driver = None

    def start_browser(self):
        self.browser_name = data.get("browser_name")
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

    def get_driver(self):
        if data.get("grid"):
            self.start_browser()
        return self.driver


