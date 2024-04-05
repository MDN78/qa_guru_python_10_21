from browserstack_test.pages.main_page import main_page


def test_search_ios_platform():
    main_page.search_request_ios("QaGuru")
    main_page.checking_result_ios("QaGuru")
