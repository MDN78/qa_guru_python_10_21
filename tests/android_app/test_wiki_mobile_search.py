from browserstack_test.pages.main_page import main_page


def test_select_search_request():
    main_page.search_request('Java')
    main_page.select_result_query()
