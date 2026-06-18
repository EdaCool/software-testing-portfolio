import allure
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@allure.feature("购物车")
@allure.story("加入购物车并校验购物车页面")
@pytest.mark.optional
@pytest.mark.xfail(strict=False, reason="官方 Demo 环境购物车流程可能因 session、弹窗或页面变化而不稳定")
def test_add_first_product_to_cart_and_check_cart_page(driver, config):
    """
    用例目标：
    1. 搜索 mac
    2. 进入第一个商品详情页
    3. 点击加入购物车
    4. 打开购物车页面
    5. 校验购物车页面打开成功
    """
    home_page = HomePage(driver, config)
    search_page = SearchPage(driver, config)
    product_page = ProductPage(driver, config)
    cart_page = CartPage(driver, config)

    with allure.step("打开首页"):
        home_page.open_home_page()

    with allure.step("搜索商品 mac"):
        home_page.search_product("mac")

    with allure.step("进入第一个商品详情页"):
        search_page.wait_until_loaded()
        assert search_page.has_product_results()
        search_page.click_first_product()

    with allure.step("获取商品标题"):
        product_title = product_page.get_product_title()
        assert product_title != ""

    with allure.step("点击加入购物车"):
        product_page.add_to_cart()

    with allure.step("等待成功提示"):
        message = product_page.wait_success_message()
        assert message == "" or "success" in message.lower() or "cart" in message.lower()

    with allure.step("打开购物车页面"):
        cart_page.open_cart_page()

    with allure.step("校验购物车页面打开成功"):
        assert cart_page.is_cart_page_opened()

