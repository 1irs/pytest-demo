from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://54.183.112.233/")

    def search(self, keyword: str):
        search = self.driver.find_element(By.NAME, "search")
        search.send_keys(keyword)

    def search_for_link(self, text: str) -> WebElement:
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, text)
