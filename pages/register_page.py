from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "https://practicesoftwaretesting.com/auth/register"
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    DOB = (By.ID, "dob")
    POSTAL_CODE = (By.ID, "postal_code")
    HOUSE_NUMBER = (By.ID, "house_number")
    STREET = (By.ID, "street")
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    PHONE = (By.ID, "phone")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    COUNTRY = (By.ID, "country")
    REG_BUTTON = (By.CSS_SELECTOR, "[data-test='register-submit']")
    # REG_BUTTON = (By.CLASS_NAME, "btnSubmit.mb-3")


    
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, "[data-test='first-name-error']")
    LAST_NAME_ERROR = (By.CSS_SELECTOR, "[data-test='last-name-error']")
    DOB_ERROR = (By.CSS_SELECTOR, "[data-test='dob-error']")
    COUNTRY_ERROR = (By.CSS_SELECTOR, "[data-test='country-error']")
    COUNTRY_INFO = (By.CSS_SELECTOR, "[data-test='postcode-lookup-hint']")
    POSTAL_CODE_ERROR = (By.CSS_SELECTOR, "[data-test='postal_code-error']")
    EMAIL_ERROR = (By.CSS_SELECTOR, "[data-test='email-error']")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "[data-test='password-error']")



    def input_first_name(self, text):
        self.type(self.FIRST_NAME, text)

    def input_last_name(self, text):
        self.type(self.LAST_NAME, text)

    def input_dob(self, text):
        self.type(self.DOB, text)

    def input_postal_code(self, text):
        self.type(self.POSTAL_CODE, text)

    def input_house_number(self, text):
        self.type(self.HOUSE_NUMBER, text)

    def input_street(self, text):
        self.type(self.STREET, text)

    def input_city(self, text):
        self.type(self.CITY, text)

    def input_state(self, text):
        self.type(self.STATE, text)

    def input_phone(self, text):
        self.type(self.PHONE, text)

    def input_email(self, text):
        self.type(self.EMAIL, text)

    def input_password(self, text):
        self.type(self.PASSWORD, text)

    def select_country(self, country):
        dropdown = Select(self.find(self.COUNTRY))
        dropdown.select_by_visible_text(country)   

    def click_register(self):
        self.wait_clickable(self.REG_BUTTON)
        self.click(self.REG_BUTTON)


    def get_first_name_error(self, text):
        self.find(self.FIRST_NAME_ERROR)
        self.get_text(self.FIRST_NAME_ERROR, text)


    def get_last_name_error(self, text):
        self.find(self.LAST_NAME_ERROR)
        self.get_text(self.LAST_NAME_ERROR, text)


    def get_dob_error(self):
        self.wait_visible(self.DOB_ERROR)
        return self.get_text(self.DOB_ERROR)

        
    def get_country_error(self, text):
        self.find(self.COUNTRY_ERROR)
        self.get_text(self.COUNTRY_ERROR, text)


    def get_country_error(self, text):
        self.find(self.COUNTRY_INFO)
        self.get_text(self.COUNTRY_INFO, text)

        
    def get_postal_code_error(self, text):
        self.find(self.POSTAL_CODE_ERROR)
        self.get_text(self.POSTAL_CODE_ERROR, text)


    def get_email_error(self, text):
        self.find(self.EMAIL_ERROR)
        self.get_text(self.EMAIL_ERROR, text)


    def get_password_error(self, text):
        self.find(self.PASSWORD_ERROR)
        self.get_text(self.PASSWORD_ERROR, text)


    def get_password_strength_text(self, text):
        self.find(self.PASSWORD_ERROR)
        self.get_text(self.PASSWORD_ERROR, text)
                

    
    # def fill_all_data(self, user):
    #     self.input_first_name(user["first_name"])
    #     self.input_last_name(user["last_name"])
    #     self.input_dob(user["dob"])
    #     self.select_country(user["country"])
    #     self.input_postal_code(user["postal_code"])
    #     self.input_house_number(user["house_number"])
    #     # self.input_street(user["street"])
    #     # self.input_city(user["city"])
    #     # self.input_state(user["state"])        
    #     self.input_phone(user["phone"])
    #     self.input_email(user["email"])
    #     self.input_password(user["password"])
    #     self.click_register()
            