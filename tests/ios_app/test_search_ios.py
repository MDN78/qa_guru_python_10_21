from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy
from browserstack_test.pages.main_page import main_page


# def test_search_ios_platform():
#     browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
#     browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys("QaGuru" + '\n')
#     browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("QaGuru"))

def test_search_ios_platform():
    main_page.search_request_ios("QaGuru")
    main_page.checking_result_ios("QaGuru")
