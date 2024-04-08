import os
from dotenv import load_dotenv
from utils import path
from pydantic_settings import BaseSettings
from appium.options.android import UiAutomator2Options


class Config(BaseSettings):
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    TIMEOUT: float = os.getenv('TIMEOUT')
    platformName: str = os.getenv('PLATFORM_NAME')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    URL: str = os.getenv('URL')
    app: str = path.relative_from_root('apk_file/org-wikipedia.apk')
    load_dotenv('.env.example')

    def to_driver_options(self, context):
        options = UiAutomator2Options()
        if context == 'local':
            options.set_capability('remote_url', self.URL)
            options.set_capability("platformName", self.platformName)
            options.set_capability("appWaitActivity", self.appWaitActivity)
            options.set_capability("app", self.app)
        return options


config_app = Config()
