import os
from dotenv import load_dotenv
from utils import path
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    TIMEOUT: float = os.getenv('TIMEOUT')
    # CONTEXT: list = os.getenv('CONTEXT')
    # # app: str = path.relative_from_root('apk_file/org-wikipedia.apk')
    platformName: str = os.getenv('PLATFORM_NAME')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    URL: str = os.getenv('URL')
    # app: str = "D:\\QAGuru\\org-wikipedia.apk"
    app: str = path.relative_from_root('apk_file/org-wikipedia.apk')

config = Config(_env_file=path.relative_from_root(f'.env.{Config()}'))


# class Config_local(BaseSettings):
#     load_dotenv('.env.local_emulator')
#     platformName: str = os.getenv('PLATFORM_NAME')
#     appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
#     app: str = path.relative_from_root('apk_file/org-wikipedia.apk')
#     URL: str = os.getenv('URL')
#
# config_local = Config_local(_env_file=path.relative_from_root(f'.env.local_emulator.{Config_local()}'))