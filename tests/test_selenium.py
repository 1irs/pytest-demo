import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_object.main_page import MainPage


@pytest.fixture(scope="module")
def get_main_page() -> MainPage:
    # Выполняется до теста (аналог setUp  или setUpClass, если scope="module")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(driver)

    # Временно возвращаем управление в pytest
    yield main_page

    # Выполняется после теста (аналог tearDown или tearDownClass, если scope="module")
    driver.quit()


TEST_DATA = (
    ("apple\n", "Apple Cinema"),
    ("sony\n", "Sony"),
    ("canon\n", "Canon EOS 5D"),
)


@pytest.mark.parametrize("keyword,expected_link", TEST_DATA)
def test_search_apple(get_main_page, keyword, expected_link):
    get_main_page.open()
    get_main_page.search(keyword)
    apple_link = get_main_page.search_for_link(expected_link)

    assert apple_link
