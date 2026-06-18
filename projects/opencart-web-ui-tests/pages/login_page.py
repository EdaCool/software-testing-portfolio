from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert-danger, .alert")

    def open_login_page(self):
        self.open("index.php?route=account/login")

    def is_login_form_visible(self):
        return self.is_visible(self.EMAIL_INPUT) and self.is_visible(self.PASSWORD_INPUT)

    def login(self, email, password):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_alert_message(self):
        return self.get_text(self.ALERT_MESSAGE)

