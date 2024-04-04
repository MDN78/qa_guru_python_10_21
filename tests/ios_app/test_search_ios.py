from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy

def test_search_ios_platform():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys("QaGuru" + '\n')
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("QaGuru"))