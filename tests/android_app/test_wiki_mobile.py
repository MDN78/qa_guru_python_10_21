from browserstack_test.pages.main_page import main_page


def test_search_query_request():
    main_page.search_request('Appium')
    main_page.checking_result('Appium')


def test_select_search_request():
    main_page.search_request('Appium')
    main_page.select_result_query()
