# conftest.py
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    """每个测试用例启动一次driver"""
    desired_caps = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:62001",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "noReset": True
    }
    # 将配置加载到 options 中
    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    yield driver
    driver.quit()