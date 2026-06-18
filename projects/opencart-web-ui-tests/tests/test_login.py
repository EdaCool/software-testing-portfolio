import allure
import pytest

from pages.login_page import LoginPage


@allure.feature("登录")
@allure.story("登录页元素校验")
@pytest.mark.regression
def test_login_page_should_show_email_and_password_inputs(driver, config):
    """
    用例目标：
    1. 打开登录页
    2. 校验邮箱输入框和密码输入框存在
    """
    login_page = LoginPage(driver, config)

    with allure.step("打开登录页"):
        login_page.open_login_page()

    with allure.step("校验登录表单可见"):
        assert login_page.is_login_form_visible()


@allure.feature("登录")
@allure.story("错误账号登录")
@pytest.mark.regression
def test_login_with_invalid_account_should_not_success(driver, config):
    """
    用例目标：
    1. 输入错误账号密码
    2. 校验不会成功登录
    """
    login_page = LoginPage(driver, config)

    with allure.step("打开登录页"):
        login_page.open_login_page()

    with allure.step("输入错误账号密码并提交"):
        login_page.login("wrong_user@example.com", "wrong_password_123")

    with allure.step("校验仍然停留在登录相关页面"):
        assert "account/login" in driver.current_url or "login" in driver.page_source.lower()

