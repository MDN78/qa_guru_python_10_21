import pytest
from dotenv import load_dotenv
from utils import attach
from appium import webdriver
from selene import browser
from allure_commons._allure import step


def pytest_addoption(parser):
    parser.addoption('--context', default='local_emulator')


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
