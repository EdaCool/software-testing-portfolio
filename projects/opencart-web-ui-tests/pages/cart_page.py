from pages.base_page import BasePage


class CartPage(BasePage):
    def open_cart_page(self):
        self.open("index.php?route=checkout/cart")

    def is_cart_page_opened(self):
        source = self.driver.page_source.lower()
        return "shopping cart" in source or "cart" in source

    def contains_product(self, product_name):
        return product_name.lower() in self.driver.page_source.lower()

