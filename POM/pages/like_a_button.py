from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.LINK_TEXT, 'Click')
result_text = (By.ID, 'result-text')
class LikeAButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/like_a_button')

    def button_is_displayed(self):
        return self.find(button_selector).is_displayed()

    def click_on_button(self):
        self.find(button_selector).click()

    @property
    def result_text(self):
        return self.find(result_text).text