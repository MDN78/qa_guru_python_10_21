import os
from utils import path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from appium.options.android import UiAutomator2Options


class Config(BaseSettings):
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    TIMEOUT: float = os.getenv('TIMEOUT')
    platformName: str = os.getenv('PLATFORM_NAME')
    platform_version: str = os.getenv('PLATFORM_VERSION')
    deviceName: str = os.getenv('DEVICE_NAME')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    URL: str = os.getenv('URL')
    app: str = os.getenv('APP')
    load_dotenv('.env.example')

    def to_driver_options(self, context):
        options = UiAutomator2Options()
        if context == 'local_emulator':
            options.set_capability('remote_url', self.URL)
            options.set_capability('platformName', self.platformName)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', path.relative_from_root(self.app))
        if context == 'bstack':
            options.set_capability('remote_url', self.URL)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options',
                {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    "userName": self.USER_NAME,
                    "accessKey": self.ACCESS_KEY,
                },
            )
            if context == 'local_real':
                options.set_capability('remote_url', self.remote_url)
                options.set_capability('appWaitActivity', self.app_wait_activity)
                options.set_capability('app', path.relative_from_root(self.app))

        return options


config_app = Config()
