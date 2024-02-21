from selenium.webdriver import Keys


class WebsiteInteractions:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get("https://www.365scores.com/he")

    def search_for_keyword(self, keyword):
        search_box = self.driver.find_element_by_id("search-input")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
