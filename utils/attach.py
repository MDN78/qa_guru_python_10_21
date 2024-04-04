import os
import allure
import requests
from allure_commons.types import AttachmentType


# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


# video
def add_video(browser):
    user_name = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{browser.driver.session_id}.json',
        auth=(user_name, access_key),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
