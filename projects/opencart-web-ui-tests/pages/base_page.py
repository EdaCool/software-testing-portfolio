from urllib.parse import urljoin

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    所有 Page Object 的父类。
    这里封装 Selenium 常用操作，减少重复代码。
    """

    def __init__(self, driver, config):
        self.driver = driver
        self.base_url = config["base_url"].rstrip("/") + "/"
        self.timeout = config.get("timeout", 20)

    def open(self, path=""):
        """
        打开页面。
        path 可以为空，也可以是 index.php?route=xxx。
        """
        target_url = urljoin(self.base_url, path)
        self.driver.get(target_url)

    def wait_visible(self, locator):
        """
        等待元素可见。
        locator 示例：(By.NAME, "search")
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        """
        等待元素可点击。
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def find_all(self, locator):
        """
        查找多个元素。
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        点击元素。
        """
        self.wait_clickable(locator).click()

    def input_text(self, locator, text):
        """
        输入文本。
        """
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        获取元素文本。
        """
        return self.wait_visible(locator).text.strip()

    def is_visible(self, locator):
        """
        判断元素是否可见。
        """
        try:
            self.wait_visible(locator)
            return True
        except TimeoutException:
            return False

    def page_contains(self, text):
        """
        判断页面源码中是否包含某段文本。
        """
        return text.lower() in self.driver.page_source.lower()

    def wait_page_contains(self, text):
        """
        等待页面中出现某段文本。
        """
        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: text.lower() in driver.page_source.lower()
        )

