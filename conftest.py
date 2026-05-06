import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.device_config import DEVICE_CONFIG, APPIUM_SERVER

@pytest.fixture(scope="session")
def driver():
    options = UiAutomator2Options()
    options.platform_name = DEVICE_CONFIG["platformName"]
    options.platform_version = DEVICE_CONFIG["platformVersion"]
    options.device_name = DEVICE_CONFIG["deviceName"]
    options.app_package = DEVICE_CONFIG["appPackage"]
    options.app_activity = DEVICE_CONFIG["appActivity"]
    options.no_reset = DEVICE_CONFIG["noReset"]
    options.auto_grant_permissions = DEVICE_CONFIG["autoGrantPermissions"]

    driver = webdriver.Remote(APPIUM_SERVER, options=options)
    yield driver
    driver.quit()