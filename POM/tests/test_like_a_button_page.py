from selenium.webdriver.common.by import By
from pages.like_a_button import LikeAButtonPage

def test_button2_exist(browser):
    like_a_button_page = LikeAButtonPage(browser)
    like_a_button_page.open()
    assert like_a_button_page.button_is_displayed()

def test_button2_clicked(browser):
    like_a_button_page = LikeAButtonPage(browser)
    like_a_button_page.open()
    like_a_button_page.click_on_button()
    assert 'Submitted' == browser.find_element(By.ID, 'result-text').text