from selene import browser, have
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:

    def search_request(self, query):
        with step(f'ANDROID: Search request by word {query}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(query)

    def search_request_ios(self, query):
        with step(f'iOS: Searsh request by word {query}'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys(query + '\n')

    def checking_result_ios(self, query):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text(query))

    def select_result_query(self):
        with step('ANDROID: Select request result'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()

    def checking_result(self, query):
        with step(f'ANDROID: Checking request result by word {query}'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(query))


main_page = MainPage()
