from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//input[@name='search']/following::button[1]")

    def open_home_page(self):
        self.open("")

    def is_search_box_visible(self):
        return self.is_visible(self.SEARCH_INPUT)

    def search_product(self, keyword):
        """
        在首页搜索商品。
        优先点击搜索按钮；如果按钮定位变化，则用 Enter 触发搜索。
        """
        search_input = self.wait_visible(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(keyword)

        try:
            self.click(self.SEARCH_BUTTON)
        except Exception:
            search_input.send_keys(Keys.ENTER)
