from browserstack_test.pages.main_page import main_page


def test_search_query_request():
    main_page.wiki_start_page()
    main_page.get_started_button()
