import pytest
from selenium import webdriver
from datetime import datetime


@pytest.fixture
def driver():
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_name = f"screenshot_{timestamp}.png"

        driver.save_screenshot(screenshot_name)

        print(f"\nScreenshot saved: {screenshot_name}")