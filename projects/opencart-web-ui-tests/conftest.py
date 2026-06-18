from pathlib import Path

import allure
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


PROJECT_ROOT = Path(__file__).parent


@pytest.fixture(scope="session")
def config():
    """
    读取 config/config.yaml。
    scope='session' 表示整个测试会话只读取一次配置。
    """
    config_path = PROJECT_ROOT / "config" / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


@pytest.fixture
def driver(config):
    """
    创建并关闭浏览器。
    每个测试用例开始前创建 Chrome，测试结束后关闭 Chrome。
    """
    browser = config.get("browser", "chrome").lower()
    headless = config.get("headless", True)

    if browser != "chrome":
        raise ValueError(f"Unsupported browser in WSL2 project: {browser}")

    options = ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    # WSL2 / Linux 容器或无界面环境常用参数
    options.add_argument("--window-size=1440,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest hook：当测试用例失败时自动截图。
    截图保存在 screenshots 目录，并附加到 Allure 报告里。
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            screenshots_dir = PROJECT_ROOT / "screenshots"
            screenshots_dir.mkdir(exist_ok=True)

            screenshot_name = f"{item.name}.png"
            screenshot_path = screenshots_dir / screenshot_name

            driver.save_screenshot(str(screenshot_path))

            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name=screenshot_name,
                    attachment_type=allure.attachment_type.PNG
                )

