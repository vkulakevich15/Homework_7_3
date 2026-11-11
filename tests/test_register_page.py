from data.users import REGISTER_USER
from pages.register_page import RegisterPage


def test_successful_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER)
    page.wait_page_changed(driver.current_url)
    assert "login" in driver.current_url


def test_first_name_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_first_name("")
    page.click_register()
    assert page.get_text(page.FIRST_NAME_ERROR) == "First name is required"


def test_last_name_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_last_name("")
    page.click_register()
    assert page.get_text(page.LAST_NAME_ERROR) == "Last name is required"


def test_dob_invalid_format_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_dob("123")
    page.click_register()
    assert page.get_dob_error() == "Please enter a valid date in YYYY-MM-DD format."


def test_country_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    assert page.get_text(page.COUNTRY_ERROR) == "Country is required"


def test_select_country_info_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.select_country("Palau")
    assert page.get_text(page.COUNTRY_INFO) == (
        "Choose your country and enter the postal code and house number. "
        "Street, city and state will be filled in automatically."
    )


def test_postal_code_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_postal_code("")
    page.click_register()
    assert page.get_text(page.POSTAL_CODE_ERROR) == "Postcode is required"


def test_email_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_email("")
    page.click_register()
    assert page.get_text(page.EMAIL_ERROR) == "Email is required"


def test_email_without_at_sign_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_email("testmail.ru")
    page.click_register()
    assert page.get_text(page.EMAIL_ERROR) == "Email format is invalid"


def test_email_without_domain_part_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_email("test@")
    page.click_register()
    assert page.get_text(page.EMAIL_ERROR) == "Email format is invalid"


def test_email_without_local_part_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_email("@mail.ru")
    page.click_register()
    assert page.get_text(page.EMAIL_ERROR) == "Email format is invalid"


def test_password_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_password("")
    page.click_register()
    assert page.get_text(page.PASSWORD_ERROR) == (
        "Password is required\n"
        "Password must be minimal 6 characters long.\n"
        "Password can not include invalid characters."
    )