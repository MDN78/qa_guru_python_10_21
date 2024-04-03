import os
import allure
import pytest
from utils import attach
from selene import browser
from dotenv import load_dotenv
from allure_commons._allure import step
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    user_name = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": user_name,
            "accessKey": access_key
        }
    })
    browser.config.driver_remote_url = os.getenv('REMOTE_URL')
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('TIMEOUT'))

    yield

    with step('Add screenshot'):
        attach.add_screenshot(browser)

    with step('Add html'):
        attach.add_html(browser)

    with step('Add video'):
        attach.add_video(browser)

    with step('Close driver'):
        browser.quit()
