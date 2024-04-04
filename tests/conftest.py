import pytest
import project
from utils import attach
from appium import webdriver
from selene import browser
from allure_commons._allure import step
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options

DEFAULT_PLATFORM_NAME = 'android'


@step('Select palform type')
def pytest_addoption(parser):
    parser.addoption('--platform_name', default='android')


@step('load env')
@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    with step('Configurate options'):
        platform_name = request.config.getoption('--platform_name')
        platform_name = platform_name if platform_name != '' else DEFAULT_PLATFORM_NAME
        if platform_name.lower() == 'android':
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
        elif platform_name.lower() == 'ios':
            options = XCUITestOptions().load_capabilities({
                # Specify device and os_version for testing
                "deviceName": "iPhone 11 Pro",
                "platformName": "ios",
                "platformVersion": "13",

                # Set URL of the application under test
                "app": "bs://sample.app",

                # Set other BrowserStack capabilities
                'bstack:options': {
                    "projectName": "Second Python project",
                    "buildName": "browserstack-build-2",
                    "sessionName": "BStack second_test",

                    # Set your access credentials
                    "userName": project.config.USER_NAME,
                    "accessKey": project.config.ACCESS_KEY
                }
            })

    browser.config.driver = webdriver.Remote(project.config.URL, options=options)
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
