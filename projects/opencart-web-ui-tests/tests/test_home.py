import allure
import pytest

from pages.home_page import HomePage


@allure.feature("首页")
@allure.story("首页访问")
@pytest.mark.smoke
def test_home_page_should_open_and_show_search_box(driver, config):
    """
    用例目标：
    1. 打开 OpenCart Demo 首页
    2. 校验搜索框可见
    """
    home_page = HomePage(driver, config)

    with allure.step("打开首页"):
        home_page.open_home_page()

    with allure.step("校验搜索框可见"):
        assert home_page.is_search_box_visible()

