from data.users import REGISTER_USER
from pages.register_page import RegisterPage


def test_successful_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER)
    page.wait_page_changed(driver.current_url)
    assert "login" in driver.current_url
