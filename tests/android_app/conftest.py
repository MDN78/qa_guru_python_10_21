import pytest
import project
from utils import attach
from selene import browser
from allure_commons._allure import step
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with step('Configurate options'):
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
                "userName": project.config.USER_NAME,
                "accessKey": project.config.ACCESS_KEY
            }
        })
    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    # browser.config.timeout = 10
    browser.config.timeout = project.config.TIMEOUT

    yield

    with step('Add screenshot'):
        attach.add_screenshot(browser)

    with step('Add html'):
        attach.add_html(browser)

    with step('Add video'):
        attach.add_video(browser)

    with step('Close driver'):
        browser.quit()
