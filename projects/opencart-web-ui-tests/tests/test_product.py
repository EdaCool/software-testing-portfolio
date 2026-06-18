import allure
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage


@allure.feature("商品详情")
@allure.story("从搜索结果进入商品详情页")
@pytest.mark.smoke
def test_open_first_product_detail_from_search_result(driver, config):
    """
    用例目标：
    1. 搜索 mac
    2. 点击第一个商品
    3. 校验商品详情页标题存在
    4. 校验加入购物车按钮存在
    """
    home_page = HomePage(driver, config)
    search_page = SearchPage(driver, config)
    product_page = ProductPage(driver, config)

    with allure.step("打开首页"):
        home_page.open_home_page()

    with allure.step("搜索商品 mac"):
        home_page.search_product("mac")

    with allure.step("等待搜索结果加载"):
        search_page.wait_until_loaded()
        assert search_page.has_product_results()

    with allure.step("点击第一个商品"):
        search_page.click_first_product()

    with allure.step("校验商品详情页标题不为空"):
        title = product_page.get_product_title()
        assert title != ""

    with allure.step("校验商品详情页存在加入购物车按钮"):
        assert product_page.has_add_to_cart_button()

