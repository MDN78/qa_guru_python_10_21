import pytest
from dotenv import load_dotenv
from utils import attach
from appium import webdriver
from selene import browser
from allure_commons._allure import step


def pytest_addoption(parser):
    parser.addoption('--context', default='local')


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f'.env.{context}'
    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    with step('Configurate options'):
        from project import config_app
        options = config_app.to_driver_options(context=context)
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
        browser.config.timeout = config_app.TIMEOUT
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


