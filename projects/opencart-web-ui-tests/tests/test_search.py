import allure
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage


@allure.feature("商品搜索")
@allure.story("搜索有效关键词")
@pytest.mark.smoke
def test_search_mac_should_show_product_results(driver, config):
    """
    用例目标：
    1. 首页搜索 mac
    2. 校验搜索结果页有商品
    """
    home_page = HomePage(driver, config)
    search_page = SearchPage(driver, config)

    with allure.step("打开首页"):
        home_page.open_home_page()

    with allure.step("搜索商品关键词 mac"):
        home_page.search_product("mac")

    with allure.step("等待搜索页加载"):
        search_page.wait_until_loaded()

    with allure.step("校验搜索结果中存在商品"):
        assert search_page.has_product_results()


@allure.feature("商品搜索")
@allure.story("搜索无结果关键词")
@pytest.mark.regression
def test_search_unmatched_keyword_should_show_no_result(driver, config):
    """
    用例目标：
    1. 搜索一个极不可能存在的关键词
    2. 校验没有商品结果或页面有无结果提示
    """
    home_page = HomePage(driver, config)
    search_page = SearchPage(driver, config)

    keyword = "zzzzzz_no_such_product_123456"

    with allure.step("打开首页"):
        home_page.open_home_page()

    with allure.step(f"搜索不存在的商品关键词：{keyword}"):
        home_page.search_product(keyword)

    with allure.step("等待搜索页加载"):
        search_page.wait_until_loaded()

    with allure.step("校验无商品结果"):
        assert not search_page.has_product_results() or search_page.has_no_result_message()

