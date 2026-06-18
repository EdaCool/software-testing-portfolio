from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class SearchPage(BasePage):
    PRODUCT_LINKS = (
        By.CSS_SELECTOR,
        ".product-thumb h4 a, .product-thumb .description h4 a, a[href*='product_id=']"
    )

    def wait_until_loaded(self):
        """
        等待搜索页加载完成。
        搜索结果页可能有结果，也可能无结果，所以不能只等商品出现。
        """
        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: "search" in driver.current_url.lower()
            or "search" in driver.page_source.lower()
        )

    def product_links(self):
        return self.find_all(self.PRODUCT_LINKS)

    def has_product_results(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda driver: len(driver.find_elements(*self.PRODUCT_LINKS)) > 0
            )
            return True
        except TimeoutException:
            return False

    def first_product_name(self):
        links = self.product_links()
        if not links:
            raise AssertionError("No product link found on search result page.")
        return links[0].text.strip()

    def click_first_product(self):
        links = self.product_links()
        if not links:
            raise AssertionError("No product link found on search result page.")

        first = links[0]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first)
        first.click()

    def has_no_result_message(self):
        source = self.driver.page_source.lower()
        return (
            "no product" in source
            or "no results" in source
            or "there is no product" in source
        )

