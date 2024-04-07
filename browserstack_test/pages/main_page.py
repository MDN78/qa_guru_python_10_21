from selene import browser, have
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:

    def wiki_start_page(self):
        with step('First wellcome screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()
        with step(f'Checking second page'):
            browser.element((AppiumBy.ID, "org.wikipedia:id/view_onboarding_page_primary_text")).should(
                have.text('New ways to explore'))
        with step('Go to nex page'):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()
        with step(f'Checking third page'):
            browser.element((AppiumBy.ID, "org.wikipedia:id/view_onboarding_page_primary_text")).should(
                have.text('Reading lists with sync'))
        with step('Go to nex page'):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()
        with step(f'Checking fourth page'):
            browser.element((AppiumBy.ID, "org.wikipedia:id/view_onboarding_page_primary_text")).should(
                have.text('Send anonymous data'))

    def get_started_button(self):
        with step('Go to main page'):
            browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_done_button')).click()
        with step(f'Checking fourth page'):
            browser.element((AppiumBy.ID, "org.wikipedia:id/view_announcement_text")).should(
                have.text('Sync reading lists'))


main_page = MainPage()
