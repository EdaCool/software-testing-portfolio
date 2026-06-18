from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1")
    PRICE_TEXT = (By.CSS_SELECTOR, ".price-new, .price, h2, ul.list-unstyled")
    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "#button-cart, button[formaction*='cart.add'], button[onclick*='cart.add'], button[type='submit']"
    )
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert-success, .alert, .toast, .alert-dismissible")

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def has_price(self):
        return self.is_visible(self.PRICE_TEXT)

    def has_add_to_cart_button(self):
        return self.is_visible(self.ADD_TO_CART_BUTTON)

    def add_to_cart(self):
        button = self.wait_clickable(self.ADD_TO_CART_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

    def wait_success_message(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda driver: len(driver.find_elements(*self.ALERT_MESSAGE)) > 0
            )
            return self.get_text(self.ALERT_MESSAGE)
        except TimeoutException:
            return ""

