import pytest
import project
from utils import path
from utils import attach
from appium import webdriver
from selene import browser
from allure_commons._allure import step
from appium.options.android import UiAutomator2Options

DEFAULT_CONTEXT = 'local'

def pytest_addoption(parser):
    parser.addoption('--context', default='local')

# @pytest.fixture
# def context(request):
#     return request.config.getoption("--context")

@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    with step('Configurate options'):
        context = request.config.getoption('--context')
        context = context if context != '' else DEFAULT_CONTEXT
        if context == 'local':
            options = UiAutomator2Options()
            # options.set_capability('remote_url', project.config.URL)
            options.set_capability("platformName", project.config.platformName)
            options.set_capability("appWaitActivity", project.config.appWaitActivity)
            options.set_capability("app", project.config.app)
        browser.config.driver = webdriver.Remote(project.config.URL, options=options)
        browser.config.timeout = project.config.TIMEOUT
    #     options = UiAutomator2Options().load_capabilities({
    #         # Specify device and os_version for testing
    #         "platformName": "Android",
    #         "appWaitActivity": "org.wikipedia.*",
    #         # Set URL of the application under test
    #         "app": "D:\\QAGuru\\org-wikipedia.apk",
    #         # "app": path.relative_from_root('apk_file/org-wikipedia.apk'),
    #
    #     })
    #
    # browser.config.driver = webdriver.Remote(project.config.URL, options=options)
    # browser.config.timeout = project.config.TIMEOUT

    yield

    with step('Add screenshot'):
        attach.add_screenshot(browser)

    # with step('Add html'):
    #     attach.add_html(browser)
    #
    # with step('Add video'):
    #     attach.add_video(browser)

    with step('Close driver'):
        browser.quit()
