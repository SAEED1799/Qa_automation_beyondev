import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.website_interactions import WebsiteInteractions
import pytest


class TestScore365(unittest.TestCase):
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = WebsiteInteractions.navigate_to_homepage

    def test_change_language(browser):
        browser.get("https://www.365scores.com/he")
        language_button = browser.find_element_by_id("language-selector")
        language_button.click()
        english_option = browser.find_element_by_xpath("//a[@data-lang='en']")
        english_option.click()
        assert "365Scores - Sports Scores" in browser.title


    def test_login(browser):
        browser.get("https://www.365scores.com/he")
        login_button = browser.find_element_by_id("login-button")
        login_button.click()
        # Fill in login form and submit
        email_input = browser.find_element_by_id("email-input")
        password_input = browser.find_element_by_id("password-input")
        submit_button = browser.find_element_by_id("login-submit-button")
        email_input.send_keys("your_email@example.com")
        password_input.send_keys("your_password")
        submit_button.click()
        # Verify successful login
        assert "Welcome" in browser.page_source

    def test_navigate_to_leagues(browser):
        browser.get("https://www.365scores.com/he")
        leagues_link = browser.find_element_by_xpath("//a[@href='/he/soccer/leagues']")
        leagues_link.click()
        assert "Leagues" in browser.title

    def test_homepage_title(browser):
        website = WebsiteInteractions(browser)
        website.navigate_to_homepage()
        assert "365Scores - ספורט בזמן אמת" in browser.title

    def test_search_soccer(browser):
        website = WebsiteInteractions(browser)
        website.navigate_to_homepage()
        website.search_for_keyword("כדורגל")
        assert "Search Results" in browser.title

    def test_search_basketball(browser):
        website = WebsiteInteractions(browser)
        website.navigate_to_homepage()
        website.search_for_keyword("כדורסל")
        assert "Search Results" in browser.title

    def test_search_tennis(browser):
        website = WebsiteInteractions(browser)
        website.navigate_to_homepage()
        website.search_for_keyword("טניס")
        assert "Search Results" in browser.title

    def test_search_volleyball(browser):
        website = WebsiteInteractions()
        website.navigate_to_homepage()
        website.search_for_keyword("כדורעף")
        assert "Search Results" in browser.title

        # When you're done, close the browser

    def tearDown(self):
        self.browser_wrapper.close_browser()
