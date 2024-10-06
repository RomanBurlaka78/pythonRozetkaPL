from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators.locators import Locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def get_categories(self):
        return self.driver.find_elements(By.CSS_SELECTOR, Locators.homepage.get("categories"))

    def show_categories(self):
        return [i.text for i in self.get_categories]




